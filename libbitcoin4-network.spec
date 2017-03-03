Name:		libbitcoin4-network
Version:	4.0.0
%define gitdate 20170303
Release:	0.git.%{gitdate}%{?dist}.0
Summary:	Bitcoin P2P Network Library

Group:		LibBitcoin/Libraries
License:	AGPLv3
URL:		https://libbitcoin.org/
Source0:	0a3907a438fdaa87e16ad7d8c935156d814600d95b7c0ace3535b2b1156034cc-libbitcoin-network-master.zip

BuildRequires:	autoconf automake libtool
BuildRequires:	libbitcoin4-devel
%if 0%{?rhel}
BuildRequires:	compat-boost-devel >= 1.57.0
%else
BuildRequires:	boost-devel >= 1.57.0
%endif

%description
Libbitcoin Network is a partial implementation of the Bitcoin P2P network
protocol. Excluded are all protocols that require access to a blockchain. The
libbitcoin-node library extends the P2P networking capability and incorporates
libbitcoin-blockchain in order to implement a full node. The libbitcoin-explorer
library uses the P2P networking capability to post transactions to the P2P
network.

%package devel
Summary:	Development package for %{name}
Group:		LibBitcoin/Development
Requires:	%{name} = %{version}-%{release}
Requires:	libbitcoin4-devel

%description devel
This package contains the development header files and libraries needed to
compile software that links against %{name}.


%prep
%setup -q -n libbitcoin-network-master
./autogen.sh


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libbitcoin-network.la
rm -rf %{buildroot}%{_datadir}/doc/libbitcoin-network

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
%{_includedir}/bitcoin/network.hpp
%dir %{_includedir}/bitcoin/network
%{_includedir}/bitcoin/network/*.hpp
%dir %{_includedir}/bitcoin/network/protocols
%{_includedir}/bitcoin/network/protocols/*.hpp
%dir %{_includedir}/bitcoin/network/sessions
%{_includedir}/bitcoin/network/sessions/*.hpp
%{_libdir}/libbitcoin-network.a
%{_libdir}/libbitcoin-network.so
%{_libdir}/pkgconfig/libbitcoin-network.pc



%changelog
* Fri Mar 03 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170303.0
- Initial RPM spec file.
