%define	api	0.4
%define	major	4
%define	libname	%mklibname dbusmenu-glib %{major}
%define	girname	%mklibname dbusmenu-gir %{api}
%define	devname	%mklibname dbusmenu-glib -d

%define	libgtk3	%mklibname dbusmenu-gtk3_ %{major}
%define	libgtk2	%mklibname dbusmenu-gtk2_ %{major}
%define	girgtk3	%mklibname dbusmenu-gtk3-gir %{api}
%define	girgtk2	%mklibname dbusmenu-gtk2-gir %{api}
%define	devgtk3	%mklibname dbusmenu-gtk3 -d
%define	devgtk2	%mklibname dbusmenu-gtk2 -d

%define	libjson	%mklibname dbusmenu-jsonloader %{major}
%define	devjson	%mklibname dbusmenu-jsonloader -d

%define	toolsname	%{name}-tools

Summary:	Library for applications to pass a menu scructure accross DBus
Name:		libdbusmenu
Version:	16.04.0
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
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-glib-1.0) >= 0.13.4
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires: gcc-c++, gcc, gcc-cpp

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

%package -n %{libgtk2}
Summary:	Library for applications to pass a menu structure accross DBus
Group:		System/Libraries

%description -n %{libgtk2}
A small little library that was created by pulling out some comon code
out of indicator-applet. It passes a menu structure across DBus so that
a program can create a menu simply without worrying about how it is
displayed on the other side of the bus.

%files -n %{libgtk2}
%{_libdir}/%{name}-gtk.so.%{major}*

%package -n %{girgtk3}
Summary:	GObject introspection interface description for DBusGtk
Group:		System/Libraries

%description -n %{girgtk3}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n %{girgtk3}
%{_libdir}/girepository-1.0/DbusmenuGtk3-%{api}.typelib

%package -n %{girgtk2}
Summary:	GObject introspection interface description for DBusGtk
Group:		System/Libraries

%description -n %{girgtk2}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n %{girgtk2}
%{_libdir}/girepository-1.0/DbusmenuGtk-%{api}.typelib

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

%package -n %{devgtk2}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{libgtk2} = %{version}-%{release}
Requires:	%{girgtk2} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}
Provides:	%{name}-gtk2-devel = %{version}-%{release}

%description -n %{devgtk2}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n %{devgtk2}
%{_includedir}/libdbusmenu-gtk-%{api}/libdbusmenu-gtk
%{_libdir}/libdbusmenu-gtk.so
%{_libdir}/pkgconfig/dbusmenu-gtk-%{api}.pc
%{_datadir}/gir-1.0/DbusmenuGtk-%{api}.gir
%{_datadir}/vala/vapi/DbusmenuGtk-%{api}.vapi

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
%{_libexecdir}/dbusmenu-testapp
%{_datadir}/%{name}/json/test-gtk-label.json
%{_defaultdocdir}/%{name}/

%prep
%setup -q -c
cp -a %{name}-%{version}/{README,COPYING,COPYING.2.1,COPYING-GPL3,AUTHORS,ChangeLog} .
cp -a %{name}-%{version} %{name}-gtk3-%{version}

%build
build(){
autoreconf -vif
%configure --disable-static --disable-dumper $*
%make
}

pushd %{name}-gtk3-%{version}
sed -i -e 's@^#!.*python$@#!/usr/bin/python2@' tools/dbusmenu-bench
build --with-gtk=3
popd

pushd %{name}-%{version}
sed -i -e 's@^#!.*python$@#!/usr/bin/python2@' tools/dbusmenu-bench
build --with-gtk=2
popd

%install
pushd %{name}-gtk3-%{version}
%make_install
find %{buildroot} -name '*.la' -delete
popd

pushd %{name}-%{version}
%make_install
find %{buildroot} -name '*.la' -delete
popd

