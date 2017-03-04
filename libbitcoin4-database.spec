Name:		libbitcoin4-database
Version:	4.0.0
%define gitdate 20170228
Release:	0.git.%{gitdate}%{?dist}.2
Summary:	Bitcoin High Performance Blockchain Database

Group:		LibBitcoin/Libraries
License:	AGPLv3
URL:		https://libbitcoin.org/
Source0:	52f4616dc595850ac469dfa1f0721540a05a399eb9f6ecdf79167f6ec2d9f86e-libbitcoin-database-master.zip

BuildRequires:	autoconf automake libtool
BuildRequires:	libbitcoin4-devel
%if 0%{?rhel}
BuildRequires:	compat-boost-devel >= 1.57.0
BuildRequires:	compat-boost-test >= 1.57.0
%else
BuildRequires:	boost-devel >= 1.57.0
BuildRequires:	boost-test >= 1.57.0
%endif
%if "%{_prefix}" != "/usr"
BuildRequires: libbitcoin-prefix-setup-devel
Requires:      libbitcoin-prefix-setup
%endif

%description
Libbitcoin Database is a custom database build directly on the operating
system's memory-mapped file system. All primary tables and indexes are built on
in-memory hash tables, resulting in constant-time lookups. The database uses
sequence locking to avoid blocking the writer. This is ideal for a high
performance blockchain server as reads are significantly more frequent than
writes and yet writes must proceed wtihout delay. The libbitcoin-blockchain
library uses the database as its blockchain store.

%package devel
Summary:	Development files for %{name}
Group:		LibBitcoin/Development
Requires:	%{name} = %{version}-%{release}
Requires:	libbitcoin4-devel

%description devel
This package contains the development header files and libraries needed to
compile software that links against %{name}.


%prep
%setup -q -n libbitcoin-database-master
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
rm -f %{buildroot}%{_libdir}/libbitcoin-database.la
rm -rf %{buildroot}%{_prefix}/share/doc/libbitcoin-database

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
%{_includedir}/bitcoin/database.hpp
%dir %{_includedir}/bitcoin/database
%{_includedir}/bitcoin/database/*.hpp
%dir %{_includedir}/bitcoin/database/databases
%{_includedir}/bitcoin/database/databases/*.hpp
%dir %{_includedir}/bitcoin/database/impl
%{_includedir}/bitcoin/database/impl/*.ipp
%dir %{_includedir}/bitcoin/database/memory
%{_includedir}/bitcoin/database/memory/*.hpp
%dir %{_includedir}/bitcoin/database/primitives
%{_includedir}/bitcoin/database/primitives/*.hpp
%dir %{_includedir}/bitcoin/database/result
%{_includedir}/bitcoin/database/result/*.hpp
%{_libdir}/libbitcoin-database.a
%{_libdir}/libbitcoin-database.so
%{_libdir}/pkgconfig/libbitcoin-database.pc



%changelog
* Fri Mar 03 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.2
- Fix for defining an alternate %%_prefix at build time.
- Optional macro for defining --with-boost and --with-boost-libdir configure options

* Thu Mar 02 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.1
- Building against boost 1.58.0 to fix make check issue

* Tue Feb 28 2017 Alice Wonder <buildmaster@librelamp.com> - 4.0.0-0.git.20170228.0
- Initial RPM spec file. make check currently fails.

