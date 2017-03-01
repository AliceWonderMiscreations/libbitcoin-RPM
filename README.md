LibBitcoin-RPM
==============

RPM spec files for libbitcoin project - CC0 (Creative Commons Public Domain)

These are RPM spec files I created for the libbitcoin project. Please note that
I am not a developer of that project. Bugs with libbitcoin should be reported
to that project, not to me.

The libbitcoin website is [https://libbitcoin.org/](https://libbitcoin.org/).

Their project on GitHub is [https://github.com/libbitcoin](https://github.com/libbitcoin).

## YUM repository

If you just want the RPM packages for CentOS 7, please visit the yum repository
I created for that. Well, it is not live yet, but soon will be. When it is live
there will be a link here.

If you want to build the RPM packages yourself, read on. You need to already
familiar with how to use the [mock](https://github.com/rpm-software-management/mock/)
build system.

## CC0 Public Domain

No license is required to use the RPM spec files I created here. I consider the
RPM spec files to be Public Domain. See [Creative Commons CC0](https://wiki.creativecommons.org/wiki/CC0).

However please note that it is considered bad form to remove RPM spec file
`changelog` entries. If you do so, though, there are no legal ramifications. I
just might cry if I find out, that is all.

Please note that the Public Domain nature only applies to RPM spec files that
I wrote from scratch (all of the libbitcoin spec files). For many of the other
RPM spec files, I started with RPM spec files provided by CentOS, EPEL, or
Fedora.

Obviously I can not apply the CC0 public domain license to those. For RPM
spec files here where `Alice Wonder` is not the oldest entry in the `changelog`
you should assume the same license applies to the spec file that also applies
to the software being packaged by the spec file.

Also please note that the CC0 public domain license I apply to the RPM spec
files I did write from scratch only applies to the spec files themselves, and
not to the software that the spec files create packages for.

I just like my spec files to be CC0 so that no one has to ask me to re-use them
for whatever purpose they want. They can.

## Software Patent Statement

The software that libbitcoin packages depend upon to build are distributed by
distributions like Fedora and CentOS that have legal departments that look out
for software patent infringement and are thus *probably* not in violation of
any currently known valid software patent claims.

With respect to libbitcoin itself, I do not really know if there are any valid
software patent claims and what countries they apply to if they exist, and I do
not really care. I personally find the whole concept of software patents to be
extremely offensive.

However if you care about software patents, or if your legal department cares
about software patents, then it might be prudent to have someone look into it
before deploying libbitcoin because honestly, I do not know and I do not care.

## Spec File Target

I am targeting CentOS 7 with EPEL for some dependencies with these RPM spec
files. What that means is that they should build in mock configured to use the
CentOS 7 base, updates, and EPEL repositories for any build dependencies that
are not part of this spec file collection.

I also *hope* that these RPM spec files will build in Fedora Rawhide and/or the
current stable release of Fedora, however I do not run a Fedora system and I
have no desire to set up a Fedora mock buildroot to find out.

Fedora 25 may need some of the same type of special handling that CentOS 7
requires, but I *think* Fedora 26 (current Rawhide) has new enough packages for
the various libbitcoin dependencies.

## BOOST and ICU

The version of [boost](http://www.boost.org/) in CentOS 7 is too old
to build libbitcoin and the version of [ICU](http://site.icu-project.org/) in
CentOS 7 is too old for the master development branch of libbitcoin.

In the case of ICU, the `libicu` package in CentOS 7 is used by too many RPM
packages for me to consider updating, so a `compat-icu` package is provided
that will allow shared libraries for both versions to be installed at the same
time. This way, the CentOS 7 `libicu` package can be left alone.

In the case of boost, however, not very many packages on my systems actually
use the boost library. Most of my servers did not even have boost installed.

Thus I decided the best thing to do was simply to update the system boost
(using the Fedora 26 Rawhide source RPM) and rebuild the RPM packages from
CentOS 7 and EPEL that I use that did link against boost.

On recent Fedora systems, that should not be an issue, your version of boost
should already be new enough. However if you are on a CentOS 7 system and you
do not like the vendor provided boost packages replaced, then feel free to
solve the boost issue another way (e.g. make a compat package or use the
software collections).

You do not have to agree with my decision to replace the CentOS 7 provided
boost packaging, the beauty of open source is you can choose to do that part
differently.

### Packages that Depend On Boost

_Fedora users should not have to worry about this section_

If you have a desktop environment installed it is quite likely you have a small
number of packages on your system that are linked against the boost libraries.

You can find out what they are with the following command:

    rpm -qa --queryformat "%{name} \n" |grep "^boost" \
      |while read line; do
        rpm --test -e "${line}" >> boost-dependant.txt 2>&1
      done

The resulting file `boost-dependant.txt` will help you understand what packages
currently on your system are linked against the version of boost that CentOS 7
ships with.

You will need to rebuild those packages against the newer boost.

The source RPM for those packages will rebuild against the newer boost without
any issues with one exception:

* LibreOffice

For LibreOffice, please see the [LibreOffice](./LibreOffice.md) file.


## Other Compat Packages

_Fedora users should not have to worry about this section_

In addition to boost and ICU there are a few other build dependencies where the
version in CentOS 7 is not new enough:

* libpng
* qrencode
* zeromq

In those cases I have spec files for compatability packages that allow the
shared library for the needed version to be installed in parallel with the
shared libeary that CentOS ships with.

## Dependency Build Order

CentOS 7 users will need to create a package repository where the dependencies
can be made available to the mock build system.

The mock build system should also have access to packages in CentOS 7 base,
CentOS 7 updates, and EPEL for CentOS 7.

Build the dependencies in the following order:

* `compat-icu`
* `boost`
* `compat-libpng`
* `compat-qrencode`
* `compat-zeromq`



LIBBITCOIN RPM SPEC FILES
=========================

There are two branches of the libbitcoin project, the 3.x branch is the current
stable branch and the 4.x branch is the development branch that should not be
used in production but is very useful for developing software that uses
libbitcoin so that you can know it will be ready when 4.x branch becomes the
stable branch.

RPM spec files are provided for both branches.

The 4.x development branch packages all start with the name `libbitcoin4` and
will have `4.0.0` as the RPM version number and `0.git.` as the start of the
RPM release tag.

The stable 3.x branch packages will all start with the name `libbitcoin` and
*usually* will be built from tagged release tarballs rather than from a git
checkout.

## git packages

When a package is built from a git checkout, the source is what you get from
the `Download ZIP` link with the the `Clone or download` menu from the github
repository for the package.

I then prepend the zip archive name with the `sha256sum` of the zip archive.
After downloading the zip archive yourself, you should do the same and then
modify the `Source0:` in the spec file to reflect the sha256 when you grabbed
the source.

You also will need to change the define `gitdate` macro in the RPM spec file to
reflect the `YYYYMMDD` when you downloaded the zip archive. Do not forget to
make a changelog entry reflecting the date you grabbed the zip archive.

## libbitcoin-libsecp256k1.spec

secp256k1 is not part of the libbitcoin project, that library is actually from
the [bitcoin-core](https://github.com/bitcoin-core/secp256k1) project. However
libbitcoin keeps a fork of it in their project, and that is what I package just
to make sure changes made by bitcoin-core do not break the build of libbitcoin
packages that depend upon it.

This package will likely always use a git checkout as I do not expect tagged
release tarballs for it will ever exist.

The git project to use: [libbitcoin/secp256k1](https://github.com/libbitcoin/secp256k1)

That package is a build dependency of both the 3.x and 4.x branches of
libbitcoin.

## libbitcoin 3.x branch

This branch has not yet been fully tagged, spec files will be uploaded after
the branch is tagged.

## libbitcoin 4.x branch

I have just started writing the RPM spec files for this branch. This branch
should not be used on production systems.

### libbitcoin4.spec

This is the core library for libbitcoin. Last build attempt, both the build
itself and `make check` were successful.

The git project to use: [libbitcoin/libbitcoin](https://github.com/libbitcoin/libbitcoin)

### libbitcoin4-protocol.spec

This is the libbitcoin protocol library. Last build attempt, both the build
itself and `make check` were successful.

The git project to use: [libbitcoin/libbitcoin-protocol](https://github.com/libbitcoin/libbitcoin-protocol)
