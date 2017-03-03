Name:		libbitcoin4-blockchain
Version:	4.0.0
%define gitdate 20170228
Release:	0.git.%{gitdate}%{?dist}.1
Summary:	Bitcoin Blockchain Library

Group:		LibBitcoin/Libraries
License:	AGPLv3
URL:		https://libbitcoin.org/
Source0:	574f20ab8b16686452b2708142135e2e5c7216d02eec25d7cd997440734c2a20-libbitcoin-blockchain-master.zip

BuildRequires:	autoconf automake libtool
%if 0%{?rhel}
BuildRequires:	compat-boost-devel >= 1.57.0
%else
BuildRequires:	boost-devel >= 1.57.0
%endif
BuildRequires:	libbitcoin4-database-devel
BuildRequires:	libbitcoin4-consensus-devel


%description
The libbitcoin blockchain library.


%package devel
Summary:	Development package for %{name}
Group:		LibBitcoin/Development
Requires:	%{name} = %{version}-%{release}
Requires:	libbitcoin4-database-devel
Requires:	libbitcoin4-consensus-devel

%description devel
This package contains the development header files and libraries needed to
compile software that links against %{name}.

%prep
%setup -q -n libbitcoin-blockchain-master
./autogen.sh


%build
%configure --with-consensus %{?_with_boost}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libbitcoin-blockchain.la
rm -rf %{buildroot}%{_prefix}/share/doc/libbitcoin-blockchain

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
%{_includedir}/bitcoin/blockchain.hpp
%dir %{_includedir}/bitcoin/blockchain
%{_includedir}/bitcoin/blockchain/*.hpp
%dir %{_includedir}/bitcoin/blockchain/interface
%{_includedir}/bitcoin/blockchain/interface/*.hpp
%dir %{_includedir}/bitcoin/blockchain/pools
%{_includedir}/bitcoin/blockchain/pools/*.hpp
%dir %{_includedir}/bitcoin/blockchain/populate
%{_includedir}/bitcoin/blockchain/populate/*.hpp
%dir %{_includedir}/bitcoin/blockchain/validate
%{_includedir}/bitcoin/blockchain/validate/*.hpp
%{_libdir}/libbitcoin-blockchain.a
%{_libdir}/libbitcoin-blockchain.so
%{_libdir}/pkgconfig/libbitcoin-blockchain.pc


%changelog
* Fri Mar 03 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.1
- Fix for defining an alternate %%_prefix at build time.
- Optional macro for defining --with-boost configure option

* Tue Feb 28 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.0
- Initial RPM spec file.
