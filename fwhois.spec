Summary:	A finger-style whois program.
Name:		fwhois
Version:	1.00
Release:	12
Copyright:	BSD
Group:		Applications/Internet
Source:		ftp://sunsite.unc.edu/pub/Linux/distributions/slackware/source/n/tcpip/fwhois-1.00.tar.gz
Buildroot:	/tmp/%{name}-%{version}-root

%description
The fwhois program is a different style of the whois program.  Both
fwhois and whois query Internet whois databases to find information
about system users.  Fwhois is smaller and more compact than whois, and
runs in a different manner.

Install fwhois if you or your system's users need a program for querying
whois databases.  You may also want to install whois, and then decide for
yourself which program you prefer. 

%prep
%setup -q

%build
gcc $RPM_OPT_FLAGS -s fwhois.c -o fwhois

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -s fwhois $RPM_BUILD_ROOT/%{_bindir}/fwhois
ln -sf fwhois $RPM_BUILD_ROOT/%{_bindir}/whois

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/fwhois
%attr(755,root,root) %{_bindir}/whois
