%define name	egoboo
%define version	2.6.4
%define	rel	1
%define release %mkrel %{rel}
%define Summary 3D dungeon crawling game

Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
Source0:	%name-source-%version.tar.gz
Patch1:		egoboo-2.6.3b-fix-startup-script.patch
License:	GPL
Group:		Games/Adventure
URL:		http://egoboo.sourceforge.net/
Summary:	%{Summary}
BuildRequires:	SDL-devel SDL_mixer-devel SDL_ttf-devel
BuildRequires:	mesaglu-devel ImageMagick
Requires:	egoboo-data 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Egoboo is an open source project, using OpenGL and SDL(Simple
DirectMedia Layer) libraries. It is a 3d dungeon role playing
game in the spirit of NetHack. Nice colorful graphics, and
detailed models(using Quake2 modeling tools) make this game
stand out in the gaming open-source community.

%prep
%setup -q -n %name-source-%version
%patch1 -p0 -b .script

%build
cd game
make -f Makefile.unix OPT="%{optflags}"
cd -
convert res/egoboo.ico %name.png

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_gamesbindir}
cd game
install -m 755 -D %name %buildroot%{_gamesbindir}/%name.real
install -m 755 -D %name.sh %buildroot%{_gamesbindir}/%name
cd -

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%name.desktop <<EOF
[Desktop Entry]
Name=Egoboo
Comment=A top down graphical (3D) RPG in the spirit of Nethack
Exec=%{_gamesbindir}/egoboo
Icon=egoboo
Terminal=false
StartupNotify=false
Type=Application
Categories=Game;RolePlaying;
EOF

install -d %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert -resize 16x16 %name-0.png %{buildroot}%{_miconsdir}/%{name}.png
convert -resize 32x32 %name-0.png %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 48x48 %name-0.png %{buildroot}%{_liconsdir}/%{name}.png

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
%doc README.Linux game/change.log
%{_gamesbindir}/%{name}*
%{_datadir}/applications/egoboo.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
