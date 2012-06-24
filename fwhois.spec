Summary:	A finger-style whois program
Summary(de):	Finger-artiges whois
Summary(fr):	Un whois dans le style finger
Summary(tr):	finger tarz� whois
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
Program fwhois to jedna z wersji programu whois. Zar�wno fwhois jak i whois
kieruj� zapytania do internetowych baz danych whois by otrzyma� informacje
o u�ytkownikach systemu. Fwhois jest mniejszym programem i uruchamia si� w
inny spos�b.

Nale�y zainstalowa� fwhois je�li potzrebuje sie programu do kierowania zapyta�
do baz danych whois. Mo�na r�wnie� zainstalowac whois a potem dokona� wyboru
mi�dzy oboma programami.

%description -l de
Dies ist das 'WHOIS'-Programm. Es gestattet Ihnen, in den Whois-Datenbanken
rund um die Welt nach Personen zu suchen.

%description -l fr
Programme � whois �. Il vous permet d'obtenir des informations sur les
personnes r�pertori�es dans les bases de donn�es whois de part le monde.

%description -l tr
whois ile d�nyadaki whois veri tabanlar�nda kayd� bulunan ki�iler hakk�nda
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
