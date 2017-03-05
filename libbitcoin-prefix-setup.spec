Name:		libbitcoin-prefix-setup
Version:	1
Release:	1.2
Summary:	Configuration files for libbitcoin install path

Group:		LibBitcoin/Misc
License:	CC0
URL:		https://github.com/AliceWonderMiscreations/libbitcoin-RPM

BuildRequires:	python2-devel
%if 0%{?rhel}
BuildRequires:	python34-devel
%else
BuildRequires:	python3-devel
%endif

%description
This package installs a configuration file into /etc/ld.so.conf.d/ that allows
/sbin/ldconfig to find the shared libraries installed in %{_libdir}.

%package devel
Summary:	PKG_CONFIG_PATH macro
Group:		LibBitcoin/Misc
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains an RPM macro file that allows us to intelligently define
the PKG_CONFIG_PATH when building libbitcoin packages without impacting the
PKG_CONFIG_PATH when building RPM packages that are not related to libbitcoin.

Ideally this package will only be installed in the mock buildroot but it can be
installed on the system itself without causing any harm.

%package -n libbitcoin-prefix-python
Summary:	Python path support
Group:		LibBitcoin/Python
Requires:	%{name} = %{version}-%{release}
Provides:	libbitcoin-prefix-python2 = %{version}-%{release}

%description -n libbitcoin-prefix-python
This package adds support for libbitcoin-related python%{python2_version} packages that are
installed with a custom %%{_prefix}.

%package -n libbitcoin-prefix-python3
Summary:	Python path support
Group:		LibBitcoin/Python
Requires:       %{name} = %{version}-%{release}

%description -n libbitcoin-prefix-python3
This package adds support for libbitcoin-related python%{python3_version} packages that are
installed with a custom %%{_prefix}.

%prep


%build


%install
%if "%{_prefix}" == "/usr"
echo "=== The %%{_prefix} macros is set to /usr - exiting ==="
/bin/false
%endif

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_libexecdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_prefix}/share/doc
mkdir -p %{buildroot}%{_mandir}/man{1,2,3,4,5,6,7,8}
mkdir -p %{buildroot}%{_sysconfdir}/libbitcoin
mkdir -p %{buildroot}%{_prefix}/etc
ln -sf %{_sysconfdir}/libbitcoin %{buildroot}%{_prefix}/etc/libbitcoin
%if "%{_lib}" != "lib"
mkdir -p %{buildroot}%{_prefix}/lib
%endif

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat <<EOF > %{buildroot}%{_sysconfdir}/ld.so.conf.d/libbitcoin.conf
# Shared libraries for libbitcoin
%{_libdir}
EOF

mkdir -p %{buildroot}%{_usr}/lib/rpm/macros.d
cat <<EOF > %{buildroot}%{_usr}/lib/rpm/macros.d/macros.btcpkgconfig
#Attempt to set sane pkgconfig path
%%btc_pkgconfig %%{_libdir}/pkgconfig:%%{_usr}/%%{_lib}/pkgconfig:%%{_usr}/share/pkgconfig
EOF

cat <<EOF > %{buildroot}%{_usr}/lib/rpm/macros.d/macros.btcpython2
%%btc_py2_sitelib %%{_prefix}/lib/python%%{python2_version}/site-packages
%%btc_py2_sitearch %%{_prefix}/%{_lib}/python%%{python2_version}/site-packages
EOF
#python3
cat <<EOF > %{buildroot}%{_usr}/lib/rpm/macros.d/macros.btcpython3
%%btc_py3_sitelib %%{_prefix}/lib/python%%{python3_version}/site-packages
%%btc_py3_sitearch %%{_prefix}/%{_lib}/python%%{python3_version}/site-packages
EOF
#make the python directories
mkdir -p %{buildroot}%{_prefix}/lib/python%{python2_version}/site-packages
mkdir -p %{buildroot}%{_prefix}/lib/python%{python3_version}/site-packages
%if "%{_lib}" != "lib"
mkdir -p %{buildroot}%{_prefix}/%{_lib}/python%{python2_version}/site-packages
mkdir -p %{buildroot}%{_prefix}/%{_lib}/python%{python3_version}/site-packages
%endif

