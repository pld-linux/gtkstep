%define ver	1.5
Summary:	A NEXTSTEP(tm) theme for GTK.
Name:		gtkstep
Version:	%{ver}
Release:	1
Copyright:	GPL
Source:		ftp://sunshine.informatik.uni-wuerzburg.de/pub/wmaker/gtkstep/gtkstep-%{ver}.tar.gz
BuildRoot:	/tmp/gtkstep-%{PACKAGE_VERSION}-root
Group:		X11/Libraries
Packager:	Ullrich Hafner <hafner@bigfoot.de>
Requires:	gtk+ >= 1.1.15
Icon:		gtkstep.xpm

%description
A NEXTSTEP(tm) theme for GTK. It emulates the look and feel of the
NEXTSTEP(tm) GUI.

%prep
%setup
%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0644,root,root) /usr/lib/gtk/themes/engines/libstep.la
%attr(0644,root,root) /usr/lib/gtk/themes/engines/libstep.so
%attr(0644,root,root) /usr/lib/gtk/themes/engines/libstep.so.0
%attr(0644,root,root) /usr/lib/gtk/themes/engines/libstep.so.0.0.0
%attr(-,root,root) /usr/share/themes/Step/ICON.png
%attr(-,root,root) /usr/share/themes/Step/README.html
%attr(-,root,root) /usr/share/themes/Step/gtk/gtkrc
%doc AUTHORS COPYING ChangeLog NEWS README

%changelog

* Wed Mar 17 1999 Ullrich Hafner <hafner@bigfoot.de>

- update to GTKstep 1.5

* Tue Feb 16 1999 Oliver Graf <ograf@fga.de>

- fixed prefix handling for configure and make install
- Updated to GTKstep 1.4.

* Tue Feb 2 1999 Tom Palmer <tmp1@dcs.qmw.ac.uk>

- Updated to GTKstep 1.3.

* Thu Jan 28 1999 Tom Palmer <tmp1@dcs.qmw.ac.uk>

- First go at an RPM file.
