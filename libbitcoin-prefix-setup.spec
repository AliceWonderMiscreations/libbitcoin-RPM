Name:		libbitcoin-prefix-setup
Version:	1
Release:	1
Summary:	Configuration files for libbitcoin install path

Group:		LibBitcoin/Misc
License:	CC0
URL:		https://github.com/AliceWonderMiscreations/libbitcoin-RPM

%description
This package installs a configuration file into /etc/ld.so.conf.d/ that allows
/sbin/ldconfig to find the shared libraries installed in %{_libdir}.

%package devel
Summary:	PKG_CONFIG_PATH macro
Group:		LibBitcoin/Misc
Requires:	%{name} = %{version}

%description devel
This package contains an RPM macro file that allows us to intelligently define
the PKG_CONFIG_PATH when building libbitcoin packages without impacting the
PKG_CONFIG_PATH when building RPM packages that are not related to libbitcoin.

Ideally this package will only be installed in the mock buildroot but it can be
installed on the system itself without causing any harm.

%prep


%build


%install
%if "%{_prefix}" == "/usr"
echo "=== The %%{_prefix} macros is set to /usr - exiting ==="
/bin/false
%endif

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat <<EOF > %{buildroot}%{_sysconfdir}/ld.so.conf.d/libbitcoin.conf
# Shared libraries for libbitcoin
%{_libdir}
EOF

mkdir -p %{buildroot}%{_usr}/lib/rpm/macros.d
cat <<EOF > %{buildroot}%{_usr}/lib/rpm/macros.d/macros.libbitcoin
#Attempt to set sane pkgconfig path
%%_btc_pkgconfig %%{_libdir}/pkgconfig:%%{_usr}/%%{_lib}/pkgconfig:%%{_usr}/share/pkgconfig
EOF

#These scriptlets are not really needed but they also do not hurt.
# -- just in case the package manager installs the libraries before this package.
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%attr(0644,root,root) %config %{_sysconfdir}/ld.so.conf.d/libbitcoin.conf

%files devel
%attr(0644,root,root) %{_usr}/lib/rpm/macros.d/macros.libbitcoin


%changelog
* Fri Mar 03 2017 Alice Wonder <buildmaster@librelamp.com> - 1-1
- Initial RPM spec file
