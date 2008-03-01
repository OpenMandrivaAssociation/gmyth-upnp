%define name gmyth-upnp
%define version 0.7
%define rel %mkrel 1

%define major 0
%define libname %mklibname %{name} %{major}
%define libname_devel %mklibname -d %{name}

Summary: UPNP plugin for gmyth
Name: %{name}
Version: %version
Release: %rel
# COPYING file states GPL but all source indicates LGPL.
# http://sourceforge.net/tracker/index.php?func=detail&aid=1790620&group_id=177106&atid=879914
License: LGPLv2+
Group: System/Libraries
Source0: http://downloads.sourceforge.net/%{name}/%{name}_%{version}-indt1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://gmyth.sf.net
BuildRequires: glib2-devel
BuildRequires: gmyth-devel
BuildRequires: libupnp-devel

%description
GMyth is a library used by applications to access content provided by the
MythTV set-top box framework, such as Live TV broadcasts, TV recordings, or
TV listings.

This package provides a plugin for autodetecting Myth backends via UPNP

%package -n %{libname}
Summary: Library files for MythTV backend detection via UPNP
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description -n %{libname}
A plugin for libgmyth to autodetect Myth backends via UPNP

%package -n %{libname_devel}
Summary: Development libraries for GMyth-UPNP
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{libname_devel}
Development libraries and headers for the GMyth-UPNP library.

%prep
%setup -q -n %{name}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/*.a
rm -f %{buildroot}/%{_bindir}/test

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libgmythupnp.so.%{major}*

%files -n %{libname_devel}
%defattr(-,root,root)
%{_includedir}/gmyth_upnp.h
%{_libdir}/libgmythupnp.so
%{_libdir}/pkgconfig/*.pc
