Summary:	A finger-style whois program
Summary(de.UTF-8):	Finger-artiges whois
Summary(es.UTF-8):	Whois parecido con salida del finger
Summary(fr.UTF-8):	Un whois dans le style finger
Summary(ja.UTF-8):	finger スタイルの whois プログラム
Summary(pl.UTF-8):	Program do odpytywania bazy whois podobny w obsłudze do fingera
Summary(pt_BR.UTF-8):	Whois parecido com saída do finger
Summary(tr.UTF-8):	finger tarzı whois
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

%description -l de.UTF-8
Dies ist das 'WHOIS'-Programm. Es gestattet Ihnen, in den
Whois-Datenbanken rund um die Welt nach Personen zu suchen.

%description -l es.UTF-8
Este es el programa "whois". Permite encontrar información sobre
Personas, almacenadas en los bancos de datos "whois" de todo el mundo.

%description -l fr.UTF-8
Programme « whois ». Il vous permet d'obtenir des informations sur les
personnes répertoriées dans les bases de données whois de part le
monde.

%description -l ja.UTF-8
fwhois プログラムは whois プログラムの別のスタイルのものである。
fwhois と whois の両方ともシステムユーザについての情報を探すための
Internet whois データベースに尋ねる。fwhois は whois よりも小さくてより
コンパクトで違った方法で実行する。

もしあなたがシステムユーザで whois データベースに尋ねるプログラムを必要なら
fwhois をインストールしなさい。あなたはまた whois をインストールしたいで
あろうが、どちらのプログラムが好ましいかは自分で決めなさい。

%description -l pl.UTF-8
Program fwhois to jedna z wersji programu whois. Zarówno fwhois jak i
whois kierują zapytania do internetowych baz danych whois by otrzymać
informacje o użytkownikach systemu. Fwhois jest mniejszym programem i
uruchamia się w inny sposób.

Należy zainstalować fwhois jeśli potrzebuje sie programu do kierowania
zapytań do baz danych whois. Można również zainstalować whois a potem
dokonać wyboru między oboma programami.

%description -l pt_BR.UTF-8
Este é o programa "whois". Ele permite achar informações sobre pessoas
armazenadas nos bancos de dados "whois" do mundo inteiro.

%description -l tr.UTF-8
whois ile dünyadaki whois veri tabanlarında kaydı bulunan kişiler
hakkında bilgi edinebilirsiniz.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

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
