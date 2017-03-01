Name:		libbitcoin-libsecp256k1
Version:	0.1
%define gitdate 20170226
Release:	0.git.%{gitdate}%{?dist}.0
Summary:	libbitcoin fork of libsecp256k1

Group:		LibBitcoin/Libraries
License:	MIT
URL:		https://github.com/libbitcoin/secp256k1
# from github 2017-02-26 09:54 Pacific
Source0:	aca1a501c0ab6e416a63010c039268b9bac52829a93e267a5ba23cbb883b31d3-secp256k1-master.zip
Provides:	libsecp256k1 = %{version}

BuildRequires: automake autoconf libtool

%description
Optimized C library for EC operations on curve secp256k1.

This library is a work in progress and is being used to research best practices.
Use at your own risk.

Features:
    secp256k1 ECDSA signing/verification and key generation.
    Adding/multiplying private/public keys.
    Serialization/parsing of private keys, public keys, signatures.
    Constant time, constant memory access signing and pubkey generation.
    Derandomized DSA (via RFC6979 or with a caller provided function.)
    Very efficient implementation.

%package devel
Summary:	Development files for %{name}
Group:		LibBitcoin/Development
Requires:	%{name} = %{version}-%{release}
Provides:	libsecp256k1-devel = %{version}

%description devel
This package provides the development header files and libraries needed to
build software that links against %{name}.


%prep
%setup -q -n secp256k1-master
./autogen.sh


%build
%configure --enable-module-recovery
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.md TODO
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/libsecp256k1.a
%{_libdir}/libsecp256k1.so
%{_libdir}/pkgconfig/libsecp256k1.pc


%changelog
* Mon Feb 27 2017 Alice Wonder <buildmaster@librelamp.com> - 0.1-0.git.20170226.0
- Run make check, correct version (to match pkgconfig)

* Sun Feb 26 2017 Alice Wonder <buildmaster@librelamp.com> - 0.0.1-0.git.20170226.1
- Change RPM groups to reflect LibBitcoin

* Sun Feb 26 2017 Alice Wonder <buildmaster@librelamp.com> - 0.0.1-0.git.20170226.0
- Initial build

