Name:		libbitcoin4
Version:	4.0.0
%define gitdate 20170227
Release:	0.git.%{gitdate}%{?dist}.1
Summary:	Bitcoin Cross-Platform C++ Development Toolkit

Group:		LibBitcoin/Libraries
License:	AGPLv3
URL:		https://libbitcoin.org/
Source0:	c854b0ed5609821a1f490116fac046a648fbb7f50738ead77eb0856fc8f00f87-libbitcoin-master.zip

BuildRequires:	autoconf automake libtool
BuildRequires:	boost-devel >= 1.57.0
BuildRequires:	libsecp256k1-devel >= 0.0.1
%if 0%{?rhel}
BuildRequires:	compat-libpng-devel >= 2:1.6.27
BuildRequires:	compat-qrencode-devel >= 3.4.4
BuildRequires:	compat-libicu-devel >= 51.2
%else
BuildRequires:	libpng-devel >= 2:1.6.27
BuildRequires:	qrencode-devel >= 3.4.4
BuildRequires:	libicu-devel >= 51.2
%endif

%description
The libbitcoin toolkit is a set of cross platform C++ libraries for building
bitcoin applications. The toolkit consists of several libraries, most of which
depend on the foundational libbitcoin library.

%package devel
Summary:	Development package for %{name}
Group:		LibBitcoin/Development
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development header files and libraries needed to
compile software that links against %{name}.


%prep
%setup -q -n libbitcoin-master
./autogen.sh


%build
%configure --without-examples --with-icu --with-png --with-qrencode --with-boost
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libbitcoin.la
rm -rf %{buildroot}%{_datadir}/doc/libbitcoin

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
%dir %{_includedir}/bitcoin
%{_includedir}/bitcoin/bitcoin.hpp
%dir %{_includedir}/bitcoin/bitcoin
%{_includedir}/bitcoin/bitcoin/*.h
%{_includedir}/bitcoin/bitcoin/*.hpp
%dir %{_includedir}/bitcoin/bitcoin/chain
%{_includedir}/bitcoin/bitcoin/chain/*.hpp
%dir %{_includedir}/bitcoin/bitcoin/config
%{_includedir}/bitcoin/bitcoin/config/*.hpp
%dir %{_includedir}/bitcoin/bitcoin/formats
%{_includedir}/bitcoin/bitcoin/formats/*.hpp
%dir %{_includedir}/bitcoin/bitcoin/impl
%dir %{_includedir}/bitcoin/bitcoin/impl/formats
%{_includedir}/bitcoin/bitcoin/impl/formats/*.ipp
%dir %{_includedir}/bitcoin/bitcoin/impl/log
%dir %{_includedir}/bitcoin/bitcoin/impl/log/features
%{_includedir}/bitcoin/bitcoin/impl/log/features/*.ipp
%dir %{_includedir}/bitcoin/bitcoin/impl/machine
%{_includedir}/bitcoin/bitcoin/impl/machine/*.ipp
%dir %{_includedir}/bitcoin/bitcoin/impl/math
%{_includedir}/bitcoin/bitcoin/impl/math/*.ipp
%dir %{_includedir}/bitcoin/bitcoin/impl/utility
%{_includedir}/bitcoin/bitcoin/impl/utility/*.ipp
%dir %{_includedir}/bitcoin/bitcoin/log
%{_includedir}/bitcoin/bitcoin/log/*.hpp
%dir %{_includedir}/bitcoin/bitcoin/log/features
%{_includedir}/bitcoin/bitcoin/log/features/*.hpp
%dir %{_includedir}/bitcoin/bitcoin/machine
%{_includedir}/bitcoin/bitcoin/machine/*.hpp
%dir %{_includedir}/bitcoin/bitcoin/math
%{_includedir}/bitcoin/bitcoin/math/*.hpp
%dir %{_includedir}/bitcoin/bitcoin/message
%{_includedir}/bitcoin/bitcoin/message/*.hpp
%dir %{_includedir}/bitcoin/bitcoin/unicode
%{_includedir}/bitcoin/bitcoin/unicode/*.hpp
%dir %{_includedir}/bitcoin/bitcoin/utility
%{_includedir}/bitcoin/bitcoin/utility/*.hpp
%dir %{_includedir}/bitcoin/bitcoin/wallet
%{_includedir}/bitcoin/bitcoin/wallet/*.hpp
%{_libdir}/libbitcoin.a
%{_libdir}/libbitcoin.so
%{_libdir}/pkgconfig/libbitcoin.pc




%changelog
* Tue Feb 28 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170227.1
- Rename package to libbitcoin4

* Mon Feb 27 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170227.0
- Update to 4.0.0 from git master

* Mon Feb 27 2017 Alice Wonder <buildmaster@librelamp.com> - 2.12.0-1.2
- Run make check

* Sun Feb 26 2017 Alice Wonder <buildmaster@librelamp.com> - 2.12.0-1.1
- Change RPM groups to reflect LibBitcoin

* Sun Feb 26 2017 Alice Wonder <buildmaster@librelamp.com> - 2.12.0-1
- Initial RPM spec file
