%define		major         4
%define		major_gtk     4
%define		major_json    4
%define		libname       %mklibname dbusmenu-glib %{major}
%define		typelibname   %mklibname dbusmenu-gir 0.4
%define		gtklibname    %mklibname dbusmenu-gtk3_ %{major_gtk}
%define		typelibgtk    %mklibname dbusmenu-gtk3-gir 0.4
%define		jsonname      %mklibname dbusmenu-jsonloader %{major_json}
%define		develname     %mklibname dbusmenu-glib -d
%define		gtkdevelname  %mklibname dbusmenu-gtk -d
%define		jsondevelname %mklibname dbusmenu-jsonloader -d
%define		toolsname     %{name}-tools

Name:		libdbusmenu
Version:	0.6.2
Release:	2
Summary:	Library for applications to pass a menu scructure accross DBus
License:	LGPLv3
Group:		System/Libraries
URL:		https://launchpad.net/dbusmenu
Source0:	http://launchpad.net/dbusmenu/0.6/%{version}/+download/%{name}-%{version}.tar.gz

BuildRequires:	intltool
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-glib-1.0) >= 0.13.4
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	vala-tools
BuildRequires:	pkgconfig(valgrind)
BuildRequires:	pkgconfig(gnome-doc-utils)

%description
A small little library that was created by pulling out some comon code
out of indicator-applet. It passes a menu structure across DBus so that
a program can create a menu simply without worrying about how it is
displayed on the other side of the bus.

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for applications to pass a menu structure accross DBus
Group:		System/Libraries

%description -n %{libname}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n %{libname}
%{_libdir}/%{name}-glib.so.%{major}*

#-----------------------------------------------------------------------

%package -n %{typelibname}
Summary:	GObject introspection interface description for DBus
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{typelibname}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n %{typelibname}
%{_libdir}/girepository-1.0/Dbusmenu-0.4.typelib

#-----------------------------------------------------------------------

%package -n %{gtklibname}
Summary:	Library for applications to pass a menu structure accross DBus
Group:		System/Libraries

%description -n %{gtklibname}
A small little library that was created by pulling out some comon code
out of indicator-applet. It passes a menu structure across DBus so that
a program can create a menu simply without worrying about how it is
displayed on the other side of the bus.

%files -n %{gtklibname}
%{_libdir}/%{name}-gtk3.so.%{major_gtk}*

#-----------------------------------------------------------------------

%package -n %{typelibgtk}
Summary:	GObject introspection interface description for DBusGtk
Group:		System/Libraries
Requires:	%{gtklibname} = %{version}-%{release}

%description -n %{typelibgtk}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n %{typelibgtk}
%{_libdir}/girepository-1.0/DbusmenuGtk3-0.4.typelib

#-----------------------------------------------------------------------

%package -n %{jsonname}
Summary:	Library for applications to pass a menu structure accross DBus
Group:		System/Libraries

%description -n %{jsonname}
A small little library that was created by pulling out some comon code
out of indicator-applet. It passes a menu structure across DBus so that
a program can create a menu simply without worrying about how it is
displayed on the other side of the bus.

%files -n %{jsonname}
%{_libdir}/%{name}-jsonloader.so.%{major_json}*

#-----------------------------------------------------------------------

%package -n %{develname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{typelibname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n %{develname}
%dir %{_includedir}/libdbusmenu-glib-0.4
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib
%{_libdir}/libdbusmenu-glib.so
%{_libdir}/pkgconfig/dbusmenu-glib-0.4.pc
%{_datadir}/gir-1.0/Dbusmenu-0.4.gir
%{_datadir}/vala/vapi/Dbusmenu-0.4.vapi
%doc %{_datadir}/gtk-doc/html/libdbusmenu-glib

#------------------------------------------------------------------------

%package -n %{gtkdevelname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{gtklibname} = %{version}-%{release}
Requires:	%{typelibgtk} = %{version}-%{release}
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-gtk-devel = %{version}-%{release}

%description -n %{gtkdevelname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n %{gtkdevelname}
%{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk
%{_libdir}/libdbusmenu-gtk3.so
%{_libdir}/pkgconfig/dbusmenu-gtk3-0.4.pc
%{_datadir}/gir-1.0/DbusmenuGtk3-0.4.gir
%{_datadir}/vala/vapi/DbusmenuGtk3-0.4.vapi
%doc %{_datadir}/gtk-doc/html/libdbusmenu-gtk

#-----------------------------------------------------------------------

%package -n %{jsondevelname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{jsonname} = %{version}-%{release}
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-jsonloader-devel = %{version}-%{release}

%description -n %{jsondevelname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n %{jsondevelname}
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-jsonloader
%{_libdir}/libdbusmenu-jsonloader.so
%{_libdir}/pkgconfig/dbusmenu-jsonloader-0.4.pc

#-----------------------------------------------------------------------

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

#-----------------------------------------------------------------------

%prep
%setup -q

%build
CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
%configure2_5x --disable-static --enable-gtk-doc-html
%make

%install
%makeinstall_std

%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6.2-1
+ Revision: 810802
- BR: pkgconfig(gnome-doc-utils)
- version update 0.6.2

* Mon Jan 23 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.5.1-3
+ Revision: 767380
- dropped configure2_5x for configure macro
- added autoreconf
- fix linking
- rebuild
- removed .la files
- cleaned up spec

* Tue Nov 01 2011 Frank Kober <emuse@mandriva.org> 0.5.1-2
+ Revision: 709289
- Patch added to fix build against gtk-3 (deprecated hbox usage)
- rebuild

* Mon Oct 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.5.1-1
+ Revision: 708065
- new version 0.5.1
  copied chagnes from mga spec

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.16-2
+ Revision: 660233
- mass rebuild

* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 0.3.16-1mdv2011.0
+ Revision: 593656
- new version 0.3.16
- disable gir building (it is failing)
- rebuild for new gir

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.3.8-2mdv2011.0
+ Revision: 564207
- rebuild
- drop unused patch
- New version 0.3.8

  + Emmanuel Andry <eandry@mandriva.org>
    - New version 0.2.9
    - BR vala-tools
    - update files list

* Sat Mar 13 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.2.6-1mdv2010.1
+ Revision: 518768
- Clean up of the spec file

  + John Balcaen <mikala@mandriva.org>
    - import libdbusmenu

