%define name libdbusmenu
%define version 0.2.6
%define release %mkrel 1
%define summary Library for applications to pass a menu scructure accross DBus
%define major 1
%define major_gtk 1
%define libname %mklibname dbusmenu-glib %{major}
%define gtklibname  %mklibname dbusmenu-gtk %{major_gtk}
%define develname %mklibname dbusmenu-glib -d
%define gtkdevelname %mklibname dbusmenu-gtk -d

Summary:	%summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://launchpad.net/dbusmenu/0.2/%{version}/+download/%{name}-%{version}.tar.gz
License:	LGPLv3
Group:		System/Libraries
URL:		https://launchpad.net/dbusmenu
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	intltool
BuildRequires:	libxml2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libjson-glib-devel

%description
A small little library that was created by pulling out some comon code
out of indicator-applet. It passes a menu structure across DBus so that
a program can create a menu simply without worrying about how it is
displayed on the other side of the bus.

%package -n	%{libname}
Summary:	Library for applications to pass a menu scructure accross DBus
Group:		System/Libraries
%description -n	%{libname}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n	%{libname}
%defattr(-,root,root)
%{_libdir}/%{name}-glib.so.%{major}*


#-----------------------------------------------------------------------

%package -n	%{gtklibname}
Summary:	Library for applications to pass a menu scructure accross DBus
Group:		System/Libraries
%description -n	%{gtklibname}
A small little library that was created by pulling out some comon code
out of indicator-applet. It passes a menu structure across DBus so that
a program can create a menu simply without worrying about how it is
displayed on the other side of the bus.

%files -n	%{gtklibname}
%defattr(-,root,root)
%{_libdir}/%{name}-gtk.so.%{major_gtk}*


#-----------------------------------------------------------------------

%package -n	%{develname}
Summary:	Library headers for %{name}
Group:		Development/C 
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
%description -n	%{develname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n	%{develname}
%defattr(-,root,root)
%{_includedir}/libdbusmenu-0.1/libdbusmenu-glib/
%{_libdir}/libdbusmenu-glib.*
%{_libdir}/pkgconfig/dbusmenu-glib.pc


#------------------------------------------------------------------------

%package -n     %{gtkdevelname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{gtklibname} = %{version}
Requires:	%{develname} = %{version}
Provides:	%{name}-gtk-devel = %{version}-%{release}


%description -n %{gtkdevelname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n       %{gtkdevelname}
%defattr(-,root,root)
%{_includedir}/libdbusmenu-0.1/libdbusmenu-gtk/
%{_libdir}/libdbusmenu-gtk.*
%{_libdir}/pkgconfig/dbusmenu-gtk.pc

%package tools
Summary:	Tools useful when building applications
Group:		Development/C
%description tools
This package contains tools that are useful when building applications. 

%files tools
%defattr(-,root,root)
%{_libdir}/dbusmenu-bench
%{_libdir}/dbusmenu-dumper
%{_libdir}/dbusmenu-testapp
%{_datadir}/%{name}/json/test-gtk-label.json
%{_defaultdocdir}/%{name}/

#-----------------------------------------------------------------------

%prep
%setup -q 


%build
%configure2_5x 
%make

%install
%__rm -rf %{buildroot}
%makeinstall


%clean
%__rm -rf %{buildroot}
