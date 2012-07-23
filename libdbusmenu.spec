%define         major         4
%define         major_gtk     4
%define         major_json    4
%define         libname       %mklibname dbusmenu-glib %{major}
%define         typelibname   %mklibname dbusmenu-gir 0.4
%define         gtklibname    %mklibname dbusmenu-gtk3_ %{major_gtk}
%define         typelibgtk    %mklibname dbusmenu-gtk3-gir 0.4
%define         jsonname      %mklibname dbusmenu-jsonloader %{major_json}
%define         develname     %mklibname dbusmenu-glib -d
%define         gtkdevelname  %mklibname dbusmenu-gtk -d
%define         jsondevelname %mklibname dbusmenu-jsonloader -d
%define         toolsname     %{name}-tools

Name:           libdbusmenu
Version:        0.6.2
Release:        1
Summary:        Library for applications to pass a menu scructure accross DBus
License:        LGPLv3
Group:          System/Libraries
URL:            https://launchpad.net/dbusmenu
Source0:        http://launchpad.net/dbusmenu/0.6/%{version}/+download/%{name}-%{version}.tar.gz

BuildRequires:  intltool
BuildRequires:  libxml2-devel
BuildRequires:  dbus-glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:  gtk+3-devel
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.13.4
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala-tools
BuildRequires:	pkgconfig(valgrind)
BuildRequires:  gnome-doc-utils

%description
A small little library that was created by pulling out some comon code
out of indicator-applet. It passes a menu structure across DBus so that
a program can create a menu simply without worrying about how it is
displayed on the other side of the bus.

#-----------------------------------------------------------------------

%package -n     %{libname}
Summary:        Library for applications to pass a menu structure accross DBus
Group:          System/Libraries

%description -n	%{libname}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n       %{libname}
%{_libdir}/%{name}-glib.so.%{major}*

#-----------------------------------------------------------------------

%package -n	%{typelibname}
Summary:	GObject introspection interface description for DBus
Group:		System/Libraries
Requires:	%{libname} = %{version}

%description -n %{typelibname}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n	%{typelibname}
%{_libdir}/girepository-1.0/Dbusmenu-0.4.typelib

#-----------------------------------------------------------------------

%package -n     %{gtklibname}
Summary:        Library for applications to pass a menu structure accross DBus
Group:          System/Libraries

%description -n %{gtklibname}
A small little library that was created by pulling out some comon code
out of indicator-applet. It passes a menu structure across DBus so that
a program can create a menu simply without worrying about how it is
displayed on the other side of the bus.

%files -n       %{gtklibname}
%{_libdir}/%{name}-gtk3.so.%{major_gtk}*

#-----------------------------------------------------------------------

%package -n	%{typelibgtk}
Summary:	GObject introspection interface description for DBusGtk
Group:		System/Libraries
Requires:	%{gtklibname} = %{version}

%description -n %{typelibgtk}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n	%{typelibgtk}
%{_libdir}/girepository-1.0/DbusmenuGtk3-0.4.typelib

#-----------------------------------------------------------------------

%package -n     %{jsonname}
Summary:        Library for applications to pass a menu structure accross DBus
Group:          System/Libraries

%description -n %{jsonname}
A small little library that was created by pulling out some comon code
out of indicator-applet. It passes a menu structure across DBus so that
a program can create a menu simply without worrying about how it is
displayed on the other side of the bus.

%files -n       %{jsonname}
%{_libdir}/%{name}-jsonloader.so.%{major_json}*

#-----------------------------------------------------------------------

%package -n     %{develname}
Summary:        Library headers for %{name}
Group:          Development/C 
Requires:       %{libname} = %{version}
Requires:	%{typelibname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n       %{develname}
%dir %{_includedir}/libdbusmenu-glib-0.4
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib
%{_libdir}/libdbusmenu-glib.so
%{_libdir}/pkgconfig/dbusmenu-glib-0.4.pc
%{_datadir}/gir-1.0/Dbusmenu-0.4.gir
%{_datadir}/vala/vapi/Dbusmenu-0.4.vapi
%doc %{_datadir}/gtk-doc/html/libdbusmenu-glib

#------------------------------------------------------------------------

%package -n     %{gtkdevelname}
Summary:        Library headers for %{name}
Group:          Development/C
Requires:       %{gtklibname} = %{version}
Requires:	%{typelibgtk} = %{version}
Requires:       %{develname} = %{version}
Provides:       %{name}-gtk-devel = %{version}-%{release}

%description -n %{gtkdevelname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n       %{gtkdevelname}
%{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk
%{_libdir}/libdbusmenu-gtk3.so
%{_libdir}/pkgconfig/dbusmenu-gtk3-0.4.pc
%{_datadir}/gir-1.0/DbusmenuGtk3-0.4.gir
%{_datadir}/vala/vapi/DbusmenuGtk3-0.4.vapi
%doc %{_datadir}/gtk-doc/html/libdbusmenu-gtk
 
#-----------------------------------------------------------------------

%package -n     %{jsondevelname}
Summary:        Library headers for %{name}
Group:          Development/C
Requires:       %{jsonname} = %{version}
Requires:       %{develname} = %{version}-%{release}
Provides:       %{name}-jsonloader-devel = %{version}-%{release}

%description -n %{jsondevelname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n       %{jsondevelname}
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-jsonloader
%{_libdir}/libdbusmenu-jsonloader.so
%{_libdir}/pkgconfig/dbusmenu-jsonloader-0.4.pc

#-----------------------------------------------------------------------

%package -n %{toolsname}
Summary:        Tools useful when building applications
Group:          Development/C
%description -n %{toolsname}
This package contains tools that are useful when building applications. 

%files -n %{toolsname}
%{_libexecdir}/dbusmenu-bench
%{_libexecdir}/dbusmenu-dumper
%{_libexecdir}/dbusmenu-testapp
%{_datadir}/%{name}/json/test-gtk-label.json
%{_defaultdocdir}/%{name}/

#-----------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static --enable-gtk-doc-html
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la
