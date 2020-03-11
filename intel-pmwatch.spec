Name:           intel-pmwatch
Version:        3.2.0
Release:        1%{?dist}
Summary:        Intel PMWatch(PersistentMemoryWatch) tool

License:        MIT
URL:            https://github.com/intel/intel-pmwatch
Source0:        https://github.com/intel/intel-pmwatch/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  gcc
BuildRequires:  libipmctl-devel
BuildRequires:  make

%description
Intel PMWatch (PersistentMemoryWatch) is a tool that monitors and reports
the performance and health information metrics of the Intel Optane DC
Persistent Memory.


%package -n intel-pmwatch-devel
Summary: Development files to build against intel-pmwatch

Requires: intel-pmwatch = %{version}-%{release}

%description -n intel-pmwatch-devel
%{summary}


%prep
%autosetup -n %{name}-%{version}
./autogen.sh
./configure --libdir=%{_libdir} --bindir=%{_bindir} --includedir=%{_includedir}

%build
chmod -x README.md 
make

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%license COPYING
%doc README.md
%{_libdir}/libpmwapi.so.0
%{_libdir}/libpmwapi.so.0.0.0
%{_libdir}/libpmwcollect.so.0
%{_libdir}/libpmwcollect.so.0.0.0
%{_bindir}/pmwatch
%{_bindir}/pmwatch-stop

%files -n intel-pmwatch-devel
%{_libdir}/libpmwapi.a
%{_libdir}/libpmwapi.la
%{_libdir}/libpmwapi.so
%{_libdir}/libpmwcollect.so
%{_libdir}/libpmwcollect.a
%{_libdir}/libpmwcollect.la
%{_includedir}/pmw_api.h
%{_includedir}/pmw_struct.h


%changelog
* Wed Mar 11 2020 Piotr Rabiega <piotrx.rabiega@intel.com> - 3.2.0-1
- initial packaging
