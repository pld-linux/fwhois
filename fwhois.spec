Summary:	A finger-style whois program
Summary(de):	Finger-artiges whois
Summary(fr):	Un whois dans le style finger
Summary(tr):	finger tarzý whois
Name:		fwhois
Version:	1.00
Release:	13
Copyright:	BSD
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source:		ftp://sunsite.unc.edu/pub/Linux/distributions/slackware/source/n/tcpip/fwhois-1.00.tar.gz
Buildroot:	/tmp/%{name}-%{version}-root

%description
The fwhois program is a different style of the whois program. Both
fwhois and whois query Internet whois databases to find information
about system users. Fwhois is smaller and more compact than whois, and
runs in a different manner.

Install fwhois if you or your system's users need a program for querying
whois databases. You may also want to install whois, and then decide for
yourself which program you prefer. 

%description -l pl
Program fwhois to jedna z wersji programu whois. Zarówno fwhois jak i whois
kieruj± zapytania do internetowych baz danych whois by otrzymaæ informacje
o u¿ytkownikach systemu. Fwhois jest mniejszym programem i uruchamia siê w
inny sposób.

Nale¿y zainstalowaæ fwhois je¶li potzrebuje sie programu do kierowania zapytañ
do baz danych whois. Mo¿na równie¿ zainstalowac whois a potem dokonaæ wyboru
miêdzy oboma programami.

%description -l de
Dies ist das 'WHOIS'-Programm. Es gestattet Ihnen, in den Whois-Datenbanken
rund um die Welt nach Personen zu suchen.

%description -l fr
Programme « whois ». Il vous permet d'obtenir des informations sur les
personnes répertoriées dans les bases de données whois de part le monde.

%description -l tr
whois ile dünyadaki whois veri tabanlarýnda kaydý bulunan kiþiler hakkýnda
bilgi edinebilirsiniz.

%prep
%setup -q

%build
gcc $RPM_OPT_FLAGS -s fwhois.c -o fwhois

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -s fwhois $RPM_BUILD_ROOT/%{_bindir}/fwhois

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/fwhois
