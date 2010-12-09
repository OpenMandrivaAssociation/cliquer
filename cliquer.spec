Name:		cliquer
Version:	1.2
Release:	%mkrel 3
Group:		Sciences/Mathematics
License:	GPL
Summary:	Routines for finding cliques in an arbitrary weighted graph
Source0:	http://users.tkk.fi/~pat/cliquer/cliquer-1.2.tar.gz
# Slightly modified sagemath 4.1.1 patches to generate a shared library
Source1:	SConstruct
Source2:	cl.h
URL:		http://users.tkk.fi/pat/cliquer.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	scons

# Unlisted patches to upstream directly applied to spkg...
Patch0:		cliquer-1.2-sagemath.patch

%description
Cliquer is a set of C routines for finding cliques in an arbitrary weighted
graph. It uses an exact branch-and-bound algorithm recently developed by
Patric Östergård. It is designed with the aim of being efficient while still
being flexible and easy to use.

%package devel
Group:		Development/C
Summary:	Routines for finding cliques in an arbitrary weighted graph
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description devel
Cliquer is a set of C routines for finding cliques in an arbitrary weighted
graph. It uses an exact branch-and-bound algorithm recently developed by
Patric Östergård. It is designed with the aim of being efficient while still
being flexible and easy to use.

%prep
%setup -q

%patch0 -p1

%build
# generated shared library
cp %{SOURCE1} `pwd`
%scons

# generated standalone program
%make CFLAGS='%{optflags}'

%install
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_bindir} %{buildroot}%{_includedir}/%{name}
cp -f libcliquer.so %{buildroot}%{_libdir}
cp -f %{SOURCE2} *.h %{buildroot}%{_includedir}/%{name}

cp -f cl %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/cl

%files devel
%defattr(-,root,root)
%{_libdir}/libcliquer.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%doc README
