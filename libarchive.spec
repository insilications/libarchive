#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libarchive
Version  : 3.5.1
Release  : 62
URL      : file:///aot/build/clearlinux/packages/libarchive/libarchive-3.5.1.tar.gz
Source0  : file:///aot/build/clearlinux/packages/libarchive/libarchive-3.5.1.tar.gz
Summary  : A library for handling streaming archive formats
Group    : Development/Tools
License  : BSD-2-Clause
Requires: libarchive-bin = %{version}-%{release}
Requires: libarchive-lib = %{version}-%{release}
Requires: libarchive-man = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : acl-dev32
BuildRequires : acl-staticdev
BuildRequires : acl-staticdev32
BuildRequires : attr-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : bzip2-dev
BuildRequires : bzip2-dev32
BuildRequires : bzip2-staticdev
BuildRequires : dbus-dev
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : e2fsprogs-dev
BuildRequires : elfutils-dev
BuildRequires : expat-dev
BuildRequires : expat-dev32
BuildRequires : expat-staticdev
BuildRequires : expat-staticdev32
BuildRequires : expect
BuildRequires : fakechroot
BuildRequires : fakechroot-dev
BuildRequires : fakechroot-staticdev
BuildRequires : file-dev
BuildRequires : findutils
BuildRequires : flex
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb
BuildRequires : gdb-dev
BuildRequires : gettext-bin
BuildRequires : git
BuildRequires : glibc-bench
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : gmp-dev
BuildRequires : gmp-staticdev
BuildRequires : libcap-dev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libgcrypt
BuildRequires : libgcrypt-dev
BuildRequires : libstdc++
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libunwind
BuildRequires : libunwind-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : lrzip-dev
BuildRequires : lrzip-staticdev
BuildRequires : lz4-dev
BuildRequires : lz4-staticdev
BuildRequires : lzo-dev
BuildRequires : lzo-dev32
BuildRequires : lzo-staticdev
BuildRequires : lzo-staticdev32
BuildRequires : m4
BuildRequires : nettle-dev
BuildRequires : nettle-dev32
BuildRequires : openssl-dev
BuildRequires : openssl-dev32
BuildRequires : openssl-staticdev
BuildRequires : openssl-staticdev32
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(32bzip2)
BuildRequires : pkgconfig(32hogweed)
BuildRequires : pkgconfig(32libacl)
BuildRequires : pkgconfig(32nettle)
BuildRequires : pkgconfig(bzip2)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(hogweed)
BuildRequires : pkgconfig(libacl)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(lrzip)
BuildRequires : pkgconfig(nettle)
BuildRequires : popt-dev
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : sqlite-autoconf
BuildRequires : unzip
BuildRequires : xz-dev
BuildRequires : xz-dev32
BuildRequires : xz-staticdev
BuildRequires : xz-staticdev32
BuildRequires : zip
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
BuildRequires : zlib-staticdev32
BuildRequires : zstd-dev
BuildRequires : zstd-dev32
BuildRequires : zstd-staticdev
BuildRequires : zstd-staticdev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Libarchive is a programming library that can create and read several different
streaming archive formats, including most popular tar variants, several cpio
formats, and both BSD and GNU ar variants. It can also write shar archives and
read ISO9660 CDROM images and ZIP archives.

%package bin
Summary: bin components for the libarchive package.
Group: Binaries

%description bin
bin components for the libarchive package.


%package dev
Summary: dev components for the libarchive package.
Group: Development
Requires: libarchive-lib = %{version}-%{release}
Requires: libarchive-bin = %{version}-%{release}
Provides: libarchive-devel = %{version}-%{release}
Requires: libarchive = %{version}-%{release}

%description dev
dev components for the libarchive package.


%package lib
Summary: lib components for the libarchive package.
Group: Libraries

%description lib
lib components for the libarchive package.


%package man
Summary: man components for the libarchive package.
Group: Default

%description man
man components for the libarchive package.


%package staticdev
Summary: staticdev components for the libarchive package.
Group: Default
Requires: libarchive-dev = %{version}-%{release}

%description staticdev
staticdev components for the libarchive package.


