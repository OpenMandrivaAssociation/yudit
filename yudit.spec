%define debug_package %nil

Name:       yudit
Version:    3.1.0
Release:    1
Group:      Editors
License:    GPLv2
Source0:    http://www.yudit.org/download/yudit-%{version}.tar.bz2 
# Here I define the directories with ttf files; and several ttf fonts
# we provide or that are widely used, in order to cover the most of unicode
# if this patch doesn't work after an upgrade please try to fix it (it is
# a very simple three-lines one) rather than discarding, as discarding it
# means we lose out-of-the box support for various languages -- pablo
Patch0: yudit-2.9.2-properties.patch
URL:        https://www.yudit.org/
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
%autosetup -p1
%configure2_5x

%build
%make_build

%install
%make_install

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
cp yudit64x64.png %{buildroot}%{_liconsdir}/%{name}.png
convert yudit64x64.png -geometry 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert yudit64x64.png -geometry 16x16 %{buildroot}%{_miconsdir}/%{name}.png


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Yudit
Name[ru]=Yudit
Type=Application
Description=Unicode Text Editor
Description[ru]=Текстовый редактор с поддержкой Unicode
Exec=yudit
Icon=yudit
Terminal=false
Categories=TextEditor;Utility;
EOF
 
# rpm complains and fails when there are installed but unpackaged files
# as we don't include those in the package, we delete them from the
# build tree -- pablo
rm -rf %{buildroot}%{_datadir}/yudit/src

%find_lang %{name}

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
