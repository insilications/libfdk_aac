#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libfdk_aac
Version  : 2.0.1
Release  : 9
URL      : file:///insilications/build/clearlinux/packages/libfdk_aac/libfdk_aac-v2.0.1.zip
Source0  : file:///insilications/build/clearlinux/packages/libfdk_aac/libfdk_aac-v2.0.1.zip
Summary  : AAC codec library
Group    : Development/Tools
License  : GPL-2.0
Requires: libfdk_aac-lib = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the libfdk_aac package.
Group: Development
Requires: libfdk_aac-lib = %{version}-%{release}
Provides: libfdk_aac-devel = %{version}-%{release}
Requires: libfdk_aac = %{version}-%{release}

%description dev
dev components for the libfdk_aac package.


%package lib
Summary: lib components for the libfdk_aac package.
Group: Libraries

%description lib
lib components for the libfdk_aac package.


%package staticdev
Summary: staticdev components for the libfdk_aac package.
Group: Default
Requires: libfdk_aac-dev = %{version}-%{release}

%description staticdev
staticdev components for the libfdk_aac package.


%prep
%setup -q -n libfdk_aac-v2.0.1
cd %{_builddir}/libfdk_aac-v2.0.1

%build
## build_prepend content
find . -type f -name 'configure*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name '*.ac' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name '*.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
echo "AM_MAINTAINER_MODE([disable])" >> configure.ac
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595040771
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-common -Wno-error -Wp,-D_REENTRANT
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags1 end
%autogen  --enable-static --enable-shared --disable-maintainer-mode
## make_prepend content
find . -type f -name 'Makefile*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'configure*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name '*.ac' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name '*.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'config.status' -exec touch {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1595040771
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/fdk-aac/FDK_audio.h
/usr/include/fdk-aac/aacdecoder_lib.h
/usr/include/fdk-aac/aacenc_lib.h
/usr/include/fdk-aac/genericStds.h
/usr/include/fdk-aac/machine_type.h
/usr/include/fdk-aac/syslib_channelMapDescr.h
/usr/lib64/pkgconfig/fdk-aac.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfdk-aac.so
/usr/lib64/libfdk-aac.so.2
/usr/lib64/libfdk-aac.so.2.0.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libfdk-aac.a
