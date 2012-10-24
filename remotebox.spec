%include	/usr/lib/rpm/macros.perl
Summary:	Open Source VirtualBox Client with Remote Management
Name:		remotebox
Version:	0.4
Release:	0.1
License:	GPL
Group:		Daemons
URL:		http://remotebox.knobgoblin.org.uk/
Source0:	http://remotebox.knobgoblin.org.uk/downloads/RemoteBox-%{version}.tar
# Source0-md5:	984c107980053f478be302f136be7f27
BuildRequires:	perl-Gtk2
BuildRequires:	perl-SOAP-Lite
BuildRequires:	rpm-perlprov >= 4.1-13
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a share/remotebox/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__sed} -i -e 's|\$Bin/share/remotebox|%{_datadir}/%{name}|g' \
	$RPM_BUILD_ROOT%{_bindir}/%{name} $RPM_BUILD_ROOT%{_datadir}/%{name}/rbox_gui_init.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
