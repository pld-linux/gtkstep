Summary:	A NEXTSTEP(tm) theme for GTK
Summary(pl.UTF-8):	Motyw NEXTSTEP(tm) dla GTK
Name:		gtkstep
Version:	2.2
Release:	2
License:	GPL
Group:		X11/Libraries
#Source0:	http://ulli.linuxave.net/gtkstep/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	a7c015ae759eee918799c058e241cc8a
#URL:		http://ulli.linuxave.net/gtkstep/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.1.6
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A NEXTSTEP(tm) theme for GTK. It emulates the look and feel of the
NEXTSTEP(tm) GUI.

%description -l pl.UTF-8
Motyw NEXTSTEP(tm) dla GTK. Emuluje wygląd graficznego interfejsu
NEXTSTEP(tm).

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gtk/themes/engines/lib*.so
%{_datadir}/themes/Step
