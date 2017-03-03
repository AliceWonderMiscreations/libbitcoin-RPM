Name:           harfbuzz
Version:        1.4.1
Release:        2%{?dist}.0
Summary:        Text shaping library

License:        MIT
URL:            http://freedesktop.org/wiki/Software/HarfBuzz
Source0:        http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-%{version}.tar.bz2

BuildRequires:  cairo-devel
BuildRequires:  freetype-devel
BuildRequires:  glib2-devel
%if 0%{?rhel}
BuildRequires:	compat-libicu-devel
%else
BuildRequires:  libicu-devel
%endif
BuildRequires:  graphite2-devel
BuildRequires:  gtk-doc

%description
HarfBuzz is an implementation of the OpenType Layout engine.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-icu%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        icu
Summary:        Harfbuzz ICU support library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    icu
This package contains Harfbuzz ICU support library.

%prep
%setup -q


%build
%configure --disable-static --with-graphite2

# Remove lib64 rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post icu -p /sbin/ldconfig
%postun icu -p /sbin/ldconfig


%files
%license COPYING
%doc NEWS AUTHORS README
%{_libdir}/libharfbuzz.so.*

%files devel
%doc %{_datadir}/gtk-doc
%{_bindir}/hb-view
%{_bindir}/hb-ot-shape-closure
%{_bindir}/hb-shape
%{_includedir}/harfbuzz/
%{_libdir}/libharfbuzz.so
%{_libdir}/pkgconfig/harfbuzz.pc
%{_libdir}/libharfbuzz-icu.so
%{_libdir}/pkgconfig/harfbuzz-icu.pc

%files icu
%{_libdir}/libharfbuzz-icu.so.*

%changelog
* Wed Mar 01 2017 Alice Wonder <buildmaster@librelamp.com> - 1.4.1-2.0
- Use compat-icu for build dependency on CentOS systems

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 06 2017 Parag Nemade <pnemade AT redhat DOT com> - 1.4.1-1
- Update to 1.4.1

* Thu Jan 05 2017 Parag Nemade <pnemade AT redhat DOT com> - 1.4.0-1
- Update to 1.4.0

* Tue Dec 06 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.3.4-1
- Update to 1.3.4

* Fri Oct 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.3.3-1
- Update to 1.3.3

* Wed Sep 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.3.2-1
- Update to 1.3.2

* Thu Sep 08 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.3.1-1
- Update to 1.3.1

* Sun Jul 24 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.3.0-1
- Update to 1.3.0

* Mon May 02 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.2.7-1
- Update to 1.2.7

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 1.2.6-2
- rebuild for ICU 57.1

* Sun Apr 10 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.2.6-1
- Update to 1.2.6

* Tue Apr 05 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.2.5-1
- Update to 1.2.5

* Sat Mar 19 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.2.4-1
- Update to 1.2.4

* Fri Feb 26 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.2.3-1
- Update to 1.2.3

* Thu Feb 25 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.2.2-1
- Update to 1.2.2

* Thu Feb 25 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.2.1-1
- Update to 1.2.1

* Mon Feb 22 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.2.0-1
- Update to 1.2.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.1.3-1
- Update to 1.1.3

* Mon Dec 21 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.1.2-1
- Update to 1.1.2

* Thu Nov 26 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.1.1-1
- Update to 1.1.1

* Thu Nov 19 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.1.0-1
- Update to 1.1.0

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 1.0.6-2
- rebuild for ICU 56.1

* Fri Oct 16 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.6-1
- Update to 1.0.6

* Wed Oct 14 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.5-1
- Update to 1.0.5

* Thu Oct 01 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.4-1
- Update to 1.0.4

* Tue Sep 01 2015 Kalev Lember <klember@redhat.com> - 1.0.3-1
- Update to 1.0.3
- Use license macro for COPYING

* Mon Aug 24 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-1
- Update to 1.0.2

* Wed Jul 29 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.1-1
- Update to 1.0.1

* Fri Jun 19 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.9.41-1
- Update to 0.9.41 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.40-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 21 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.9.40-1
- Update to 0.9.40 upstream release

* Fri Mar 06 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.9.39-1
- Update to 0.9.39 upstream release

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.9.38-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 0.9.38-3
- Bump for rebuild.

* Wed Feb  4 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9.38-2
- Rebuild for libicu soname bump

* Tue Jan 27 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.9.38-1
- Update to 0.9.38 upstream release

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 0.9.37-2
- rebuild for ICU 54.1

* Tue Dec 23 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.37-1
- Update to 0.9.37 upstream release

* Tue Nov 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.36-1
- Update to 0.9.36 upstream release

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 0.9.35-3
- rebuild for ICU 53.1

