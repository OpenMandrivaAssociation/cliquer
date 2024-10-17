Name:           cliquer
Version:        1.21
Release:        1%{?dist}
Summary:        Find cliques in arbitrary weighted graphs
License:        GPLv2+
URL:            https://users.tkk.fi/pat/cliquer.html
Source0:        http://users.tkk.fi/~pat/%{name}/%{name}-%{version}.tar.gz
Source1:        http://users.tkk.fi/~pat/%{name}/%{name}_fm.pdf
Source2:        http://users.tkk.fi/~pat/%{name}/%{name}.pdf
Source3:        http://users.tkk.fi/~pat/%{name}/%{name}_bm.pdf
Source4:        http://users.tkk.fi/~pat/%{name}/basic.c
Source5:        http://users.tkk.fi/~pat/%{name}/hamming.c
Source6:        http://users.tkk.fi/~pat/%{name}/poly.c
Source7:        http://users.tkk.fi/~pat/%{name}/tetromino.h
# Man page formatting by Jerry James, text from the sources
Source8:        %{name}.1
# Sagemath patches and extra files. History can be found in related tracs at:
#       http://trac.sagemath.org/sage_trac/ticket/6355
#       http://trac.sagemath.org/sage_trac/ticket/5793
# A private email was also sent to cliquer author asking for any comments
# on Fedora cliquer review request and sagemath patches.
Source9:        cl.h
Source10:	%{name}.rpmlintrc
Patch0:         %{name}-sagemath.patch

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
The main cliquer package contains a command-line interface to the
cliquer library.  Note that the upstream binary name is "cl", which is
too generic for Fedora.  Therefore, the binary is named "cliquer".

%package libs
Summary:        Library to find cliques in arbitrary weighted graphs

%description libs
Cliquer is a set of C routines for finding cliques in an arbitrary
weighted graph.  It uses an exact branch-and-bound algorithm developed
by Patric Östergård.  It is designed with the aim of being efficient
while still being flexible and easy to use.

%package devel
Summary:        Development files for cliquer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for cliquer.

%prep
%setup -q
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} .
%patch0 -p1

mkdir example
sed 's|"cliquer.h"|<cliquer/cliquer.h>|' %{SOURCE4} > example/basic.c
sed 's|"cliquer.h"|<cliquer/cliquer.h>|' %{SOURCE5} > example/hamming.c
sed 's|"cliquer.h"|<cliquer/cliquer.h>|' %{SOURCE6} > example/poly.c
cp -p %{SOURCE7} example

sed -i \
    's/59 Temple Place, Suite 330, Boston, MA  02111-1307/51 Franklin Street, Suite 500, Boston, MA  02110-1335/' \
    LICENSE

%build
# The distributed Makefile just builds a binary named "cl".  However, the
# examples show that the internal code is clearly meant to be used as a
# library.  So we build a library by hand.
gcc ${RPM_OPT_FLAGS} -fPIC -c cl.c
gcc ${RPM_OPT_FLAGS} -fPIC -c cliquer.c
gcc ${RPM_OPT_FLAGS} -fPIC -c graph.c
gcc ${RPM_OPT_FLAGS} -fPIC -c reorder.c
gcc ${RPM_OPT_FLAGS} -fPIC -shared -o libcliquer.so.%{version} \
  -Wl,-soname=libcliquer.so.1 cl.o cliquer.o graph.o reorder.o
ln -s libcliquer.so.%{version} libcliquer.so.1
ln -s libcliquer.so.1 libcliquer.so

# Now build the binary
gcc ${RPM_OPT_FLAGS} -DENABLE_LONG_OPTIONS -DMAIN -c cl.c
gcc ${RPM_OPT_FLAGS} -o cliquer cl.o -L. -lcliquer

%install
# Install the library
mkdir -p $RPM_BUILD_ROOT%{_libdir}
cp -pP libcliquer.so* $RPM_BUILD_ROOT%{_libdir}
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libcliquer.so.%{version}

# Install the binary
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 -p cliquer $RPM_BUILD_ROOT%{_bindir}/cliquer

# Install the header file
mkdir -p $RPM_BUILD_ROOT%{_includedir}/cliquer
cp -p %{SOURCE9} cliquer.h cliquerconf.h graph.h misc.h reorder.h set.h $RPM_BUILD_ROOT%{_includedir}/cliquer

# Install the man page
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{SOURCE8} $RPM_BUILD_ROOT%{_mandir}/man1

%check
LD_LIBRARY_PATH=. make test CFLAGS="${RPM_OPT_FLAGS}"

%files
%doc cliquer*.pdf
%{_bindir}/%{name}
%{_mandir}/man1/*

%files libs
%doc ChangeLog LICENSE README example
%{_libdir}/libcliquer.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libcliquer.so
