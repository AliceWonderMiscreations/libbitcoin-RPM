# libbitcoin-RPM

RPM spec files for libbitcoin client - CC0 (Creative Commons Public Domain)

These are RPM spec files I created for the libbitcoin project. Please note that
I am not a developer of that project. Bugs with libbitcoin should be reported
to that project, not to me.

The libbitcoin website is [https://libbitcoin.org/](https://libbitcoin.org/).

Their project on GitHub is [https://github.com/libbitcoin](https://github.com/libbitcoin).

## Public Domain
No license is required to use the RPM spec files provided here. I consider the
RPM spec files to be Public Domain. See [Creative Commons CC0](https://wiki.creativecommons.org/wiki/CC0).

However please note that it is considered bad form to remove RPM spec file
changelog entries. If you do so, though, there are no legal ramifications. I just might
cry if I find out.

Please note that the Public Domain nature only applies to RPM spec files that
I wrote from scratch (all of the libbitcoin spec files). For many of the RPM
spec files, I started with RPM spec files provided by CentOS, EPEL, or Fedora.

Obviously I can not apply the CC0 public domain license to those. The license
for the software packaged applies to those unless the people who originally
wrote those spec files applied a different one.

Also please note that the CC0 public domain license I apply to the RPM spec
files I did write from scratch only applies to the spec files themselves, and
not to the software that the spec files create packages for.

## Spec File Target
I am targeting CentOS 7 with EPEL for some dependencies with these RPM spec
files. What that means is that they should build in [mock](https://github.com/rpm-software-management/mock/)
configured to use the CentOS 7 base, updates, and EPEL repositories for any
build dependencies.

I also *hope* that these RPM spec files will build in Fedora Rawhide and/or the
current stable release of Fedora, however I do not run a Fedora system and I
have no desire to set up a Fedora mock buildroot to find out.

## BOOST and ICU

The version of [boost](http://www.boost.org/) in CentOS 7 is too old
to build libbitcoin and the version of [ICU](http://site.icu-project.org/) in
CentOS 7 is too old for the master development branch of libbitcoin.

In the case of ICU, the `libicu` package in CentOS 7 is used by too many RPM
packages for me to consider updating, so a `compat-icu` package is provided
that will allow shared libraries for both versions to be installed at the same
time. This way, the CentOS 7 `libicu` package can be left alone.

In the case of boost, however, not very many packages on my systems actually
use the boost library, so I decided the best thing to do was simply to update
the system boost (using the Fedora 26 Rawhide source RPM) and rebuild the RPM
packages from CentOS 7 and EPEL that I use that did link against boost.

On recent Fedora systems, that should not be an issue, your version of boost
should already be new enough. However if you are on a CentOS 7 system and you
do not like the vendor provided boost packages replaced, then feel free to
solve the boost issue another way (e.g. make a compat package or use the
software collections).

You do not have to agree with my decision to replace the CentOS 7 provided
boost packaging, the beauty of open source is you can choose to do that part
differently.

### LibreOffice

It is my suspicion that most people wanting libbitcoin want it for a server
where LibreOffice is not installed. If you use it on the desktop, however,
LibreOffice is one of the packages where the CentOS 7 version links against
boost and has to be rebuilt to upgrade the CentOS 7 provided boost to a newer
version.

I did not just rebuild the CentOS 7 LibreOffice, I decided to update to the
version provided by Fedora Rawhide.

The RPM spec file from Rawhide that I started from had macros to do some things
differently when building on RHEL/CentOS 7. I did not like all of those
differences.

For example, many of the build dependencies are not packaged for CentOS so what
the spec file does in those cases is bundle the source for those dependencies
and build them before building LibreOffice, using those libraries within
LibreOffice.

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
the mock build root. It also helps to have a good CPU, e.g. a quad code Xeon
with hyper-threading, the build will utilize all 8 threads and it will build
significantly faster than on something like an i5 where only four threads are
available. With 16 GB of memory, building LibreOffice peak memory usage was
at about 75% of available.
