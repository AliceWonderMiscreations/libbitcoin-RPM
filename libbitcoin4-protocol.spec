Name:		libbitcoin4-protocol
Version:	4.0.0
%define gitdate 20170305
Release:	0.git.%{gitdate}%{?dist}.0
Summary:	Bitcoin Blockchain Query Protocol

Group:		LibBitcoin/Libraries
License:	AGPLv3
URL:		https://libbitcoin.org/
Source0:	8ce264bbc6d7e43fbad227beda3afb826c759dd9c26c2a694447ad3994409a30-libbitcoin-protocol-master.zip

BuildRequires:	autoconf automake libtool
%if 0%{?rhel}
BuildRequires:	compat-boost-devel >= 1.57.0
BuildRequires:	compat-zeromq-devel >= 4.2.0
%else
BuildRequires:	boost-devel >= 1.57.0
BuildRequires:	zeromq-devel >= 4.2.0
%endif
BuildRequires:	libbitcoin4-devel
%if "%{_prefix}" != "/usr"
BuildRequires: libbitcoin-prefix-setup-devel
Requires:      libbitcoin-prefix-setup
%endif

%description
A library for querying the Bitcoin Blockchain via Libbitcoin.

%package devel
Summary:	Development package for %{name}
Group:		LibBitcoin/Development
Requires:	%{name} = %{version}-%{release}
Requires:	libbitcoin4-devel
%if 0%{?rhel}
Requires:	compat-zeromq-devel
%else
Requires:	zeromq-devel
%endif

%description devel
This package contains the development header files and libraries needed to
compile software that links against %{name}.


%prep
%setup -q -n libbitcoin-protocol-master
./autogen.sh


%build
%if 0%{?btc_pkgconfig:1}%{!?btc_pkgconfig:0}
  PKG_CONFIG_PATH="%{btc_pkgconfig}"
  export PKG_CONFIG_PATH
%endif
%configure %{?_with_boost} %{?_boost_libdir}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_prefix}/share/doc/libbitcoin-protocol

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS README.md
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/bitcoin/protocol.hpp
%dir %{_includedir}/bitcoin/protocol
%{_includedir}/bitcoin/protocol/*.h
%{_includedir}/bitcoin/protocol/*.hpp
%dir %{_includedir}/bitcoin/protocol/zmq
%{_includedir}/bitcoin/protocol/zmq/*.hpp
%{_libdir}/libbitcoin-protocol.a
%{_libdir}/libbitcoin-protocol.so
%{_libdir}/pkgconfig/libbitcoin-protocol.pc


%changelog
* Sun Mar 05 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170305.0
- Update git checkout

* Fri Mar 03 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.2
- Fix for defining an alternate %%_prefix at build time.
- Optional macro for defining --with-boost and --with-boost-libdir configure option

* Tue Feb 28 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.1
- Change name to libbitcoin4-protocol due to devel rather than stable nature.

* Tue Feb 28 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.0
- Initial RPM spec file
