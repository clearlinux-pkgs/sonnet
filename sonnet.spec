#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v5
# autospec commit: c02b2fe
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : sonnet
Version  : 6.0.0
Release  : 77
URL      : https://download.kde.org/stable/frameworks/6.0/sonnet-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.0/sonnet-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.0/sonnet-6.0.0.tar.xz.sig
Summary  : Spelling framework for Qt5
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1
Requires: sonnet-bin = %{version}-%{release}
Requires: sonnet-data = %{version}-%{release}
Requires: sonnet-lib = %{version}-%{release}
Requires: sonnet-license = %{version}-%{release}
BuildRequires : aspell-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : hunspell-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(enchant)
BuildRequires : pkgconfig(hunspell)
BuildRequires : qt6base-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Sonnet
Multi-language spell checker
## Introduction
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports several different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.

%package bin
Summary: bin components for the sonnet package.
Group: Binaries
Requires: sonnet-data = %{version}-%{release}
Requires: sonnet-license = %{version}-%{release}

%description bin
bin components for the sonnet package.


%package data
Summary: data components for the sonnet package.
Group: Data

%description data
data components for the sonnet package.


%package dev
Summary: dev components for the sonnet package.
Group: Development
Requires: sonnet-lib = %{version}-%{release}
Requires: sonnet-bin = %{version}-%{release}
Requires: sonnet-data = %{version}-%{release}
Provides: sonnet-devel = %{version}-%{release}
Requires: sonnet = %{version}-%{release}

%description dev
dev components for the sonnet package.


%package lib
Summary: lib components for the sonnet package.
Group: Libraries
Requires: sonnet-data = %{version}-%{release}
Requires: sonnet-license = %{version}-%{release}

%description lib
lib components for the sonnet package.


%package license
Summary: license components for the sonnet package.
Group: Default

%description license
license components for the sonnet package.


%prep
%setup -q -n sonnet-6.0.0
cd %{_builddir}/sonnet-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711174816
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711174816
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sonnet
cp %{_builddir}/sonnet-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/sonnet/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/sonnet-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/sonnet/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/sonnet-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/sonnet/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/sonnet-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/sonnet/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/parsetrigrams6
/usr/bin/parsetrigrams6

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ar/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/as/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ast/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/az/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/be/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/bn/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/br/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/crh/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/csb/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/cy/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/da/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/de/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/el/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/es/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/et/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/fa/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/fy/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ga/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/gd/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/gu/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ha/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/he/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/hi/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/hne/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/hr/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/hu/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/hy/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/id/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/is/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/it/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/kk/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/km/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/kn/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ku/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/lb/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/lv/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/mai/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/mk/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ml/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/mr/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ms/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/nb/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/nds/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ne/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/oc/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/or/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/pa/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ps/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/se/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/si/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/sq/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/sr/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ta/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/te/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/tg/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/th/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/tt/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/ug/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/uz/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/vi/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/wa/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/xh/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/sonnet6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/sonnet6_qt.qm
/usr/share/qlogging-categories6/sonnet.categories
/usr/share/qlogging-categories6/sonnet.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/Sonnet/sonnet_version.h
/usr/include/KF6/SonnetCore/Sonnet/BackgroundChecker
/usr/include/KF6/SonnetCore/Sonnet/GuessLanguage
/usr/include/KF6/SonnetCore/Sonnet/Settings
/usr/include/KF6/SonnetCore/Sonnet/Speller
/usr/include/KF6/SonnetCore/sonnet/backgroundchecker.h
/usr/include/KF6/SonnetCore/sonnet/guesslanguage.h
/usr/include/KF6/SonnetCore/sonnet/settings.h
/usr/include/KF6/SonnetCore/sonnet/sonnetcore_export.h
/usr/include/KF6/SonnetCore/sonnet/speller.h
/usr/include/KF6/SonnetUi/Sonnet/ConfigDialog
/usr/include/KF6/SonnetUi/Sonnet/ConfigView
/usr/include/KF6/SonnetUi/Sonnet/ConfigWidget
/usr/include/KF6/SonnetUi/Sonnet/Dialog
/usr/include/KF6/SonnetUi/Sonnet/DictionaryComboBox
/usr/include/KF6/SonnetUi/Sonnet/Highlighter
/usr/include/KF6/SonnetUi/Sonnet/SpellCheckDecorator
/usr/include/KF6/SonnetUi/sonnet/configdialog.h
/usr/include/KF6/SonnetUi/sonnet/configview.h
/usr/include/KF6/SonnetUi/sonnet/configwidget.h
/usr/include/KF6/SonnetUi/sonnet/dialog.h
/usr/include/KF6/SonnetUi/sonnet/dictionarycombobox.h
/usr/include/KF6/SonnetUi/sonnet/highlighter.h
/usr/include/KF6/SonnetUi/sonnet/sonnetui_export.h
/usr/include/KF6/SonnetUi/sonnet/spellcheckdecorator.h
/usr/lib64/cmake/KF6Sonnet/KF6SonnetConfig.cmake
/usr/lib64/cmake/KF6Sonnet/KF6SonnetConfigVersion.cmake
/usr/lib64/cmake/KF6Sonnet/KF6SonnetTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Sonnet/KF6SonnetTargets.cmake
/usr/lib64/libKF6SonnetCore.so
/usr/lib64/libKF6SonnetUi.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6SonnetCore.so.6.0.0
/V3/usr/lib64/libKF6SonnetUi.so.6.0.0
/V3/usr/lib64/qt6/plugins/designer/sonnet6widgets.so
/V3/usr/lib64/qt6/plugins/kf6/sonnet/sonnet_aspell.so
/V3/usr/lib64/qt6/plugins/kf6/sonnet/sonnet_hunspell.so
/V3/usr/lib64/qt6/qml/org/kde/sonnet/libsonnetquickplugin.so
/usr/lib64/libKF6SonnetCore.so.6
/usr/lib64/libKF6SonnetCore.so.6.0.0
/usr/lib64/libKF6SonnetUi.so.6
/usr/lib64/libKF6SonnetUi.so.6.0.0
/usr/lib64/qt6/plugins/designer/sonnet6widgets.so
/usr/lib64/qt6/plugins/kf6/sonnet/sonnet_aspell.so
/usr/lib64/qt6/plugins/kf6/sonnet/sonnet_hunspell.so
/usr/lib64/qt6/qml/org/kde/sonnet/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/sonnet/libsonnetquickplugin.so
/usr/lib64/qt6/qml/org/kde/sonnet/qmldir
/usr/lib64/qt6/qml/org/kde/sonnet/sonnetquickplugin.qmltypes

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sonnet/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/sonnet/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/sonnet/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/sonnet/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
