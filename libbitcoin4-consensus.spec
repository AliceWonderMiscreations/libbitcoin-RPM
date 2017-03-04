Name:		libbitcoin4-consensus
Version:	4.0.0
%define gitdate 20170228
Release:	0.git.%{gitdate}%{?dist}.2
Summary:	Bitcoin consensus library

Group:		LibBitcoin/Libraries
License:	AGPLv3
URL:		https://libbitcoin.org/
Source0:	fda2a060fb5d71a2dd8e62af846f104bbaecec90cb5bcb585eb45f2aa22abe00-libbitcoin-consensus-master.zip

BuildRequires:	autoconf automake libtool
BuildRequires:	libsecp256k1-devel >= 0.0.1
BuildRequires:	java-devel
%if 0%{?rhel}
BuildRequires:	compat-boost-devel >= 1.57.0
BuildRequires:	python-devel >= 2.7
%else
#Fedora and Python 3
BuildRequires:	boost-devel >= 1.57.0
BuildRequires:	python3-devel
%endif
%if "%{_prefix}" != "/usr"
BuildRequires: libbitcoin-prefix-setup-devel
Requires:      libbitcoin-prefix-setup
%endif


%description
This library provides libbitcoin consensus checks with the Satoshi client.


%package devel
Summary:	Development files for %{name}
Group:		LibBitcoin/Development
Requires:	%{name} = %{version}-%{release}
Requires:	libsecp256k1-devel

%description devel
This package contains the header files and libraries needed to compile software
that links against the %{name} libraries.

%package java
Summary:	Java JAR file for %{name}
Group:		LibBitcoin/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	java-headless

%description java
This package contains the Java JAR file for %{name}.

%package java-devel
Summary:	Java Development files for %{name}
Group:		LibBitcoin/Development
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-java = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description java-devel
This package contains the development files needed to create applications
that use the Java JAR file.

%if 0%{?rhel}
%package python
Summary:	Python bindings for %{name}
%else
%package python3
Summary:        Python3 bindings for %{name}
%endif
Group:		LibBitcoin/Libraries
Requires:	%{name} = %{version}-%{release}

%if 0%{?rhel}
%description python
This package provides the python2 bindings for %{name}.
%else
%description python3
This package provides the python3 bindings for %{name}.
%endif

%prep
%setup -q -n libbitcoin-consensus-master
./autogen.sh


%build
%if 0%{?_btc_pkgconfig:1}%{!?_btc_pkgconfig:0}
  PKG_CONFIG_PATH="%{_btc_pkgconfig}"
  export PKG_CONFIG_PATH
%endif
%configure --with-java --with-python %{?_with_boost} %{?_boost_libdir}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_prefix}/share/doc/libbitcoin-consensus

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.md
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/bitcoin/consensus.hpp
%dir %{_includedir}/bitcoin/consensus
%{_includedir}/bitcoin/consensus/*.hpp
%{_libdir}/libbitcoin-consensus.a
%{_libdir}/libbitcoin-consensus.so
%{_libdir}/pkgconfig/libbitcoin-consensus.pc

%files java
%defattr(-,root,root,-)
%{_datadir}/java/*.jar

%files java-devel
%defattr(-,root,root,-)
%{_libdir}/libbitcoin-consensus-jni.a
%{_libdir}/libbitcoin-consensus-jni.so

%if 0%{?rhel}
%files python
%defattr(-,root,root,-)
# need a better way
%if "%{_prefix}" == "/usr"
%{python2_sitelib}/*
%{python2_sitearch}/*
%else
%{_prefix}/lib/python2.7/site-packages/*
%{_libdir}/python2.7/*
%endif
%else
%files python3
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{python3_sitearch}/*
%endif


%changelog
* Fri Mar 03 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.2
- Fix for defining an alternate %%_prefix at build time.
- Optional macro for defining --with-boost and --with-boost-libdir configure option
- FIXME - better handling of the python file locations.

* Thu Mar 02 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.1
- In CentOS build against compat-boost

* Tue Feb 28 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.0
- Build 4.0.0 from git master, add support for Python3 if using Fedora (untested)
- Rename to libbitcoin4-consensus

* Mon Feb 27 2017 Alice Wonder <buildmaster@librelamp.com> - 3.0.0-1.1
- Add Requires: java-headless to Java package

* Sun Feb 26 2017 Alice Wonder <buildmaster@librelamp.com> - 3.0.0-1
- Initial packaging
