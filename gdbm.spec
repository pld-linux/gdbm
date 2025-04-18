#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	GNU database library for C
Summary(de.UTF-8):	GNU-Datenbank-Library für C
Summary(fr.UTF-8):	La librairie GNU de bases de données pout le langage C
Summary(pl.UTF-8):	Biblioteka GNU bazy danych dla języka C
Summary(ru.UTF-8):	Библиотека базы данных GNU для C
Summary(uk.UTF-8):	Бібліотека бази даних GNU для C
Name:		gdbm
Version:	1.25
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	https://ftp.gnu.org/gnu/gdbm/%{name}-%{version}.tar.gz
# Source0-md5:	46266720c7980b75f29e3554aeaeb7a8
Patch0:		%{name}-info.patch
Patch1:		%{name}-link-compat.patch
URL:		http://www.gnu.org/software/gdbm/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.19
BuildRequires:	libtool >= 2:2
BuildRequires:	readline-devel
BuildRequires:	texinfo
Obsoletes:	libgdbm2 < 1.8.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gdbm is a GNU database indexing library, including routines which use
extensible hashing. gdbm works in a similar way to standard UNIX dbm
routines. gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

%description -l de.UTF-8
Dies ist eine Datenbank-Index-Library für Programmierer, die
C-Anwendungen schreiben und eine einfache und leistungsfähige
Datenbank benötigen oder diese in C-Anwendungen einsetzen möchten.

%description -l fr.UTF-8
Une librairie d'indexation de bases de données. Elle est utile pour
ceux qui désirent écrivent des applications en C et ont besion
d'accéder à une base de données simple et efficace ou de construire
une application en C qui l'utilise.

%description -l pl.UTF-8
W pakiecie znajduje się biblioteka indeksowania bazy danych.
Biblioteka ta jest szczególnie użyteczna dla ludzi, którzy piszą
oprogramowanie w C i potrzebują prostej i szybkiej bazy danych, lub
dla tych którzy piszą programy w C z wykorzystaniem tej biblioteki.

%description -l tr.UTF-8
gdbm bir veri tabanı dizinleme kitaplığıdır. C uygulamaları yazıp
basit ve etkin bir şekilde veri tabanına ulaşmak isteyenler için
yararlı olacaktır.

%description -l ru.UTF-8
Это библиотека для работы с индексированной базой данных. Полезна для
тех, кто разрабатывает программы на C и кому нужен доступ к простой и
эффективной базе данных либо требуется написать программу, которая ее
использует.

%description -l uk.UTF-8
Це бібліотека для роботи з індексованою базою даних. Корисна для тих,
хто розробляє програми на C і кому потрібен доступ до простої та
ефективної бази даних або потрібно написати програму, що її
використовує.

%package devel
Summary:	development libraries and header files for gdbm
Summary(de.UTF-8):	Entwicklungs-Libraries und Header-Dateien für gdbm
Summary(fr.UTF-8):	Bibliothèques de développement et en-têtes pour gdbm
Summary(pl.UTF-8):	Biblioteki i pliki nagłówkowe dla gdbm
Summary(ru.UTF-8):	Библиотека и хедеры gdbm для разработчиков
Summary(tr.UTF-8):	gdbm için başlık dosyaları ve geliştirme kitaplıkları
Summary(uk.UTF-8):	Бібліотека та хедери gdbm для програмістів
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgdbm2-devel < 1.8.1

%description devel
These are the development libraries and header files for gdbm, the GNU
database system. These are required if you plan to do development
using the gdbm database.

%description devel -l de.UTF-8
Dies sind die Entwicklungs-Libraries und Header-Dateien für gdbm, das
GNU-Datenbanksystem. Sie sind darauf angewiesen, wenn Sie vorhaben,
die gdbm-Datenbank für Entwicklungsarbeiten zu benutzen.

%description devel -l fr.UTF-8
Ce sont les librairies de développement et les fichiers d'en-tête pour
gdbm, le système de base de données GNU. Ceci est nécessaire si vous
désirez développer en utilisant la base de données gdbm.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe i biblioteki dla systemu
bazy danych GNU.

%description devel -l tr.UTF-8
GNU veri tabanı sistemi gdbm ile program geliştirmek için gereken
başlık dosyaları ve kitaplıklar.

%description devel -l ru.UTF-8
Это библиотека для разработчиков и хедеры gdbm, базы данных GNU. Они
нужны, если вы собираетесь разрабатывать программы с использованием
gdbm.

%description devel -l uk.UTF-8
Це бібліотека для програмістів та хедери gdbm, бази даних GNU. Вони
потрібні, якщо ви збираєтесь розробляти програми з використанням gdbm.

%package static
Summary:	Static gdbm library
Summary(pl.UTF-8):	Biblioteki statyczne gdbm
Summary(ru.UTF-8):	Статическая библиотека gdbm
Summary(uk.UTF-8):	Статична бібліотека gdbm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gdbm library.

%description static -l pl.UTF-8
Biblioteka statyczna gdbm.

%description static -l ru.UTF-8
Это статическая библиотека gdbm, базы данных GNU.

%description static -l uk.UTF-8
Це статична бібліотека gdbm, бази даних GNU.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-libgdbm-compat \
	--disable-silent-rules

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS NOTE-WARNING README
%attr(755,root,root) %{_bindir}/gdbm_dump
%attr(755,root,root) %{_bindir}/gdbm_load
%attr(755,root,root) %{_bindir}/gdbmtool
%attr(755,root,root) %{_libdir}/libgdbm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdbm.so.6
%attr(755,root,root) %{_libdir}/libgdbm_compat.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdbm_compat.so.4
%{_mandir}/man1/gdbm_dump.1*
%{_mandir}/man1/gdbm_load.1*
%{_mandir}/man1/gdbmtool.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdbm.so
%attr(755,root,root) %{_libdir}/libgdbm_compat.so
%{_libdir}/libgdbm.la
%{_libdir}/libgdbm_compat.la
%{_includedir}/dbm.h
%{_includedir}/gdbm.h
%{_includedir}/ndbm.h
%{_mandir}/man3/gdbm.3*
%{_infodir}/gdbm.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdbm.a
%{_libdir}/libgdbm_compat.a
