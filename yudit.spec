%define debug_package %nil

Name:       yudit
Version:    2.9.2
Release:    5
Group:      Editors
License:    GPLv2
Conflicts:  netatalk < 2.0.3-3mdk
Source0:    http://www.yudit.org/download/yudit-%{version}.tar.bz2 
# Here I define the directories with ttf files; and several ttf fonts
# we provide or that are widely used, in order to cover the most of unicode
# if this patch doesn't work after an upgrade please try to fix it (it is
# a very simple three-lines one) rather than discarding, as discarding it
# means we lose out-of-the box support for various languages -- pablo
Patch0: yudit-2.9.2-properties.patch
URL:        http://www.yudit.org/
Summary:    Unicode Text Editor
BuildRequires:  imagemagick pkgconfig(x11)

%description
Yudit is a unicode text editor for the X Window System.
It does not need localized environment or unicode fonts.
It supports simultanious processing of many languages,
input methods, conversions for local character standards.
This package includes X11 editor interface, shell conversion
utilities and it also has support for postscript printing.

%prep
%setup -q 

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
 
%makeinstall_std

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert gnome-%{name}.png -geometry 48x48 %{buildroot}%{_liconsdir}/%{name}.png
convert gnome-%{name}.png -geometry 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert gnome-%{name}.png -geometry 16x16 %{buildroot}%{_miconsdir}/%{name}.png


mkdir -p %{buildroot}%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Yudit
Type=Application
Description=Unicode Text Editor
Exec=yudit
Icon=yudit
Terminal=false
Categories=TextEditor;Utility;
EOF
 
%find_lang %{name} || touch %name.lang

# rpm complains and fails when there are installed but unpackaged files
# as we don't include those in the package, we delete them from the
# build tree -- pablo
rm -rf $RPM_BUILD_ROOT%{_datadir}/yudit/src

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post 
%{update_menus}
%endif

%if %mdkversion < 200900
%postun 
%{clean_menus}
%endif


%files -f %{name}.lang
%defattr (-, root, root, 755)
%doc *.TXT
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/applications/*.desktop
%{_datadir}/yudit
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


%changelog
* Fri Jan 21 2011 Funda Wang <fwang@mandriva.org> 2.9.2-3mdv2011.0
+ Revision: 632001
- drop unused BRs

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.9.2-2mdv2011.0
+ Revision: 615762
- the mass rebuild of 2010.1 packages

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.9.2-1mdv2010.1
+ Revision: 515726
- update to 2.9.2

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 2.9.0-2mdv2010.0
+ Revision: 435375
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Jun 25 2008 Funda Wang <fwang@mandriva.org> 2.9.0-1mdv2009.0
+ Revision: 228850
- New version 2.9.0

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 2.8.1-1mdv2008.1
+ Revision: 141006
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Thu Apr 19 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2.8.1-1mdv2008.0
+ Revision: 15191
- Fix BuildRequires
- Kill old debian menu
- Import yudit


 

* Tue Aug 01 2006 Charles A Edwards <eslrahc@mandriva.org> 2.8.1-1mdv2007.0
- 2.8.1
- update spec, drop unneeded and some clean-up
- xdg

* Tue Aug 23 2005 Stew Benedict <sbenedict@mandriva.com> 2.7.6-5mdk
- conflicts for upgrades

* Mon Aug 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.7.6-4mdk
- Rebuild for new menu

* Mon Jun 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.7.6-3mdk
- REbuild

* Tue Mar 16 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 2.7.6-2mdk
- Take back our configuration improvements (to find and use all fonts
  we ship and be able to support out of the box a wide range of languages)
- changed Japanese input method to uim-anthy

* Sun Jan 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.7.6-1mdk
- 2.7.6
- drop and updated patches
- convert icons to png and don't bzip2 'em
- generate menu item during %%install in stead
- cosmetics
- add new locale
- update docs

* Mon Jul 14 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.7.5-1mdk
- 2.7.5
- drop and update patches
- add new locales

* Fri Jan 10 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 2.7.2-1mdk
- updated version to 2.7.2

* Wed Nov 06 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 2.6.4-1mdk
- updated version to 2.6.4

* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.6.2-3mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Thu Jul 25 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.6.2-2mdk
- Automated rebuild with gcc3.2

* Fri Jul 12 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 2.6.2-1mdk

* Wed May 29 2002 Stefan van der Eijk <stefan@eijk.nu> 2.6-2mdk
- BuildRequires

* Fri May 03 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 2.6-1mdk
- updated to 2.6

* Mon Jan 28 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 2.5.2-1mdk
- updated to 2.5.2, with OpenType support

* Fri Jan 18 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 2.5-3mdk
- Rebuild with an improved list of default ttf fonts

* Thu Dec 27 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.5-2mdk
- General cleanup.

* Thu Dec 27 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.5-1mdk
- 2.5 for general consumption.

* Wed Aug 29 2001 David BAUDENS <baudens@mandrakesoft.com> 2.4-2mdk
- Use new icons

* Sun Apr 08 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.4-1mdk
- Bump up to 2.4.
- Apply official yudit patch 1 for 2.4.

* Tue Feb 13 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.3-1mdk
- Bump up to 2.3 in cooker.

* Tue Jan 23 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.2-1mdk
- new and shiny source.
- use -j instead of -I when uncompressing bzip2 files with tar.

* Fri Jan 19 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.1-1mdk
- new and shiny source.

* Fri Nov 17 2000 David BAUDENS <baudens@mandrakesoft.com> 1.5-8mdk
- Rebuild with gcc-2.96 & glibc-2.2

* Mon Oct 02 2000 Daouda Lo <daouda@mandrakesoft.com> 1.5-7mdk
- change icons + more macrozif..
- use find_lang macro.
- let spechelper do its job ;-)
- patched to prevent yudit to find Tahoma font
- add some kmap files
 
* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.5-6mdk
- automatically added BuildRequires

* Sun Jul 23 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 1.5-5mdk
- makeinstall macro
- macroszifications
- BM
- Geoffrey Lee <snailtalk@mandrakesoft.com>
  - update menus and clean menus macro
  - tmppath
  - full src url

* Tue May  2 2000 Vincent Saugey <vince@mandrakesoft.com> 1.5-4mdk
- Fixed menu entry
- Add 16 and 32 icons

* Tue May 02 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.5-3mdk
- added URLs, now Yudit has its own web page!
- added a menu entry

* Thu Apr 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.5-2mdk
- fixed group

* Wed Dec 01 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- updated to 1.5
- merged with Nguyen-Dai Quy <daiquy.nguyen@ulg.ac.be> changes:
  added vietnamese locale (contributed by Lai Hoa`i Trie^'t
  <thlai@mail.usyd.edu.au>)

* Thu Nov  4 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix compilation with gcc2.95.

* Mon Aug 09 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- cleaned %%files
- added more encodings

* Sun Jul 18 1999 NGUYEN-DAI Quy <DaiQuy.Nguyen@ulg.ac.be>
- Added "telex" input Method for Vietnamese (VNtelex.kmap).
- Modified "vn.utf8" --> "vi.utf8"
- Added "fr.utf8" for French

* Wed Jul 14 1999 Triet H. Lai <thlai@ee.usyd.edu.au>
- Updated to version 1.3
- Added Vietnamese locale, unicode maps for VPS, TCVN,
  and system config file (yuditrc.vn).
