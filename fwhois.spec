Summary:	A finger-style whois program
Summary(de):	Finger-artiges whois
Summary(es):	Whois parecido con salida del finger
Summary(fr):	Un whois dans le style finger
Summary(ja):	finger ¥¹¥¿¥¤¥ë¤Î whois ¥×¥í¥°¥é¥à
Summary(pl):	Program do odpytywania bazy whois podobny w obs³udze do fingera
Summary(pt_BR):	Whois parecido com saída do finger
Summary(tr):	finger tarzý whois
Name:		fwhois
Version:	1.00
Release:	16
License:	BSD
Group:		Applications/Networking
Source0:	ftp://sunsite.unc.edu/pub/Linux/distributions/slackware/source/n/tcpip/%{name}-%{version}.tar.gz
# Source0-md5:	13648b9ff2aa2deb7910c1a5a4bec931
Patch0:		%{name}-nicname.patch
Patch1:		%{name}-crsnic.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fwhois program is a different style of the whois program. Both
fwhois and whois query Internet whois databases to find information
about system users. Fwhois is smaller and more compact than whois, and
runs in a different manner.

Install fwhois if you or your system's users need a program for
querying whois databases. You may also want to install whois, and then
decide for yourself which program you prefer.

%description -l de
Dies ist das 'WHOIS'-Programm. Es gestattet Ihnen, in den
Whois-Datenbanken rund um die Welt nach Personen zu suchen.

%description -l es
Este es el programa "whois". Permite encontrar información sobre
Personas, almacenadas en los bancos de datos "whois" de todo el mundo.

%description -l fr
Programme « whois ». Il vous permet d'obtenir des informations sur les
personnes répertoriées dans les bases de données whois de part le
monde.

%description -l ja
fwhois ¥×¥í¥°¥é¥à¤Ï whois ¥×¥í¥°¥é¥à¤ÎÊÌ¤Î¥¹¥¿¥¤¥ë¤Î¤â¤Î¤Ç¤¢¤ë¡£
fwhois ¤È whois ¤ÎÎ¾Êý¤È¤â¥·¥¹¥Æ¥à¥æ¡¼¥¶¤Ë¤Ä¤¤¤Æ¤Î¾ðÊó¤òÃµ¤¹¤¿¤á¤Î
Internet whois ¥Ç¡¼¥¿¥Ù¡¼¥¹¤Ë¿Ò¤Í¤ë¡£fwhois ¤Ï whois ¤è¤ê¤â¾®¤µ¤¯¤Æ¤è¤ê
¥³¥ó¥Ñ¥¯¥È¤Ç°ã¤Ã¤¿ÊýË¡¤Ç¼Â¹Ô¤¹¤ë¡£

¤â¤·¤¢¤Ê¤¿¤¬¥·¥¹¥Æ¥à¥æ¡¼¥¶¤Ç whois ¥Ç¡¼¥¿¥Ù¡¼¥¹¤Ë¿Ò¤Í¤ë¥×¥í¥°¥é¥à¤òÉ¬Í×¤Ê¤é
fwhois ¤ò¥¤¥ó¥¹¥È¡¼¥ë¤·¤Ê¤µ¤¤¡£¤¢¤Ê¤¿¤Ï¤Þ¤¿ whois ¤ò¥¤¥ó¥¹¥È¡¼¥ë¤·¤¿¤¤¤Ç
¤¢¤í¤¦¤¬¡¢¤É¤Á¤é¤Î¥×¥í¥°¥é¥à¤¬¹¥¤Þ¤·¤¤¤«¤Ï¼«Ê¬¤Ç·è¤á¤Ê¤µ¤¤¡£

%description -l pl
Program fwhois to jedna z wersji programu whois. Zarówno fwhois jak i
whois kieruj± zapytania do internetowych baz danych whois by otrzymaæ
informacje o u¿ytkownikach systemu. Fwhois jest mniejszym programem i
uruchamia siê w inny sposób.

Nale¿y zainstalowaæ fwhois je¶li potrzebuje sie programu do kierowania
zapytañ do baz danych whois. Mo¿na równie¿ zainstalowaæ whois a potem
dokonaæ wyboru miêdzy oboma programami.

%description -l pt_BR
Este é o programa "whois". Ele permite achar informações sobre pessoas
armazenadas nos bancos de dados "whois" do mundo inteiro.

%description -l tr
whois ile dünyadaki whois veri tabanlarýnda kaydý bulunan kiþiler
hakkýnda bilgi edinebilirsiniz.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__cc} %{rpmcflags} %{rpmldflags} fwhois.c -o fwhois

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install fwhois $RPM_BUILD_ROOT%{_bindir}/fwhois

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/fwhois