#add to "official" search path
mkdir -p %{buildroot}%{python2_sitelib}
mkdir -p %{buildroot}%{python3_sitelib}
cat <<EOF > %{buildroot}%{python2_sitelib}/libbitcoin.pth
%{_prefix}/lib/python%{python2_version}/site-packages
EOF
cat <<EOF > %{buildroot}%{python3_sitelib}/libbitcoin.pth
%{_prefix}/lib/python%{python3_version}/site-packages
EOF
%if "%{_lib}" != "lib"
mkdir -p %{buildroot}%{python2_sitearch}
mkdir -p %{buildroot}%{python3_sitearch}
cat <<EOF > %{buildroot}%{python2_sitearch}/libbitcoin.pth
%{_prefix}/%{_lib}/python%{python2_version}/site-packages
EOF
cat <<EOF > %{buildroot}%{python3_sitearch}/libbitcoin.pth
%{_prefix}/%{_lib}/python%{python3_version}/site-packages
EOF
%endif

#These scriptlets are not really needed but they also do not hurt.
# -- just in case the package manager installs the libraries before this package.
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%attr(0644,root,root) %config %{_sysconfdir}/ld.so.conf.d/libbitcoin.conf
%attr(0755,root,root) %dir %{_prefix}
%attr(0755,root,root) %dir %{_sysconfdir}/libbitcoin
%attr(0755,root,root) %dir %{_bindir}
%attr(0755,root,root) %dir %{_libdir}
%attr(0755,root,root) %dir %{_libdir}/pkgconfig
%attr(0755,root,root) %dir %{_libexecdir}
%attr(0755,root,root) %dir %{_includedir}
%attr(0755,root,root) %dir %{_prefix}/share
%attr(0755,root,root) %dir %{_prefix}/share/doc
%attr(0755,root,root) %dir %{_mandir}
%attr(0755,root,root) %dir %{_mandir}/man*
%attr(0755,root,root) %dir %{_prefix}/etc
%{_prefix}/etc/libbitcoin
%if "%{_lib}" != "lib"
%attr(0755,root,root) %dir %{_prefix}/lib
%endif

%files devel
%attr(0644,root,root) %{_usr}/lib/rpm/macros.d/macros.btcpkgconfig

%files -n libbitcoin-prefix-python
%attr(0644,root,root) %{_usr}/lib/rpm/macros.d/macros.btcpython2
%attr(0644,root,root) %{python2_sitelib}/libbitcoin.pth
%attr(0755,root,root) %dir %{_prefix}/lib/python%{python2_version}
%attr(0755,root,root) %dir %{_prefix}/lib/python%{python2_version}/site-packages
%if "%{_lib}" != "lib"
%attr(0644,root,root) %{python2_sitearch}/libbitcoin.pth
%attr(0755,root,root) %dir %{_prefix}/%{_lib}/python%{python2_version}
%attr(0755,root,root) %dir %{_prefix}/%{_lib}/python%{python2_version}/site-packages
%endif

%files -n libbitcoin-prefix-python3
%attr(0644,root,root) %{_usr}/lib/rpm/macros.d/macros.btcpython3
%attr(0644,root,root) %{python3_sitelib}/libbitcoin.pth
%attr(0755,root,root) %dir %{_prefix}/lib/python%{python3_version}
%attr(0755,root,root) %dir %{_prefix}/lib/python%{python3_version}/site-packages
%if "%{_lib}" != "lib"
%attr(0644,root,root) %{python3_sitearch}/libbitcoin.pth
%attr(0755,root,root) %dir %{_prefix}/%{_lib}/python%{python3_version}
%attr(0755,root,root) %dir %{_prefix}/%{_lib}/python%{python3_version}/site-packages
%endif


%changelog
* Sat Mar 04 2017 Alice Wonder <buildmaster@librelamp.com> - 1-1.2
- Create python3 sub-package
- Create (and own) directory structure within the %%{_prefix}

* Sat Mar 04 2017 Alice Wonder <buildmaster@librelamp.com> - 1-1.1
- Do not start custom macros with an underscore
- Add python sub-package to provide custom prefix support with python

* Fri Mar 03 2017 Alice Wonder <buildmaster@librelamp.com> - 1-1
- Initial RPM spec file
