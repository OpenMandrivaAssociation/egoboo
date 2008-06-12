%define name	egoboo
%define version	2.22
%define	rel	9
%define release %mkrel %{rel}
%define Summary 3D dungeon crawling game

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}_%{version}.orig.tar.gz
Patch0:		egoboo_2.22-28.diff
License:	GPL
Group:		Games/Adventure
URL:		http://egoboo.sourceforge.net/
Summary:	%{Summary}
BuildRequires:	SDL-devel mesaglu-devel dos2unix desktop-file-utils ImageMagick
Requires:	egoboo-data >= 2.220
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Egoboo is an open source project, using OpenGL and SDL(Simple
DirectMedia Layer) libraries. It is a 3d dungeon role playing
game in the spirit of NetHack. Nice colorful graphics, and
detailed models(using Quake2 modeling tools) make this game
stand out in the gaming open-source community.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .debian
dos2unix egoboo.txt change.log

%build
%make DESTDIR=%{_prefix} BIN_PATH=%{_gamesbindir} SHARE_PATH=%{_gamesdatadir} FLAGS="-D_LINUX $RPM_OPT_FLAGS" LIBDIR="-L%{_libdir}"

%install
rm -rf %{buildroot}
install -d %{buildroot}{%{_gamesbindir},%{_sysconfdir}/egoboo}
%{makeinstall_std}

install -m644 debian/egoboo.desktop -D %{buildroot}%{_datadir}/applications/egoboo.desktop
desktop-file-install	--vendor="" \
			--remove-category="Application" \
			--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

install -d %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert -resize 16x16 debian/egoboo.xpm %{buildroot}%{_miconsdir}/%{name}.png
convert -resize 32x32 debian/egoboo.xpm %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 48x48 debian/egoboo.xpm %{buildroot}%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{name}.txt change.log
%{_gamesbindir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_datadir}/applications/egoboo.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

