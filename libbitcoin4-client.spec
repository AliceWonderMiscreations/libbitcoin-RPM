Name:		libbitcoin4-client
Version:	4.0.0
%define gitdate 20170304
Release:	0.git.%{gitdate}%{?dist}.0
Summary:	Bitcoin Client Query Library

Group:		LibBitcoin/Libraries
License:	AGPLv3
URL:		https://libbitcoin.org/
Source0:	332844c90a0b8e084521cfcb214ef8518cfa6bc0ac339d19371ec067afae27ea-libbitcoin-client-master.zip

BuildRequires:	autoconf automake libtool
%if 0%{?rhel}
BuildRequires:  compat-boost-devel >= 1.57.0
%else
BuildRequires:  boost-devel >= 1.57.0
%endif
BuildRequires:	libbitcoin4-devel
BuildRequires:	libbitcoin4-protocol-devel
%if "%{_prefix}" != "/usr"
BuildRequires: libbitcoin-prefix-setup-devel
Requires:      libbitcoin-prefix-setup
%endif

%description
The libbitcoin client library

%package devel
Summary:	Development package for %{name}
Group:		LibBitcoin/Development
Requires:	%{name} = %{version}-%{release}
Requires:	libbitcoin4-devel
Requires:	libbitcoin4-protocol-devel

%description devel
This package contains the development header files and libraries needed to
compile software that links against %{name}.


%prep
%setup -q -n libbitcoin-client-master
./autogen.sh


%build
%if 0%{?btc_pkgconfig:1}%{!?btc_pkgconfig:0}
  PKG_CONFIG_PATH="%{btc_pkgconfig}"
  export PKG_CONFIG_PATH
%endif
%configure --without-examples %{?_with_boost} %{?_boost_libdir}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libbitcoin-client.la
rm -rf %{buildroot}%{_prefix}/share/doc/libbitcoin-client

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
%{_includedir}/bitcoin/client.hpp
%dir %{_includedir}/bitcoin/client
%{_includedir}/bitcoin/client/*.hpp
%{_libdir}/libbitcoin-client.a
%{_libdir}/libbitcoin-client.so
%{_libdir}/pkgconfig/libbitcoin-client.pc



%changelog
* Sat Mar 04 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170304.0
- Initial spec file
