Summary:	GNU database library for C
Summary(de):	GNU-Datenbank-Library f�r C
Summary(fr):	La librairie GNU de bases de donn�es pout le langage C
Summary(pl):	Biblioteka GNU bazy danych dla j�zyka C
Summary(ru):	���������� ���� ������ GNU ��� C
Summary(uk):	��̦����� ���� ����� GNU ��� C
Name:		gdbm
Version:	1.8.0
Release:	16
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/pub/gnu/gdbm/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-jbj.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgdbm2

%description
Gdbm is a GNU database indexing library, including routines which use
extensible hashing. Gdbm works in a similar way to standard UNIX dbm
routines. Gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

%description -l de
Dies ist eine Datenbank-Index-Library f�r Programmierer, die
C-Anwendungen schreiben und eine einfache und leistungsf�hige
Datenbank ben�tigen oder diese in C-Anwendungen einsetzen m�chten.

%description -l fr
Une librairie d'indexation de bases de donn�es. Elle est utile pour
ceux qui d�sirent �crivent des applications en C et ont besion
d'acc�der � une base de donn�es simple et efficace ou de construire
une application en C qui l'utilise.

%description -l pl
W pakiecie znajduje si� biblioteka indeksowania bazy danych.
Biblioteka ta jest szczeg�lnie u�yteczna dla ludzi, kt�rzy pisz�
oprogramowanie w C i potrzebuj� prostej i szybkiej bazy danych, lub
dla tych kt�rzy pisz� programy w C z wykorzystaniem tej biblioteki.

%description -l tr
gdbm bir veri taban� dizinleme kitapl���d�r. C uygulamalar� yaz�p
basit ve etkin bir �ekilde veri taban�na ula�mak isteyenler i�in
yararl� olacakt�r.

%description -l ru
��� ���������� ��� ������ � ��������������� ����� ������. ������� ���
���, ��� ������������� ��������� �� C � ���� ����� ������ � ������� �
����������� ���� ������ ���� ��������� �������� ���������, ������� ��
����������.

%description -l uk
�� ¦�̦����� ��� ������ � ������������ ����� �����. ������� ��� ���,
��� �������Ѥ �������� �� C � ���� ���Ҧ��� ������ �� �����ϧ ��
��������ϧ ���� ����� ��� ���Ҧ��� �������� ��������, �� ��
����������դ.

%package devel
Summary:	development libraries and header files for gdbm
Summary(de):	Entwicklungs-Libraries und Header-Dateien f�r gdbm
Summary(fr):	Biblioth�ques de d�veloppement et en-t�tes pour gdbm
Summary(pl):	Biblioteki i pliki nag��wkowe dla gdbm
Summary(tr):	gdbm i�in ba�l�k dosyalar� ve geli�tirme kitapl�klar�
Summary(ru):	���������� � ������ gdbm ��� �������������
Summary(uk):	��̦����� �� ������ gdbm ��� ������ͦ�Ԧ�
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libgdbm2-devel

%description devel
These are the development libraries and header files for gdbm, the GNU
database system. These are required if you plan to do development
using the gdbm database.

%description devel -l de
Dies sind die Entwicklungs-Libraries und Header-Dateien f�r gdbm, das
GNU-Datenbanksystem. Sie sind darauf angewiesen, wenn Sie vorhaben,
die gdbm-Datenbank f�r Entwicklungsarbeiten zu benutzen.

%description devel -l fr
Ce sont les librairies de d�veloppement et les fichiers d'en-t�te pour
gdbm, le syst�me de base de donn�es GNU. Ceci est n�cessaire si vous
d�sirez d�velopper en utilisant la base de donn�es gdbm.

%description devel -l pl
W pakiecie tym znajduj� si� pliki nag��wkowe i biblioteki dla systemu
bazy danych GNU.

%description devel -l tr
GNU veri taban� sistemi gdbm ile program geli�tirmek i�in gereken
ba�l�k dosyalar� ve kitapl�klar.

%description devel -l ru
��� ���������� ��� ������������� � ������ gdbm, ���� ������ GNU. ���
�����, ���� �� ����������� ������������� ��������� � ��������������
gdbm.

%description devel -l uk
�� ¦�̦����� ��� ������ͦ�Ԧ� �� ������ gdbm, ���� ����� GNU. ����
���Ҧ�Φ, ���� �� ���������� ���������� �������� � ������������� gdbm.

%package static
Summary:	Static gdbm library
Summary(pl):	Biblioteki statyczne gdbm
Summary(uk):	�������� ¦�̦����� gdbm
Summary(ru):	����������� ���������� gdbm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gdbm library.

%description static -l pl
Biblioteka statyczna gdbm.

%description static -l ru
��� ����������� ���������� gdbm, ���� ������ GNU.

%description static -l uk
�� �������� ¦�̦����� gdbm, ���� ����� GNU.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure

%{__make} CFLAGS="%{rpmcflags}"

makeinfo gdbm.texinfo

cat .libs/libgdbm.lai|sed -e 's/\/usr\/local\/lib/\/usr\/lib/'>libgdbm.lai.tmp
mv libgdbm.lai.tmp .libs/libgdbm.lai

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}} \
	   $RPM_BUILD_ROOT{%{_mandir}/man3,%{_infodir}}

%{__make} install install-compat \
	prefix=%{_prefix} \
	exec_prefix=%{_exec_prefix} \
	binprefix=%{_exec_prefix} \
	manprefix=%{_prefix} \
	libdir=%{_libdir} \
	includedir=%{_includedir} \
	infodir=%{_infodir} \
	man3dir=%{_mandir}/man3 \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_mandir}/man3/*
%{_includedir}/*
%{_infodir}/gdbm*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
