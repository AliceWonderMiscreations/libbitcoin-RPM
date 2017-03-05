Name:		libbitcoin4-server
Version:	4.0.0
%define gitdate 20170304
Release:	0.git.%{gitdate}%{?dist}.1
Summary:	Bitcoin Full Node and Query Server

Group:		LibBitcoin/Libraries
License:	AGPLv3
URL:		https://libbitcoin.org/
Source0:	9e21d3e9e6111c46b2c6520d2c3cec497645e4ed379d4cde225a620ce23be491-libbitcoin-server-master.zip

BuildRequires:	autoconf automake libtool
%if 0%{?rhel}
BuildRequires:  compat-boost-devel >= 1.57.0
%else
BuildRequires:  boost-devel >= 1.57.0
%endif
BuildRequires:  bash-completion >= 2.0.0
BuildRequires:	libbitcoin4-node-devel
BuildRequires:	libbitcoin4-protocol-devel
%if "%{_prefix}" != "/usr"
BuildRequires: libbitcoin-prefix-setup-devel
Requires:      libbitcoin-prefix-setup
%endif

%description
A full Bitcoin peer-to-peer node, Libbitcoin Server is also a high performance
blockchain query server. It is trivial to deploy, just run the single process
and allow it about two days to synchronize the Bitcoin blockchain.

Libbitcoin Server exposes a custom query TCP API built based on the ZeroMQ
networking stack. It supports server, and optionally client, identity
certificates and wire encryption via CurveZMQ and the Sodium cryptographic
library.

The API is backward compatible with its predecessor Obelisk and supports simple
and advanced scenarios, including stealth payment queries. The libbitcoin-client
library provides a calling API for building client applications. The server is
complimented by libbitcoin-explorer (BX), the Bitcoin command line tool and
successor to SX.

%package devel
Summary:	Development package for %{name}
Group:		LibBitcoin/Development
Requires:	%{name} = %{version}-%{release}
Requires:	libbitcoin4-node-devel
Requires:	libbitcoin4-protocol-devel

%description devel
This package contains the development header files and libraries needed to
compile software that links against %{name}.

%prep
%setup -q -n libbitcoin-server-master
./autogen.sh


%build
%if 0%{?btc_pkgconfig:1}%{!?btc_pkgconfig:0}
  PKG_CONFIG_PATH="%{btc_pkgconfig}"
  export PKG_CONFIG_PATH
%endif
%configure --with-bash-completiondir=%{_sysconfdir}/bash_completion.d %{?_with_boost} %{?_boost_libdir}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libbitcoin-server.la
rm -rf %{buildroot}%{_prefix}/share/doc/libbitcoin-server

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS README.md
%license COPYING
%dir %{_sysconfdir}/libbitcoin
%config(noreplace) %{_sysconfdir}/libbitcoin/bs.cfg
%{_bindir}/bs
%{_libdir}/lib*.so.*
%{_sysconfdir}/bash_completion.d/bs

%files devel
%defattr(-,root,root,-)
%{_includedir}/bitcoin/server.hpp
%dir %{_includedir}/bitcoin/server
%{_includedir}/bitcoin/server/*.hpp
%dir %{_includedir}/bitcoin/server/interface
%{_includedir}/bitcoin/server/interface/*.hpp
%dir %{_includedir}/bitcoin/server/messages
%{_includedir}/bitcoin/server/messages/*.hpp
%dir %{_includedir}/bitcoin/server/services
%{_includedir}/bitcoin/server/services/*.hpp
%dir %{_includedir}/bitcoin/server/utility
%{_includedir}/bitcoin/server/utility/*.hpp
%dir %{_includedir}/bitcoin/server/workers
%{_includedir}/bitcoin/server/workers/*.hpp
%{_libdir}/libbitcoin-server.a
%{_libdir}/libbitcoin-server.so
%{_libdir}/pkgconfig/libbitcoin-server.pc


%changelog
* Sat Mar 04 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170304.1
- Put bash completions in /etc/bash_completion.d

* Sat Mar 04 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170304.0
- Initial spec file
