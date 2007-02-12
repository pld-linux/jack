%define         module jack

Summary:	Module for accessing CDDB and FreeDB
Summary(pl.UTF-8):   Moduł do łączenia z bazami CDDB i FreeDB
Name:		jack
Version:	3.1.1
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.home.unix-ag.org/arne/jack/%{module}-%{version}.tar.gz
# Source0-md5:	8ec8971380ba009249d1bb3d1b3e7344
URL:		http://www.home.unix-ag.org/arne/jack/
BuildRequires:	ncurses-devel
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
Requires:	ncurses
Requires:	python-CDDB
Requires:	python-ID3
Requires:	python-jack-cursesmodule = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jack is a python CDDA ripping program. It has been developed with one
main goal: making MP3s without having to worry.

%description -l pl.UTF-8
Jack jest programem do zgrywania płyt audio do plików WAV, MP3 lub
OGG, stworzony by nie trzeba było się martwić o to, iż jakikolwiek
błąd przy zgrywaniu umknie naszej uwadze.

%package -n python-%{module}-cursesmodule
Summary:	An improved Python curses module used by jack (a Python ripping program)
Summary(pl.UTF-8):   Ulepszona wersja modułu curses dla Pythona wykorzystywana przez program jack
Group:		Development/Languages/Python
%pyrequires_eq	python-libs

%description -n python-%{module}-cursesmodule
Improved Python curses module used by jack (a Python ripping program).

%description -n python-%{module}-cursesmodule -l pl.UTF-8
Ulepszona wersja modułu curses dla Pythona wykorzystywana przez jack -
program do zgrywania płyt Audio CD.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

#py_comp *.py
#py_ocomp *.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}
install -d $RPM_BUILD_ROOT%{_bindir}

python setup.py install \
        --root=$RPM_BUILD_ROOT --optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.py
install jack $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/[!g]*
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{_bindir}/jack

%files -n python-%{module}-cursesmodule
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/jack_cursesmodule.so
