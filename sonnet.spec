#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : sonnet
Version  : 5.49.0
Release  : 2
URL      : https://download.kde.org/stable/frameworks/5.49/sonnet-5.49.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.49/sonnet-5.49.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.49/sonnet-5.49.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: sonnet-bin
Requires: sonnet-lib
Requires: sonnet-license
Requires: sonnet-data
BuildRequires : aspell-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : pkg-config
BuildRequires : pkgconfig(enchant)
BuildRequires : pkgconfig(hunspell)
BuildRequires : qtbase-dev qtbase-extras mesa-dev
BuildRequires : zlib-dev

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
Requires: sonnet-data
Requires: sonnet-license

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
Requires: sonnet-lib
Requires: sonnet-bin
Requires: sonnet-data
Provides: sonnet-devel

%description dev
dev components for the sonnet package.


%package lib
Summary: lib components for the sonnet package.
Group: Libraries
Requires: sonnet-data
Requires: sonnet-license

%description lib
lib components for the sonnet package.


%package license
Summary: license components for the sonnet package.
Group: Default

%description license
license components for the sonnet package.


%prep
%setup -q -n sonnet-5.49.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534106488
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1534106488
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/sonnet
cp COPYING.LIB %{buildroot}/usr/share/doc/sonnet/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gentrigrams
/usr/bin/parsetrigrams

%files data
%defattr(-,root,root,-)
/usr/share/kf5/sonnet/trigrams.map
/usr/share/locale/af/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/as/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ast/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/be/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/br/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/crh/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/da/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/de/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/el/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/es/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/et/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ha/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/he/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/hy/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/id/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/is/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/it/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/km/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/kn/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/or/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ps/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/se/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/si/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/te/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/th/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/tt/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/sonnet5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/sonnet5_qt.qm

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/SonnetCore/Sonnet/BackgroundChecker
/usr/include/KF5/SonnetCore/Sonnet/GuessLanguage
/usr/include/KF5/SonnetCore/Sonnet/Speller
/usr/include/KF5/SonnetCore/sonnet/backgroundchecker.h
/usr/include/KF5/SonnetCore/sonnet/guesslanguage.h
/usr/include/KF5/SonnetCore/sonnet/sonnetcore_export.h
/usr/include/KF5/SonnetCore/sonnet/speller.h
/usr/include/KF5/SonnetUi/Sonnet/ConfigDialog
/usr/include/KF5/SonnetUi/Sonnet/ConfigWidget
/usr/include/KF5/SonnetUi/Sonnet/Dialog
/usr/include/KF5/SonnetUi/Sonnet/DictionaryComboBox
/usr/include/KF5/SonnetUi/Sonnet/Highlighter
/usr/include/KF5/SonnetUi/Sonnet/SpellCheckDecorator
/usr/include/KF5/SonnetUi/sonnet/configdialog.h
/usr/include/KF5/SonnetUi/sonnet/configwidget.h
/usr/include/KF5/SonnetUi/sonnet/dialog.h
/usr/include/KF5/SonnetUi/sonnet/dictionarycombobox.h
/usr/include/KF5/SonnetUi/sonnet/highlighter.h
/usr/include/KF5/SonnetUi/sonnet/sonnetui_export.h
/usr/include/KF5/SonnetUi/sonnet/spellcheckdecorator.h
/usr/include/KF5/sonnet_version.h
/usr/lib64/cmake/KF5Sonnet/KF5SonnetConfig.cmake
/usr/lib64/cmake/KF5Sonnet/KF5SonnetConfigVersion.cmake
/usr/lib64/cmake/KF5Sonnet/KF5SonnetTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Sonnet/KF5SonnetTargets.cmake
/usr/lib64/libKF5SonnetCore.so
/usr/lib64/libKF5SonnetUi.so
/usr/lib64/qt5/mkspecs/modules/qt_SonnetCore.pri
/usr/lib64/qt5/mkspecs/modules/qt_SonnetUi.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5SonnetCore.so.5
/usr/lib64/libKF5SonnetCore.so.5.49.0
/usr/lib64/libKF5SonnetUi.so.5
/usr/lib64/libKF5SonnetUi.so.5.49.0
/usr/lib64/qt5/plugins/kf5/sonnet/sonnet_aspell.so
/usr/lib64/qt5/plugins/kf5/sonnet/sonnet_hunspell.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/sonnet/COPYING.LIB
