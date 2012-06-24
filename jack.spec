%define         module jack

Summary:	Module for accessing CDDB and FreeDB
Summary(pl):	Modu� do ��czenia z bazami CDDB i FreeDB
Name:		jack
Version:	3.0.0
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.home.unix-ag.org/arne/jack/%{module}-%{version}.tar.gz
# Source0-md5:	195c15a053c27f6a05fe0eda54bf9f35
URL:		http://www.home.unix-ag.org/arne/jack/
BuildRequires:	ncurses-devel
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	ncurses <= 5.3
Requires:	python-CDDB
Requires:	python-ID3
Requires:	python-jack-cursesmodule = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jack is a python CDDA ripping program. It has been developed with one
main goal: making MP3s without having to worry.

%description -l pl
Jack jest programem do zgrywania p�yt audio do plik�w WAV, MP3 lub
OGG, stworzony by nie trzeba by�o si� martwi� o to, i� jakikolwiek
b��d przy zgrywaniu umknie naszej uwadze.

%package -n python-%{module}-cursesmodule
Summary:	An improved Python curses module used by jack (a Python ripping program)
Summary(pl):	Ulepszona wersja modu�u curses dla Pythona wykorzystywana przez program jack
Group:		Development/Languages/Python

%description -n python-%{module}-cursesmodule
Improved Python curses module used by jack (a Python ripping program).

%description -n python-%{module}-cursesmodule -l pl
Ulepszona wersja modu�u curses dla Pythona wykorzystywana przez jack -
program do zgrywania p�yt Audio CD.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CLFAGS
python setup-cursesmodule.py build

python -O *.py

python - <<END
import py_compile, os, fnmatch

for f in os.listdir("."):
  if fnmatch.fnmatch(f, "*.py"):
    print "Byte compiling %s..." % f
    py_compile.compile(f)
END

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
install -d $RPM_BUILD_ROOT%{_bindir}

python setup-cursesmodule.py install \
        --root=$RPM_BUILD_ROOT --optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.py
install jack_*py[co] $RPM_BUILD_ROOT%{py_sitescriptdir}
install jack $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/[!g]*
%{py_sitescriptdir}/*.py[co]
%attr(755,root,root) %{_bindir}/jack

%files -n python-%{module}-cursesmodule
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/jack_cursesmodule.so
