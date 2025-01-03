Name:       libpciaccess
Summary:    PCI access library
Version:    0.18.1
Release:    1
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
Patch0:     libpciaccess-no-root.patch
BuildRequires: meson
Requires:   hwdata
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Generic PCI access library

%package devel
Summary:    PCI access library development package
Requires:   %{name} = %{version}-%{release}

%description devel
Generic PCI access library development package

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson -Dzlib=disabled
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libpciaccess.so.0*

%files devel
%{_includedir}/pciaccess.h
%{_libdir}/libpciaccess.so
%{_libdir}/pkgconfig/pciaccess.pc
