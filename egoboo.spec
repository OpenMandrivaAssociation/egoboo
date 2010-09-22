%define oname	Egoboo
Summary:	3D dungeon crawling game
Name:		egoboo
Version:	2.8.0
Release:	%mkrel 1
Epoch:		1
License:	GPLv3+
Group:		Games/Adventure
URL:		http://egoboo.sourceforge.net/
Source0:	http://downloads.sourceforge.net/egoboo/%{name}-%{version}.tar.bz2
Patch1:		egoboo-2.6.3b-fix-startup-script.patch
Patch2:		egoboo-2.7.7-fix-str-fmt.patch
Patch3:		egoboo-2.8.0-add-missing-source-to-make-target.patch
Patch4:		egoboo-2.8.0-create-enet-lib-directory.patch
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_image-devel
BuildRequires:	mesaglu-devel
BuildRequires:	imagemagick
BuildRequires:	physfs-devel
Requires:	egoboo-data = %{epoch}:%{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Egoboo is an open source project, using OpenGL and SDL(Simple
DirectMedia Layer) libraries. It is a 3d dungeon role playing
game in the spirit of NetHack. Nice colorful graphics, and
detailed models(using Quake2 modeling tools) make this game
stand out in the gaming open-source community.

%prep
%setup -q -n %{oname}\ %{version}
# %patch1 -p0 -b .script
# %patch2 -p1 -b .str-fmt
%patch3 -p1 -b .missing_src~
%patch4 -p1 -b .enet_lib~

%build
%make -C enet OPT='-Wall %{optflags}'
%make all OPT='-DPREFIX="%{_prefix}" -Wall %{optflags}'

# convert res/egoboo.ico %{name}.png

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_gamesbindir}
pushd game
install -m 755 -D %{name} %{buildroot}%{_gamesbindir}/%{name}.real
install -m 755 -D %{name}.sh %{buildroot}%{_gamesbindir}/%{name}
popd

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Egoboo
Comment=A top down graphical (3D) RPG in the spirit of Nethack
Exec=%{_gamesbindir}/egoboo
Icon=egoboo
Terminal=false
StartupNotify=false
Type=Application
Categories=Game;RolePlaying;AdventureGame;
EOF

mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert -resize 16x16 %{name}-0.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert -resize 32x32 %{name}-0.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -resize 48x48 %{name}-0.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

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
%{_iconsdir}/hicolor/*/apps/%{name}.png
