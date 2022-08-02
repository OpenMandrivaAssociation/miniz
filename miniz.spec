%global upstream richgel999
%global gitbase  https://github.com

%define major 2
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary: A zlib replacement library
Name:    miniz
Version: 2.2.0
Release: %mkrel 2
License: MIT
Group:   System/Libraries
URL:     %{gitbase}/%{upstream}/%{name}
Source0: %{gitbase}/%{upstream}/%{name}/archive/refs/tags/%{version}.tar.gz
Patch0:  miniz.pc.in-fix-include-path-not-containing-the-mini.patch

BuildRequires: cmake

%description
Miniz is a lossless, high performance data compression library in a single source file
that implements the zlib (RFC 1950) and Deflate (RFC 1951)
compressed data format specification standards.
It supports the most commonly used functions exported by the zlib library,
but is a completely independent implementation so zlib's licensing requirements do not apply.
Miniz also contains simple to use functions for writing .PNG format image files
and reading/writing/appending .ZIP format archives.
Miniz's compression speed has been tuned to be comparable to zlib's,
and it also has a specialized real-time compressor function
designed to compare well against fastlz/minilzo.

%package -n %{libname}
Summary:  %{summary}
Group:    %{group}
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the %{name} runtime libraries.

%package -n %{devname}
Summary:  %{summary}
Group:    %{group}
Requires: %{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the %{name} development headers and libraries.

%prep
%autosetup -p 1 -n %{name}-%{version}

%build
%cmake -DBUILD_EXAMPLES=OFF   \
       -DBUILD_SHARED_LIBS=ON

%make_build

%install
%make_install -C build

sed -i '/#include/s/"miniz.h"/<miniz.h>/g' examples/*

mv %{buildroot}%{_datadir}/pkgconfig %{buildroot}%{_libdir}/

%files -n %{libname}
%{_libdir}/lib%{name}*.so.%{major}*

%files -n %{devname}
%doc ChangeLog.md readme.md examples
%license LICENSE
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}*
