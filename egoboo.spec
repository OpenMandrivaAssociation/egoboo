Summary:	3D dungeon crawling game
Name:		egoboo
Version:	2.8.1
Release:	1
Epoch:		1
License:	GPLv3+
Group:		Games/Adventure
URL:		http://egoboo.sourceforge.net/
Source0:	http://downloads.sourceforge.net/egoboo/%{name}-%{version}.tar.xz
Patch3:		egoboo-2.8.0-add-missing-source-to-make-target.patch
Patch4:		egoboo-2.8.0-create-enet-lib-directory.patch
Patch5:		egoboo-2.8.0-add-destdir.patch
Patch6:		egoboo-2.8.0-disable-unsupported-gl-extension.patch
Patch7:		egoboo-2.8.0-use-datadir-for-config.patch
Patch8:		egoboo-2.8.0-fix-infinite-loop.patch
Patch9:		egoboo-2.8.1-link-against-libm.patch
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_image-devel
BuildRequires:	mesaglu-devel
BuildRequires:	imagemagick
BuildRequires:	physfs-devel
Requires:	egoboo-data = %{epoch}:%{version}

%description
Egoboo is an open source project, using OpenGL and SDL(Simple
DirectMedia Layer) libraries. It is a 3d dungeon role playing
game in the spirit of NetHack. Nice colorful graphics, and
detailed models(using Quake2 modeling tools) make this game
stand out in the gaming open-source community.

%prep
%setup -q
# %patch3 -p0 -b .missing_src~
# %patch4 -p0 -b .enet_lib~
# %patch5 -p1 -b .destdir~
# %patch6 -p1 -b .gl_ext~
# %patch7 -p1 -b .conf_dir~
# %patch8 -p1 -b .infinite_loop~
%patch9 -p1 -b .libm~

%build
pushd src
%make all LIBS="-lm" OPT='-DPREFIX=\"%{_prefix}\" -D_NIX_PREFIX -Wall %{optflags}'
popd
%install
pushd src/game
%makeinstall_std PREFIX=%{buildroot}/%{_prefix}/
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
convert egoboo1.ico egoboo.png
convert -resize 16x16 egoboo-1.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert -resize 32x32 egoboo-1.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -resize 48x48 egoboo-1.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%files
%doc README.Linux game/change.log
%{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}/players
%{_gamesdatadir}/%{name}/players/*
%{_gamesdatadir}/%{name}/controls.txt
%{_gamesdatadir}/%{name}/setup.txt
%{_datadir}/applications/egoboo.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
