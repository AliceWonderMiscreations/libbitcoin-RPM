Name:		libbitcoin4-node
Version:	4.0.0
%define gitdate 20170304
Release:	0.git.%{gitdate}%{?dist}.1
Summary:	Bitcoin full node based on libbitcoin-blockchain

Group:		LibBitcoin/Libraries
License:	AGPLv3
URL:		https://libbitcoin.org/
Source0:	11eed6ee56ced6bed556aff0422fc07876382860e878144774854e9aa3acd144-libbitcoin-node-master.zip

BuildRequires:	autoconf automake libtool
%if 0%{?rhel}
BuildRequires:  compat-boost-devel >= 1.57.0
%else
BuildRequires:  boost-devel >= 1.57.0
%endif
BuildRequires:	bash-completion >= 2.0.0
BuildRequires:	libbitcoin4-blockchain-devel
BuildRequires:	libbitcoin4-network-devel
%if "%{_prefix}" != "/usr"
BuildRequires:	libbitcoin-prefix-setup-devel
Requires:	libbitcoin-prefix-setup
%endif

%description
This package provides a full Bitcoin node based on the libbitcoin-blockchain
library.

%package devel
Summary:	Development package for %{name}
Group:		LibBitcoin/Development
Requires:	%{name} = %{version}-%{release}
Requires:	libbitcoin4-blockchain-devel
Requires:	libbitcoin4-network-devel

%description devel
This package contains the development header files and libraries needed to
compile software that links against %{name}.


%prep
%setup -q -n libbitcoin-node-master
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
rm -f %{buildroot}%{_libdir}/libbitcoin-node.la
rm -rf %{buildroot}%{_prefix}/share/doc/libbitcoin-node


%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS README.md
%license COPYING
%dir %{_sysconfdir}/libbitcoin
%config(noreplace) %{_sysconfdir}/libbitcoin/bn.cfg
%{_bindir}/bn
%{_libdir}/lib*.so.*
%{_sysconfdir}/bash_completion.d/bn

%files devel
%defattr(-,root,root,-)
%{_includedir}/bitcoin/node.hpp
%dir %{_includedir}/bitcoin/node
%{_includedir}/bitcoin/node/*.hpp
%dir %{_includedir}/bitcoin/node/protocols
%{_includedir}/bitcoin/node/protocols/*.hpp
%dir %{_includedir}/bitcoin/node/sessions
%{_includedir}/bitcoin/node/sessions/*.hpp
%dir %{_includedir}/bitcoin/node/utility
%{_includedir}/bitcoin/node/utility/*.hpp
%{_libdir}/libbitcoin-node.a
%{_libdir}/libbitcoin-node.so
%{_libdir}/pkgconfig/libbitcoin-node.pc


%changelog
* Sat Mar 04 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170304.1
- Put bash completions in /etc/bash_completion.d

* Sat Mar 04 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170304.0
- Initial spec file
