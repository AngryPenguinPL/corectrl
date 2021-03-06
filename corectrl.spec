

Name:           corectrl
Version:        1.0.5
Release:        1
Summary:        Hardware control tools with nice GUI for Linux
License:        GPLv3+
URL:            https://gitlab.com/corectrl/corectrl
Source0:        https://gitlab.com/corectrl/corectrl/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

#Qt stack
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Charts)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5QuickTemplates2)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(botan-2)
BuildRequires:  pkgconfig(x11)

BuildRequires:  desktop-file-utils

Requires:       dbus
Requires:       hicolor-icon-theme
Requires:       polkit
Requires:       qt5-qtquickcontrols2
# For pidof (???)
Requires:       procps-ng
Requires:       sysvinit-tools
# For pci.ids
Requires:       hwdata

Recommends:     glxinfo
Recommends:     mesa-demos
# For lscpu
Recommends:     util-linux
#NOT AVAILABLE IN CÓKIER yet
#Recommends:    vulkan-tools

%description
CoreCtrl is a linux application that allows you to control 
with ease your computer hardware using application profiles.
The default settings are defined on a global profile. 
You can also create as many custom profiles as you want, each of them defining its own settings. 
Each custom profile is associated to one program executable. 
When the associated program is launched, the settings of the profile will be applied automatically. 
Later on, when the program ends, the previous settings are restored.
You can choose which elements of the system will be controlled by a profile, 
even for the global profile. In this way, some parts of the system will be left untouched when the profile is applied. 
This will allow you to control those parts using other applications 
or define a global behavior for a part while controlling other parts with custom profiles. 
See How profiles works for more info on this topic.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake -G Ninja \
    -DBUILD_TESTING=OFF \
    -DCMAKE_BUILD_TYPE=Release
    
%ninja -C build

%install
%ninja_install -C

%files
#!
