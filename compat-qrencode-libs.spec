Name:           compat-qrencode-libs
Version:        3.4.4
Release:        1%{?dist}.1
Summary:        QR Code encoding library

License:        LGPLv2+
URL:            http://fukuchi.org/works/qrencode/
Source0:        http://fukuchi.org/works/qrencode/qrencode-%{version}.tar.bz2

BuildRequires:	chrpath
BuildRequires:	compat-libpng-devel
BuildRequires:	SDL-devel
## For ARM 64 support (RHBZ 926414)
BuildRequires:	autoconf >= 2.69
%if "%{_prefix}" != "/usr"
BuildRequires: libbitcoin-prefix-setup-devel
Requires:      libbitcoin-prefix-setup
%endif

%description
Qrencode is a utility software using libqrencode to encode string data in
a QR Code and save as a PNG image.

This package contains shared libraries for qrencode %{version}


%package        -n compat-qrencode-devel
Summary:        QR Code encoding library - Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    -n compat-qrencode-devel
The qrencode-devel package contains libraries and header files for developing
applications that use qrencode.


%prep
%setup -q -n qrencode-%{version}


%build
%if 0%{?_btc_pkgconfig:1}%{!?_btc_pkgconfig:0}
  PKG_CONFIG_PATH="%{_btc_pkgconfig}"
  export PKG_CONFIG_PATH
%endif
## Rebuild configure scripts for ARM 64 support. (RHBZ 926414)
%{__autoconf}
%configure --with-tests
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -rf $RPM_BUILD_ROOT%{_libdir}/libqrencode.la
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/qrencode
# don't package binary
rm -f %{buildroot}%{_bindir}/qrencode
rm -f %{buildroot}%{_mandir}/man1/qrencode.*
%if "%{_prefix}" == "/usr"
# don't package the .3 symlink
rm -f %{buildroot}%{_libdir}/libqrencode.so.3
%endif


%check
cd ./tests
sh test_all.sh


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc ChangeLog NEWS README TODO
%if "%{_prefix}" != "/usr"
%{_libdir}/libqrencode.so.*
%else
%{_libdir}/libqrencode.so.3.*
%endif

%files -n compat-qrencode-devel
%{_includedir}/qrencode.h
%{_libdir}/libqrencode.so
%{_libdir}/pkgconfig/libqrencode.pc


%changelog
* Fri Mar 03 2017 Alice Wonder <buildmaster@librelamp.com> - 3.4.4-1.1
- Allow for custom %%{_prefix} at package build

* Mon Feb 27 2017 Alice Wonder <buildmaster@librelamp.com> - 3.4.4-1
- Rename to compat-qrencode-libs for CentOS 7 build
- Only package the libs, not the binary

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug  4 2014 Tom Callaway <spot@fedoraproject.org> - 3.4.2-3
- fix license handling

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 11 2013 Peter Gordon <peter@thecodergeek.com> - 3.4.2-1
- Update to new upstream release (3.4.2)
  - Fixes a memory leak, string-splitting, and Micro QR encoding bugs.
- Run autoconf in %%build to add ARM 64 (aarch64) to the configure scripts.
- Resolves:  #926414 (qrencode: Does not support aarch64 in f19 and rawhide)
- Update source/homepage URLs.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1

* Fri Sep 21 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 3.3.1-4
- Add libs subpackage (fix RHBZ #856808)

* Thu Aug 16 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 3.3.1-3
- Add French translation in spec file
- Fix incomplete removing Group tags in spec file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 3.3.1-1
- update to 3.3.1
- remove "Group" tag in spec file
- fix manfile suffix
- remove patch to fix improper LIBPTHREAD macro in the pkgconfig file:
  - upstream issue

* Sat Feb 25 2012 Peter Gordon <peter@thecodergeek.com> - 3.2.0-3
- Fix applying the LIBPTHREAD patch. (Thanks to Matthieu Saulnier.)

* Thu Feb 23 2012 Peter Gordon <peter@thecodergeek.com> - 3.2.0-2
- Add patch to fix improper LIBPTHREAD macro in the pkgconfig file:
  + fix-LIBPTHREAD-macro.patch
- Resolves: #795582 (qrencode-devel: Malformed pkgconfig file causes build to
  fail ("@LIBPTHREAD@: No such file or directory"))

* Sun Jan 15 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 3.2.0-1
- update to 3.2.0
- remove BuildRoot tag in spec file
- remove "rm -rf $RPM_BUILD_ROOT" at the beginning of %%install section
- remove %%clean section
- remove %%defattr lines
- add a joker for libqrencode.so.* files

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.1.1-6
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 3.1.1-4
- Fixed the rpath problem.

* Mon Jul 12 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 3.1.1-3
- Fixed some small spec mistakes.

* Mon Jul 12 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 3.1.1-2
- Fixed some small errors.

* Thu Jul 08 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 3.1.1-1
- Initial build.
