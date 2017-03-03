# LibreOffice

*This is something only CentOS 7 users need to worry about. Fedora users do not
need to update boost and therefore do not need to rebuild LibreOffice.*

It is my suspicion that most people wanting libbitcoin want it for a server
where LibreOffice is not installed. If you use it on the desktop, however,
LibreOffice is one of the packages where the CentOS 7 packages link against
boost, so it has to be rebuilt to upgrade the CentOS 7 provided boost to a
newer version.

I did not just rebuild the CentOS 7 LibreOffice, I decided to update to the
version provided by Fedora Rawhide.

The RPM spec file from Rawhide that I started from had macros to do some things
differently when building on RHEL/CentOS 7. I did not like all of those
differences.

For example, many of the build dependencies are not packaged for CentOS so what
the Fedora Rawhide spec file does in those cases is bundle the source for those
dependencies and build them before building LibreOffice, using those libraries
within LibreOffice.

I chose instead to build those dependencies as separate packages the same way
they are done in Fedora. That way if there is a bug fix to one of those
shared libraries, I can simply update the dependency and do not have to rebuild
all of LibreOffice just to get the bug fix.

I also build LibreOffice against the newer version of ICU. As LibreOffice links
against boost and I build the newer boost against the newer ICU, it made sense
to also build LibreOffice against the newer ICU even though it is not strictly
necessary.

Please note that building LibreOffice takes a long time and takes a lot of
space. I noticed the build goes a lot faster if you have an SSD dedicated for
the mock build root. It also helps to have a good CPU, e.g. a quad core Xeon
with hyper-threading, the build will utilize all 8 threads and it will build
significantly faster than on something like an i5 where only four threads are
available. With 16 GB of memory, building LibreOffice peak memory usage was
at about 75% of available. If you only have 8 GB of memory (or less) building
LibreOffice will likely take quite a bit longer.

## LibreOffice Build Order

If LibreOffice is on your system and needs to be rebuilt for the newer boost
library, make sure `compat-icu` and `boost` are rebuilt first. Then build in
the following order:

* `harfbuzz`
* `libcmis`
* `mdds`
* `libixion`
* `liborcus`
* `libstaroffice`
* `libwps`
* `libzmf`
* `libe-book`

With the exception of `harfbuzz`, just use the source RPM from Fedora Rawhide
for the above packages. They should build just fine in CentOS 7 when built in
that order.

You can find rawhide source packages at the [Fedora Packages Search](https://apps.fedoraproject.org/packages/)
site.

For `harfbuzz` you should use the RPM spec file provided here. The spec file
provided here started life in the Fedora Rawhide world but has been modified
to build against the `compat-icu` package on RHEL/CentOS systems.

Once those dependencies are built you can build LibreOffice packages that link
against the newer boost packages and the newer ICU packages.

For LibreOffice, start with the source RPM from Fedora Rawhide to get the
source tarball and patches (there are a lot). Then replace the RPM spec file
with the LibreOffice spec file that is provided here.

The needed source file `0168229624cfac409e766913506961a8-ucpp-1.3.2.tar.gz` is
not included with the Fedora Rawhide source RPM because of stupid reasons I
will not go into here.

You can get it from [https://svn.apache.org/repos/asf/openoffice/trunk/ext_sources/](https://svn.apache.org/repos/asf/openoffice/trunk/ext_sources/)
