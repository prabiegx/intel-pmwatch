Name:           intel-pmwatch
Version:        0
Release:        1%{?dist}
Summary:        Intel PMWatch(PersistentMemoryWatch) tool

License:        MIT
URL:            https://github.com/intel/intel-pmwatch
Source0:        https://github.com/intel/intel-pmwatch/archive/ef5432874a56c11b4ca4ed60b6b458eeb813604f.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  gcc
BuildRequires:  libipmctl-devel

%description
Intel PMWatch (PersistentMemoryWatch) is a tool that monitors and reports the performance
and health information metrics of the Intel Optane DC Persistent Memory.


%package -n intel-pmwatch-devel
Summary: Developement files to build against intel-pmwatch

Provides: intel-pmwatch-static = %{version}-%{release}

Requires: intel-pmwatch = %{version}-%{release}

%description -n intel-pmwatch-devel
description


%prep
%autosetup -n %{name}-ef5432874a56c11b4ca4ed60b6b458eeb813604f
./autogen.sh
./configure --libdir=/usr/lib64

%build
make

%install
%make_install

%files
%license COPYING
%doc README.md
/usr/lib64/libpmwapi.so
/usr/lib64/libpmwapi.so.0
/usr/lib64/libpmwapi.so.0.0.0
/usr/lib64/libpmwcollect.so
/usr/lib64/libpmwcollect.so.0
/usr/lib64/libpmwcollect.so.0.0.0
/usr/local/bin/pmwatch
/usr/local/bin/pmwatch-stop


%files -n intel-pmwatch-devel
/usr/lib64/libpmwapi.a
/usr/lib64/libpmwapi.la
/usr/lib64/libpmwcollect.a
/usr/lib64/libpmwcollect.la
/usr/local/include/pmw_api.h
/usr/local/include/pmw_struct.h

%changelog
* Mon Mar 09 2020 Piotr Rabiega <piotrx.rabiega@intel.com> - 1-1
- initial packaging
