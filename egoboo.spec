Summary:	3D dungeon crawling game
Name:		egoboo
Version:	2.8.1
Release:	1
Epoch:		1
License:	GPLv3+
Group:		Games/Adventure
URL:		http://egoboo.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/egoboo/%{name}-%{version}.tar.gz
#Since upstream gives both source and data in one tarball, we split it between here and egoboo-data package :
#wget http://downloads.sourceforge.net/egoboo/%{name}-%{version}.tar.gz
#tar xvf %{name}-%{version}.tar.gz
#mkdir %{name}-data-%{version}
#cd %{name}-%{version}
#mv basicdat/ doc/ modules/ egoboo*ico ../%{name}-data-%{version}/
#cd ..
#tar Jcvf %{name}-%{version}.tar.xz %{name}-%{version}/
#tar Jcvf %{name}-data-%{version}.tar.xz %{name}-data-%{version}/
Source0:	%{name}-%{version}.tar.xz
Patch5:		egoboo-2.8.1-add-destdir.patch
Patch7:		egoboo-2.8.1-use-datadir-for-config.patch
Patch9:		egoboo-2.8.1-link-against-libm.patch
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_image-devel
BuildRequires:	mesaglu-devel
BuildRequires:	imagemagick
BuildRequires:	physfs-devel
BuildRequires:	dos2unix
Requires:	egoboo-data = %{epoch}:%{version}

%description
Egoboo is an open source project, using OpenGL and SDL(Simple
DirectMedia Layer) libraries. It is a 3d dungeon role playing
game in the spirit of NetHack. Nice colorful graphics, and
detailed models(using Quake2 modeling tools) make this game
stand out in the gaming open-source community.

%prep
%setup -q
%patch5 -p1 -b .destdir~
%patch7 -p1 -b .conf_dir~
%patch9 -p1 -b .libm~
for f in `find -name \*.c -o -name \*.h -o -name README\* -o -name change.log`; do
	dos2unix $f
	chmod 644 $f
done

%build
%make OPT='-DPREFIX=\"%{_prefix}\" -D_NIX_PREFIX -Wall %{optflags}'

%install
%makeinstall_std

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
%{_gamesdatadir}/%{name}/controls.txt
%{_gamesdatadir}/%{name}/setup.txt
%{_datadir}/applications/egoboo.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
