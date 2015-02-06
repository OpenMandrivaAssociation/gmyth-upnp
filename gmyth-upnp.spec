%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	UPNP plugin for gmyth
Name:		gmyth-upnp
Version:	0.7.1
Release:	3
# COPYING file states GPL but all source indicates LGPL.
# http://sourceforge.net/tracker/index.php?func=detail&aid=1790620&group_id=177106&atid=879914
License:	LGPLv2+
Group:		System/Libraries
URL:		http://gmyth.sf.net
Source0:	http://download.sourceforge.net/gmyth/%{name}-%{version}.tar.gz
Patch0:		gmyth-upnp-0.7.1-fix-dso-linkage.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmyth)
BuildRequires:	pkgconfig(libupnp)

%description
GMyth is a library used by applications to access content provided by the
MythTV set-top box framework, such as Live TV broadcasts, TV recordings, or
TV listings.

This package provides a plugin for autodetecting Myth backends via UPNP

%package -n %{libname}
Summary:	Library files for MythTV backend detection via UPNP
Group:		System/Libraries

%description -n %{libname}
A plugin for libgmyth to autodetect Myth backends via UPNP

%package -n %{devname}
Summary:	Development libraries for GMyth-UPNP
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development libraries and headers for the GMyth-UPNP library.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
rm -f %{buildroot}/%{_bindir}/test

%files -n %{libname}
%{_libdir}/libgmythupnp.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/libgmythupnp.so
%{_libdir}/pkgconfig/*.pc

