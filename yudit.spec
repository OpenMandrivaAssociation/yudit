%define name    yudit
%define version 2.9.0
%define release %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Group:      Editors
BuildRequires:  X11-devel freetype-devel gettext
License:    GPL
Conflicts:  netatalk < 2.0.3-3mdk
Source0:    http://www.yudit.org/download/yudit-%{version}.tar.bz2 
# Here I define the directories with ttf files; and several ttf fonts
# we provide or that are widely used, in order to cover the most of unicode
# if this patch doesn't work after an upgrade please try to fix it (it is
# a very simple three-lines one) rather than discarding, as discarding it
# means we lose out-of-the box support for various languages -- pablo
Patch0: yudit-2.7.6-properties.patch.bz2
URL:        http://www.yudit.org/
Summary:    Unicode Text Editor
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  imagemagick libx11-devel

%description
Yudit is a unicode text editor for the X Window System.
It does not need localized environment or unicode fonts.
It supports simultanious processing of many languages,
input methods, conversions for local character standards.
This package includes X11 editor interface, shell conversion
utilities and it also has support for postscript printing.
GNU (C) Gaspar Sinai <gsinai@iname.com> 

%prep
%setup -q 

%build

%configure2_5x
 
make

%install
rm -rf $RPM_BUILD_ROOT
 
%makeinstall_std

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}}
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
Categories=TextEditor;Utility;X-MandrivaLinux-MoreApplications-Editors;
EOF
 
%find_lang %{name}

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
%dir %{_datadir}/yudit
%dir %{_datadir}/yudit/data
%dir %{_datadir}/yudit/doc
%dir %{_datadir}/yudit/config
%dir %{_datadir}/yudit/fonts
%dir %{_datadir}/yudit/syntax
%{_datadir}/yudit/data/*
%{_datadir}/yudit/doc/*
%{_datadir}/yudit/config/*
%{_datadir}/yudit/fonts/*
%{_datadir}/yudit/syntax/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
# non standard translation directory
%dir %{_datadir}/yudit/locale
%lang(all) %{_datadir}/yudit/locale/*