%prep
%setup -q -n libarchive
cd %{_builddir}/libarchive

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620523295
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FCFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export CXXFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export LDFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags_pgo end
sd --flags mi '^AC_INIT\((.*\n.*\)|.*\))' '$0\nAM_MAINTAINER_MODE([disable])' configure.ac
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%reconfigure --with-acl \
--with-zlib \
--with-bz2lib \
--with-zstd \
--with-lzma \
--with-libxml2 \
--with-expat \
--with-lz4 \
--with-xml2 \
--with-lzo2 \
--with-openssl \
--enable-shared \
--enable-static \
--enable-bsdtar=static \
--enable-bsdcat=static \
--enable-bsdcpio=static \
--enable-posix-regex-lib \
--disable-maintainer-mode
## make_prepend content
find . -type f -name 'Makefile' -exec sed -i 's:-lbz2\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libbz2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lz\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libz.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-llzma\b:-Wl,--whole-archive,--as-needed,/usr/lib64/liblzma.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lzstd\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libzstd.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lacl\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libacl.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-llz4\b:-Wl,--whole-archive,--as-needed,/usr/lib64/liblz4.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-llzo2\b:-Wl,--whole-archive,--as-needed,/usr/lib64/liblzo2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lxml2\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libxml2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lexpat\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libexpat.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1

make VERBOSE=1 V=1 -j1 check || :
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%reconfigure --with-acl \
--with-zlib \
--with-bz2lib \
--with-zstd \
--with-lzma \
--with-libxml2 \
--with-expat \
--with-lz4 \
--with-xml2 \
--with-lzo2 \
--with-openssl \
--enable-shared \
--enable-static \
--enable-bsdtar=static \
--enable-bsdcat=static \
--enable-bsdcpio=static \
--enable-posix-regex-lib \
--disable-maintainer-mode
## make_prepend content
find . -type f -name 'Makefile' -exec sed -i 's:-lbz2\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libbz2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lz\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libz.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-llzma\b:-Wl,--whole-archive,--as-needed,/usr/lib64/liblzma.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lzstd\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libzstd.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lacl\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libacl.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-llz4\b:-Wl,--whole-archive,--as-needed,/usr/lib64/liblz4.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-llzo2\b:-Wl,--whole-archive,--as-needed,/usr/lib64/liblzo2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lxml2\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libxml2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lexpat\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libexpat.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1


%install
export SOURCE_DATE_EPOCH=1620523295
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bsdcat
/usr/bin/bsdcpio
/usr/bin/bsdtar

%files dev
%defattr(-,root,root,-)
/usr/include/archive.h
/usr/include/archive_entry.h
/usr/lib64/libarchive.so
/usr/lib64/pkgconfig/libarchive.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libarchive.so.13
/usr/lib64/libarchive.so.13.5.2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bsdcat.1
/usr/share/man/man1/bsdcpio.1
/usr/share/man/man1/bsdtar.1
/usr/share/man/man3/archive_entry.3
/usr/share/man/man3/archive_entry_acl.3
/usr/share/man/man3/archive_entry_linkify.3
/usr/share/man/man3/archive_entry_misc.3
/usr/share/man/man3/archive_entry_paths.3
/usr/share/man/man3/archive_entry_perms.3
/usr/share/man/man3/archive_entry_stat.3
/usr/share/man/man3/archive_entry_time.3
/usr/share/man/man3/archive_read.3
/usr/share/man/man3/archive_read_add_passphrase.3
/usr/share/man/man3/archive_read_data.3
/usr/share/man/man3/archive_read_disk.3
/usr/share/man/man3/archive_read_extract.3
/usr/share/man/man3/archive_read_filter.3
/usr/share/man/man3/archive_read_format.3
/usr/share/man/man3/archive_read_free.3
/usr/share/man/man3/archive_read_header.3
/usr/share/man/man3/archive_read_new.3
/usr/share/man/man3/archive_read_open.3
/usr/share/man/man3/archive_read_set_options.3
/usr/share/man/man3/archive_util.3
/usr/share/man/man3/archive_write.3
/usr/share/man/man3/archive_write_blocksize.3
/usr/share/man/man3/archive_write_data.3
/usr/share/man/man3/archive_write_disk.3
/usr/share/man/man3/archive_write_filter.3
/usr/share/man/man3/archive_write_finish_entry.3
/usr/share/man/man3/archive_write_format.3
/usr/share/man/man3/archive_write_free.3
/usr/share/man/man3/archive_write_header.3
/usr/share/man/man3/archive_write_new.3
/usr/share/man/man3/archive_write_open.3
/usr/share/man/man3/archive_write_set_options.3
/usr/share/man/man3/archive_write_set_passphrase.3
/usr/share/man/man3/libarchive.3
/usr/share/man/man3/libarchive_changes.3
/usr/share/man/man3/libarchive_internals.3
/usr/share/man/man5/cpio.5
/usr/share/man/man5/libarchive-formats.5
/usr/share/man/man5/mtree.5
/usr/share/man/man5/tar.5

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libarchive.a
