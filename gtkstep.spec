Summary:	A NEXTSTEP(tm) theme for GTK.
Summary(pl):	Temat NEXTSTEP(tm) dla GTK.
Name:		gtkstep
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	http://ulli.linuxave.net/gtkstep/%{name}-%{version}.tar.bz2
Icon:		gtkstep.xpm
URL:		http://ulli.linuxave.net/gtkstep/
BuildRequires:	gtk+-devel >= 1.1.6
BuildRequires:	glib-devel >= 1.1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A NEXTSTEP(tm) theme for GTK. It emulates the look and feel of the
NEXTSTEP(tm) GUI.

%description -l pl

Temat NEXTSTEP(tm) dla GTK. Emuluje wygl±d graficznego interfejsu
NEXTSTEP(tm).

%prep
%setup -q

%build
export LDFLAGS="-s"
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines/lib*.so

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_libdir}/gtk/themes/engines/lib*.so
%attr(755,root,root) %{_libdir}/gtk/themes/engines/lib*.la

%{_datadir}/themes/Step
