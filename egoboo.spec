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


%changelog
* Sun Jan 22 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:2.8.1-1
+ Revision: 765033
- add dos2unix buildrequires
- fix spurious-executable-perm & wrong-script-end-of-line-encoding
- strip game data from tarball (grabbed from Mageia)
- clean out legacy rpm junk
- link against libm (P9)

  + Zombie Ryushu <ryushu@mandriva.org>
    - fix make install
    - SIENT: Fix LDFlags
    - SIENT: Fix LDFlags
    - Fix LDFlags
    - Upgrade to 2.8.1
    - Upgrade to 2.8.1

* Sat Oct 02 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:2.8.0-2mdv2011.0
+ Revision: 582610
- fix infinite loop which makes the game freeze when selecting player (P8)

* Thu Sep 23 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:2.8.0-1mdv2011.0
+ Revision: 580671
- split out data from tarball
- add DESTDIR support for install (P5)
- disable unsupported GL extension (P6)
- use datadir for non-user configurations (P7)
- compile with %%{optflags}
- add missing source files to build target (P3)
- create missing 'enet/lib' directory (P4)
- add missing 'physfs-devel' buildrequires

  + Zombie Ryushu <ryushu@mandriva.org>
    - Attempt to upgrade to 2.8.0
    - Attempt to upgrade to 2.8.0

* Sat May 16 2009 Samuel Verschelde <stormi@mandriva.org> 1:2.7.7-2mdv2010.0
+ Revision: 376436
- fix str fmt
- add to AdventureGame; category

* Sun Nov 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:2.7.7-1mdv2009.1
+ Revision: 308497
- add buildrequires on SDL_image-devel
- fix requires for egoboo-data
- sync sources
- update to new version 2.7.7
- fix urls
- move icons to fd.o compliant directory
- spec file clean

* Fri Aug 01 2008 Funda Wang <fwang@mandriva.org> 1:2.6.4-1mdv2009.0
+ Revision: 259618
- clearify license
- New version 2.6.4

* Tue Jul 15 2008 Funda Wang <fwang@mandriva.org> 1:2.6.3b-1mdv2009.0
+ Revision: 235743
- New version 2.6.3b
- drop debian patch
- New version 2.6.3b

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 16 2007 Emmanuel Andry <eandry@mandriva.org> 2.22-9mdv2008.0
+ Revision: 88695
- drop old menu
- uncompress patch
- Import egoboo



* Tue Sep 12 2006 Emmanuel Andry <eandry@mandriva.org> 2.22-8mdv2007.0
- add buildrequires ImageMagick

* Sun Sep 10 2006 Emmanuel Andry <eandry@mandriva.org> 2.22-7mdv2007.0
- buildrequires desktop-file-utils

* Mon Aug 28 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.22-6mdv2007.0
- sync source, patches, etc. with debian as upstream seems dead
- split package
- xdg menu
- fix file encoding with 'dos2unix'
- cleanups

* Fri May 06 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.22-5mdk
- lib64 fix
- %%mkrel
- fix summary-ended-with-dot

* Fri Aug 20 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.22-4mdk
- rebuild
- fix summary macro to avoid possible conflicts if we were to build debug package
- fix buildrequires (lib64..)
- don't bzip2 icons in src.rpm

* Sun Jul 20 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.22-3mdk
- don't use soundwrapper (David Walser)

* Tue Mar 11 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.22-2mdk
- Added libMesaGLU-devel to BuildRequires

* Thu Nov 19 2002 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.22-1mdk
- First mdk-release
