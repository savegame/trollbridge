# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-trollbridge
Summary:    TRaveller's OLympus Bridge
Version:    0.1.1
Release:    2
Group:      Applications/Multimedia
License:    GPL
#Source0: https://github.com/example/app/archive/v%{version}.tar.gz
#Requires:   mapplauncherd-booster-silica-qt5
#Requires:   nemo-qml-plugin-thumbnailer-qt5
Requires:   sailfishsilica-qt5
#Requires:   qt5-qtdocgallery
BuildRequires:  pkgconfig(sailfishapp)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Core)
#BuildRequires:  pkgconfig(qdeclarative5-boostable)
BuildRequires:  desktop-file-utils

%description
TRaveller's OLympus Bridge is an app for controlling Olympus OM-D/PEN/Air cameras with integrated WiFi.

%prep
# >> setup
#%setup -q -n example-app-%{version}
rm -rf vendor
# << setup

%build
# >> build pre
GOPATH=%(pwd):~/
GOROOT=~/go
export GOPATH GOROOT
cd %(pwd)
if [ $DEB_HOST_ARCH == "armel" ]
then
~/go/bin/linux_arm/go build -ldflags "-s" -o %{name} 
else
~/go/bin/go build -ldflags "-s" -o %{name}
fi
# << build pre

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
install -d %{buildroot}%{_bindir}
install -p -m 0755 %(pwd)/%{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_datadir}/%{name}/qml
install -d %{buildroot}%{_datadir}/%{name}/qml/i18n
install -m 0444 -t %{buildroot}%{_datadir}/%{name}/qml *.qml
install -m 0444 -t %{buildroot}%{_datadir}/%{name}/qml/i18n i18n/*.qm
install -d %{buildroot}%{_datadir}/icons/hicolor/86x86/apps
install -m 0444 -t %{buildroot}%{_datadir}/icons/hicolor/86x86/apps data/%{name}.png
install -p %(pwd)/trollbridge.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/qml
%{_datadir}/%{name}/qml/i18n
%{_datadir}/icons/hicolor/86x86/apps
%{_bindir}
# >> files
# << files