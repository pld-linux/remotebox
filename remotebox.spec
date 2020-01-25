# TODO
# - perl-Gtk2 dependency not autogenerated
# - start menu integration
# NOTE
# - on server you need virtualbox and virtualbox extension pack (for rdp and
#   pxe boot) installed
Summary:	Open Source VirtualBox Client with Remote Management
Name:		remotebox
Version:	1.4
Release:	1
License:	GPL v2+
Group:		Daemons
URL:		http://remotebox.knobgoblin.org.uk/
Source0:	http://remotebox.knobgoblin.org.uk/downloads/RemoteBox-%{version}.tar.bz2
# Source0-md5:	974a24792a55ff47be35125f6377ca67
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
Requires:	perl-Gtk2
Suggests:	VirtualBox >= 4.2
Suggests:	VirtualBox-Extension-Pack
Suggests:	rdesktop
Suggests:	xdg-open
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RemoteBox is a GUI tool which lets you administer guests or virtual
machines running under VirtualBox on a remote server or even the same
local machine. VirtualBox is traditionally a desktop-side
virtualisation solution. The goal of RemoteBox is to provide a GUI
that should be familiar to VirtualBox users whist allowing them to
administer a remote installation of VirtualBox.

%prep
%setup -q -n RemoteBox-%{version}

%{__sed} -i -e '
	s|\$Bin/share/remotebox|%{_datadir}/%{name}|
	s|$Bin/docs|%{_docdir}/%{name}-%{version}|
' %{name} share/%{name}/rbox_gui_init.pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a share/%{name}/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
