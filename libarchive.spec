#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libarchive
Version  : 3.5.2
Release  : 302
URL      : file:///aot/build/clearlinux/packages/libarchive/libarchive-v3.5.2.tar.gz
Source0  : file:///aot/build/clearlinux/packages/libarchive/libarchive-v3.5.2.tar.gz
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
BuildRequires : lrzip
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
export SOURCE_DATE_EPOCH=1630156720
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage -fprofile-partial-training -fprofile-correction -freorder-functions --coverage -lgcov"
export CFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FCFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export CXXFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LDFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LIBS="-lgcov"
## pgo use
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export PGO_USE="-Wmissing-profile -Wcoverage-mismatch -fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-partial-training -fprofile-correction -freorder-functions"
export CFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
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
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags_pgo end
sd -r '\s--dirty\s' ' ' .
sd -r 'git describe' 'git describe --abbrev=0' .
sd --flags mi '^AC_INIT\((.*\n.*\)|.*\))' '$0\nAM_MAINTAINER_MODE([disable])' configure.ac
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%reconfigure  --with-acl \
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
find . -type f -name 'Makefile' -exec sed -i 's:-lbz2\b:-Wl,--whole-archive,/usr/lib64/libbz2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lz\b:-Wl,--whole-archive,/usr/lib64/libz.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-llzma\b:-Wl,--whole-archive,/usr/lib64/liblzma.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lzstd\b:-Wl,--whole-archive,/usr/lib64/libzstd.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lacl\b:-Wl,--whole-archive,/usr/lib64/libacl.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-llz4\b:-Wl,--whole-archive,/usr/lib64/liblz4.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-llzo2\b:-Wl,--whole-archive,/usr/lib64/liblzo2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lxml2\b:-Wl,--whole-archive,/usr/lib64/libxml2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lexpat\b:-Wl,--whole-archive,/usr/lib64/libexpat.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lcrypto\b:-Wl,--whole-archive,/usr/lib64/libcrypto.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lssl\b:-Wl,--whole-archive,/usr/lib64/libssl.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
## make_prepend end
make  %{?_smp_mflags}   V=1 VERBOSE=1 V=1 VERBOSE=1

## profile_payload start
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
make VERBOSE=1 V=1 -j1 check || :
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
## profile_payload end
make clean || :
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%reconfigure  --with-acl \
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
find . -type f -name 'Makefile' -exec sed -i 's:-lbz2\b:-Wl,--whole-archive,/usr/lib64/libbz2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lz\b:-Wl,--whole-archive,/usr/lib64/libz.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-llzma\b:-Wl,--whole-archive,/usr/lib64/liblzma.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lzstd\b:-Wl,--whole-archive,/usr/lib64/libzstd.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lacl\b:-Wl,--whole-archive,/usr/lib64/libacl.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-llz4\b:-Wl,--whole-archive,/usr/lib64/liblz4.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-llzo2\b:-Wl,--whole-archive,/usr/lib64/liblzo2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lxml2\b:-Wl,--whole-archive,/usr/lib64/libxml2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lexpat\b:-Wl,--whole-archive,/usr/lib64/libexpat.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lcrypto\b:-Wl,--whole-archive,/usr/lib64/libcrypto.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
find . -type f -name 'Makefile' -exec sed -i 's:-lssl\b:-Wl,--whole-archive,/usr/lib64/libssl.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
## make_prepend end
make  %{?_smp_mflags}   V=1 VERBOSE=1 V=1 VERBOSE=1
fi


%install
export SOURCE_DATE_EPOCH=1630156720
rm -rf %{buildroot}
%make_install
## install_append content
install -dm 0755 %{buildroot}/usr/lib64/haswell/ || :
cp --archive %{buildroot}/usr/lib64/lib*.so* %{buildroot}/usr/lib64/haswell/ || :
## install_append end

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
/usr/lib64/haswell/libarchive.so
/usr/lib64/libarchive.so
/usr/lib64/pkgconfig/libarchive.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libarchive.so.13
/usr/lib64/haswell/libarchive.so.13.5.3
/usr/lib64/libarchive.so.13
/usr/lib64/libarchive.so.13.5.3

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