* Mon Aug 18 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.35-1
- Update to 0.9.35 upstream release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 06 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.34-1
- Update to 0.9.34 upstream release

* Tue Jul 29 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.33-1
- Update to 0.9.33 upstream release

* Fri Jul 18 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.32-1
- Update to 0.9.32 (have all the recent releases on koji)

* Thu Jul 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.31-1
- Update to 0.9.31 (have all the recent releases on koji)

* Fri Jul 11 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.30-1
- Update to 0.9.30 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.29-1
- Update to 0.9.29 upstream release

* Tue Apr 29 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.28-1
- Update to 0.9.28 upstream release

* Thu Mar 20 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.27-1
- Update to 0.9.27 upstream release

* Wed Feb 12 2014 Nils Philippsen <nils@redhat.com> - 0.9.26-3
- rebuild for new libicu

* Wed Feb 12 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 0.9.26-2
- Rebuilding for icu soname bump.

* Fri Jan 31 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.26-1
- Update to 0.9.26 upstream release

* Thu Dec 05 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.25-1
- Update to 0.9.25 upstream release

* Fri Nov 15 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.24-1
- Update to 0.9.24 upstream release

* Wed Oct 30 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.23-1
- Update to 0.9.23 upstream release

* Tue Oct 08 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.22-1
- Update to 0.9.22 upstream release

* Tue Sep 17 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.21-1
- Update to 0.9.21 upstream release

* Fri Aug 30 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.20-1
- Update to 0.9.20 upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.19-1
- Update to 0.9.19 upstream release

* Fri Jun 21 2013 Matthias Clasen <mclasen@redhat.com> - 0.9.18-3
- Don't ship a (humongous) ChangeLog

* Fri Jun 07 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.18-2
- Resolves:rh#971795:Merge -icu-devel subpackage into -devel subpackage

* Wed Jun 05 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.18-1
- Update to 0.9.18 upstream release

* Tue May 21 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.17-1
- Update to 0.9.17 upstream release

* Sat Apr 20 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.16-1
- Update to 0.9.16 upstream release

* Fri Mar 22 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.14-1
- Update to 0.9.14 upstream release

* Tue Feb 26 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.13-1
- Update to 0.9.13 upstream release

* Wed Jan 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.12-6
- Kill icu-config hack and rebuild against new icu again

* Tue Jan 29 2013 Parag Nemade <pnemade AT pnemade DOT com> - 0.9.12-5
- Resolves:rh#905334 - Please rebuild harfbuzz for new graphite-1.2.0

* Sun Jan 27 2013 Parag Nemade <pnemade AT pnemade DOT com> - 0.9.12-4
- Resolves:rh#904700-Enable additional shaper graphite2

* Sat Jan 26 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.12-3
- Add "icu-config --cppflags" to compiler flags to fix build

* Fri Jan 25 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.12-2
- Rebuild for libicu 50

* Sun Jan 20 2013 Parag Nemade <pnemade AT pnemade DOT com> - 0.9.12-1
- Update to 0.9.12 upstream release

* Fri Jan 11 2013 Parag Nemade <pnemade AT pnemade DOT com> - 0.9.11-1
- Update to 0.9.11 upstream release

* Thu Jan 03 2013 Parag Nemade <pnemade AT pnemade DOT com> - 0.9.10-1
- Update to 0.9.10 upstream release

* Thu Dec 06 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.9-1
- Update to 0.9.9 upstream release

* Wed Dec 05 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.8-1
- Update to 0.9.8 upstream release

* Wed Nov 21 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.7-1
- Update to 0.9.7 upstream release

* Wed Nov 14 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.6-1
- Update to 0.9.6 upstream release

* Mon Oct 15 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.5-1
- Update to 0.9.5 upstream release

* Mon Sep 10 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.4-1
- Update to 0.9.4 upstream release

* Sun Aug 19 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.3-1
- Update to 0.9.3 upstream release

* Mon Aug 13 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.2-1
- Update to 0.9.2 upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Kalev Lember <kalevlember@gmail.com> - 0.6.0-6
- Rebuilt for libicu 49

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.0-4
- Rebuild for new libpng

* Sat Sep 10 2011 Kalev Lember <kalevlember@gmail.com> - 0.6.0-3
- Rebuilt for libicu 4.8

* Thu Jun 16 2011 Kalev Lember <kalev@smartlink.ee> - 0.6.0-2
- Moved hb-view to -devel subpackage (#713126)

* Tue Jun 14 2011 Kalev Lember <kalev@smartlink.ee> - 0.6.0-1
- Initial RPM release
