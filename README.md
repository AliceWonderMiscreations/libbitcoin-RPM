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

A sample mock configuration is available in this directory as `libbitcoin-7-x86_64.cfg`

## CC0 Public Domain

No license is required to use the RPM spec files I created here. I consider the
RPM spec files to be Public Domain. See [Creative Commons CC0](https://wiki.creativecommons.org/wiki/CC0).

However please note that it is considered bad form to remove RPM spec file
`changelog` entries. If you do so, though, there are no legal ramifications. I
just might cry if I find out, that is all.

Please note that the Public Domain nature only applies to RPM spec files that
I wrote from scratch (all of the libbitcoin spec files). For several (all
currently) of the other RPM spec files, I started with RPM spec files provided
by CentOS, EPEL, or Fedora.

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

Fedora 25 may need some (or all) of the compatibility packages and the same
type of special handling that CentOS 7 requires, accomplished with the
`%if 0%{?rhel}` blocks within the spec files.

### Install Prefix Notes

By default, RPM and the mock build system will use `/usr` as the install
prefix. Some system administrators may prefer a prefix within `/opt`, such as
`/opt/libbitcoin` or whatever.

Using `/usr` is what I do. If that is fine with you too, then you can skip the
rest of this sub-section.

If you do wish to change the install prefix when building the packages, you
will need to specifically define some macros to the mock system at build time.
For example:

    mock -D '_prefix /opt/libbitcoin' \
      -D '_datadir /usr/share' \
      -r libbitcoin-7-x86_64 \
      compat-libpng-1.6.28-2.el7.centos.0.src.rpm

You *probably* will need to redefine a few other macros so that the `pkgconfig`
utility looks within `/opt/libbitcoin/path` before looking in `/usr/path` etc.

When installing packages built with an alternate `_prefix` you will need to
create a file within the `/etc/ld.so.conf.d/` directory on your filesystem so
the shared libraries can be found without needing to resort to an rpath. For
example, a file containing the following:

    #library path for libbitcoin packages
    /opt/libbitcoin/lib64

## Compatibility Packages

Several of the build dependencies for libbitcoin are newer than the versions of
those libraries in CentOS. In most of those cases, they seem to be optional
build dependencies but are still nice to have.

In the case of boost, it is a must. CentOS 7 ships with boost 1.53.0 and that
will not build libbitcoin.

To remedy this issue, I created compatibility packages that will allow the
newer shared libraries from those packages to be installed in parallel with the
versions of those libraries as supplied by CentOS 7.

## Dependency Build Order

CentOS 7 users will need to create a package repository where the dependencies
can be made available to the mock build system.

The mock build system should also have access to packages in CentOS 7 base,
CentOS 7 updates, and EPEL for CentOS 7.

Build the dependencies in the following order:

* `compat-icu`
* `compat-libpng`
* `compat-qrencode-libs`
* `compat-zeromq`
* `compat-boost`

Once those packages are built, the package repository they are in should be
suitable for building libbitcoin in mock.



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
should not be used on production systems. This branch will only use git master
and will not use tagged source tarballs. That is the nature of a development
branch.

### libbitcoin4.spec

This is the core library for libbitcoin. Last build attempt, both the build
itself and `make check` were successful.

The git project to use: [libbitcoin/libbitcoin](https://github.com/libbitcoin/libbitcoin)

### libbitcoin4-protocol.spec

This is the libbitcoin protocol library. Last build attempt, both the build
itself and `make check` were successful.

The git project to use: [libbitcoin/libbitcoin-protocol](https://github.com/libbitcoin/libbitcoin-protocol)

### libbitcoin4-consensus.spec

This is the libbitcoin library that provides for consensus with bitcoin-core.
It is an optional library but the RPM spec files here will use it when building
other libbitcoin packages.

The spec file may need some adjustments to the python sub-package related to
Fedora packaging guidelines. Specifically the following files:

+ `/usr/lib64/python2.7/site-packages/libbitcoin-consensus/_bitcoin-consensus.a`
+ `/usr/lib64/python2.7/site-packages/libbitcoin-consensus/_bitcoin-consensus.la`
+ `/usr/lib64/python2.7/site-packages/libbitcoin-consensus/_bitcoin-consensus.so`
+ `/usr/lib64/python2.7/site-packages/libbitcoin-consensus/_bitcoin-consensus.so.0`
+ `/usr/lib64/python2.7/site-packages/libbitcoin-consensus/_bitcoin-consensus.so.0.0.0`

That does not look right to me, the `.la` file probably should not be packaged,
the `.a` and `.so` files probably belong in a `-devel` package if packaged at
all, and I do not know about the shared libraries.

Right now it builds the python package for python2 if in CentOS and python3 if
in Fedora. It *probably* should build for both regardless of the OS but I
suspect that will take some effort to accomplish.

Last build attempt, both the build itself and `make check` were successful.

The git project to use: [libbitcoin/libbitcoin-consensus](https://github.com/libbitcoin/libbitcoin-consensus)

### libbitcoin4-database.spec

This is the libbitcoin database library. Last build attempt, both the build
itself and `make check` were successful.

The git project to use: [libbitcoin/libbitcoin-database](https://github.com/libbitcoin/libbitcoin-database)

__note:__ With boost 1.63.0, `make check` fails. The cause of that is still
being investigated.

### libbitcoin4-blockchain.spec

This id the libbitcoin blockchain library. Last build attempt, both the build
itself and `make check` were successful.

The git project to use: [libbitcoin/libbitcoin-blockchain](https://github.com/libbitcoin/libbitcoin-blockchain)

### libbitcoin4-network.spec

This id the libbitcoin network library. Last build attempt, both the build
itself and `make check` were successful.

The git project to use: [libbitcoin/libbitcoin-network](https://github.com/libbitcoin/libbitcoin-network)
