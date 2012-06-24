Summary:     GNU database library for C
Summary(de): GNU-Datenbank-Library f�r C
Summary(fr): La librairie GNU de bases de donn�es pout le langage C.
Name:        gdbm
Version:     1.7.3
Release:     19
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch:       gdbm-1.7.3-shlib.patch
Copyright:   GPL
Group:       Libraries
Buildroot:   /tmp/%{name}-%{version}-root

%description
This is a database indexing library.  It is useful for those who need 
to write C applications and need access to a simple and efficient
database or build C applications which use it.

%package devel
Summary:     development libraries and header files for gdbm
Summary(de): Entwicklungs-Libraries und Header-Dateien f�r gdbm 
Summary(fr): Biblioth�ques de d�veloppement et en-t�tes pour gdbm
Summary(tr): gdbm i�in ba�l�k dosyalar� ve geli�tirme kitapl�klar�
Group:       Development/Libraries
Requires:    %{name} = %{version}
Prereq:      /sbin/install-info

%description devel
These are the development libraries and header files for gdbm, the
GNU database system.  These are required if you plan to do 
development using the gdbm database.

%description -l de devel
Dies sind die Entwicklungs-Libraries und Header-Dateien f�r gdbm, das
GNU-Datenbanksystem. Sie sind darauf angewiesen, wenn Sie vorhaben,
die gdbm-Datenbank f�r Entwicklungsarbeiten zu benutzen.

%description -l de
Dies ist eine Datenbank-Index-Library f�r Programmierer, die 
C-Anwendungen schreiben und eine einfache und leistungsf�hige
Datenbank ben�tigen oder diese in C-Anwendungen einsetzen m�chten.

%description -l fr devel
Ce sont les librairies de d�veloppement et les fichiers d'en-t�te pour gdbm,
le syst�me de base de donn�es GNU. Ceci est n�cessaire si vous d�sirez 
d�velopper en utilisant la base de donn�es gdbm.

%description -l fr
Une librairie d'indexation de bases de donn�es. Elle est utile pour ceux
qui d�sirent �crivent des applications en C et ont besion d'acc�der �
une base de donn�es simple et efficace ou de construire une application
en C qui l'utilise.

%description -l tr devel
GNU veri taban� sistemi gdbm ile program geli�tirmek i�in gereken ba�l�k
dosyalar� ve kitapl�klar.

%description -l tr
gdbm bir veri taban� dizinleme kitapl���d�r. C uygulamalar� yaz�p basit ve
etkin bir �ekilde veri taban�na ula�mak isteyenler i�in yararl� olacakt�r.

%package static
Summary:     static gdbm library
Group:       Development/Libraries
Requires:    %{name}-devel = %{version}
Prereq:      /sbin/install-info

%description static
Static gdbm library.

%prep
%setup -q
%patch -p1 -b .shared
mkdir shared

%build
./configure --prefix=/usr
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" shared

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{lib,include,info,man/man3}
make install prefix=$RPM_BUILD_ROOT/usr
gzip -fn9 $RPM_BUILD_ROOT/usr/info/gdbm*info*
ln -sf libgdbm.so.2.0.0 $RPM_BUILD_ROOT/usr/lib/libgdbm.so

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

%post -p /sbin/ldconfig

%post devel
/sbin/install-info /usr/info/gdbm.info.gz /usr/info/dir --entry \
"* gdbm: (gdbm).                                 The GNU Database."

%postun -p /sbin/ldconfig

%preun devel
/sbin/install-info --delete /usr/info/gdbm.info.gz /usr/info/dir --entry \
"* gdbm: (gdbm).                                 The GNU Database."

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/lib/lib*.so.*.*

%files devel
%defattr(644, root, root, 755)
/usr/lib/lib*.so
%attr(644, root,  man) /usr/man/man3/*
/usr/include/*
/usr/info/gdbm*

%files static
%attr(644, root, root) /usr/lib/lib*.a

%changelog
* Sun Nov 22 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7.3-19]
- removed "Prereq: /sbin/install-info" from static,
- fixed --entry text on {un}registering info page for ed in %post
  %preun in devel.

* Sun Aug 30 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7.3-18]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added stripping shared libraries,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- gdbm-devel moved to Development/Libraries

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- buildroot and built for Manhattan

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc
