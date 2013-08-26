%define	api	0.4
%define	major	4
%define	libname	%mklibname dbusmenu-glib %{major}
%define	girname	%mklibname dbusmenu-gir %{api}
%define	devname     %mklibname dbusmenu-glib -d

%define	libgtk3	%mklibname dbusmenu-gtk3_ %{major}
%define	girgtk3	%mklibname dbusmenu-gtk3-gir %{api}
%define	devgtk3  %mklibname dbusmenu-gtk -d

%define	libjson      %mklibname dbusmenu-jsonloader %{major}
%define	devjson %mklibname dbusmenu-jsonloader -d

%define	toolsname     %{name}-tools

Summary:	Library for applications to pass a menu scructure accross DBus
Name:		libdbusmenu
Version:	0.6.2
Release:	3
License:	LGPLv3
Group:		System/Libraries
Url:		https://launchpad.net/dbusmenu
Source0:	http://launchpad.net/dbusmenu/0.6/%{version}/+download/%{name}-%{version}.tar.gz

BuildRequires:	intltool
BuildRequires:	vala-tools
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-glib-1.0) >= 0.13.4
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(valgrind)

%description
A small little library that was created by pulling out some comon code
out of indicator-applet. It passes a menu structure across DBus so that
a program can create a menu simply without worrying about how it is
displayed on the other side of the bus.

%package -n %{libname}
Summary:	Library for applications to pass a menu structure accross DBus
Group:		System/Libraries

%description -n %{libname}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n %{libname}
%{_libdir}/%{name}-glib.so.%{major}*

%package -n %{girname}
Summary:	GObject introspection interface description for DBus
Group:		System/Libraries

%description -n %{girname}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n %{girname}
%{_libdir}/girepository-1.0/Dbusmenu-%{api}.typelib

%package -n %{libgtk3}
Summary:	Library for applications to pass a menu structure accross DBus
Group:		System/Libraries

%description -n %{libgtk3}
A small little library that was created by pulling out some comon code
out of indicator-applet. It passes a menu structure across DBus so that
a program can create a menu simply without worrying about how it is
displayed on the other side of the bus.

%files -n %{libgtk3}
%{_libdir}/%{name}-gtk3.so.%{major}*

%package -n %{girgtk3}
Summary:	GObject introspection interface description for DBusGtk
Group:		System/Libraries

%description -n %{girgtk3}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n %{girgtk3}
%{_libdir}/girepository-1.0/DbusmenuGtk3-%{api}.typelib

%package -n %{libjson}
Summary:	Library for applications to pass a menu structure accross DBus
Group:		System/Libraries

%description -n %{libjson}
A small little library that was created by pulling out some comon code
out of indicator-applet. It passes a menu structure across DBus so that
a program can create a menu simply without worrying about how it is
displayed on the other side of the bus.

%files -n %{libjson}
%{_libdir}/%{name}-jsonloader.so.%{major}*

%package -n %{devname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n %{devname}
%dir %{_includedir}/libdbusmenu-glib-%{api}
%{_includedir}/libdbusmenu-glib-%{api}/libdbusmenu-glib
%{_libdir}/libdbusmenu-glib.so
%{_libdir}/pkgconfig/dbusmenu-glib-%{api}.pc
%{_datadir}/gir-1.0/Dbusmenu-%{api}.gir
%{_datadir}/vala/vapi/Dbusmenu-%{api}.vapi
%doc %{_datadir}/gtk-doc/html/libdbusmenu-glib

%package -n %{devgtk3}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{libgtk3} = %{version}-%{release}
Requires:	%{girgtk3} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}
Provides:	%{name}-gtk-devel = %{version}-%{release}

%description -n %{devgtk3}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n %{devgtk3}
%{_includedir}/libdbusmenu-gtk3-%{api}/libdbusmenu-gtk
%{_libdir}/libdbusmenu-gtk3.so
%{_libdir}/pkgconfig/dbusmenu-gtk3-%{api}.pc
%{_datadir}/gir-1.0/DbusmenuGtk3-%{api}.gir
%{_datadir}/vala/vapi/DbusmenuGtk3-%{api}.vapi
%doc %{_datadir}/gtk-doc/html/libdbusmenu-gtk

%package -n %{devjson}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{libjson} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}
Provides:	%{name}-jsonloader-devel = %{version}-%{release}

%description -n %{devjson}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n %{devjson}
%{_includedir}/libdbusmenu-glib-%{api}/libdbusmenu-jsonloader
%{_libdir}/libdbusmenu-jsonloader.so
%{_libdir}/pkgconfig/dbusmenu-jsonloader-%{api}.pc

%package -n %{toolsname}
Summary:	Tools useful when building applications
Group:		Development/C

%description -n %{toolsname}
This package contains tools that are useful when building applications. 

%files -n %{toolsname}
%{_libexecdir}/dbusmenu-bench
%{_libexecdir}/dbusmenu-dumper
%{_libexecdir}/dbusmenu-testapp
%{_datadir}/%{name}/json/test-gtk-label.json
%{_defaultdocdir}/%{name}/

%prep
%setup -q

%build
CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
%configure2_5x \
	--disable-static \
	--enable-gtk-doc-html
%make

%install
%makeinstall_std

