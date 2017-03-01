Name:		libbitcoin4-protocol
Version:	4.0.0
%define gitdate 20170228
Release:	0.git.%{gitdate}%{?dist}.1
Summary:	Bitcoin Blockchain Query Protocol

Group:		LibBitcoin/Libraries
License:	AGPLv3
URL:		https://libbitcoin.org/
Source0:	871fb7141d1f71ba3b26223e0b95c1c1b9883a82fc7a12d475def4577187ed1b-libbitcoin-protocol-master.zip

BuildRequires:	autoconf automake libtool
BuildRequires:	boost-devel >= 1.57.0
%if 0%{?rhel}
BuildRequires:	compat-zeromq-devel >= 4.2.0
%else
BuildRequires:	zeromq-devel >= 4.2.0
%endif
BuildRequires:	libbitcoin4-devel

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
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_datadir}/doc/libbitcoin-protocol

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
* Tue Feb 28 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.1
- Change name to libbitcoin4-protocol due to devel rather than stable nature.

* Tue Feb 28 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.0
- Initial RPM spec file
