Summary:	A NEXTSTEP(tm) theme for GTK
Summary(pl):	Temat NEXTSTEP(tm) dla GTK
Name:		gtkstep
Version:	2.2
Release:	2
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/����������
Group(uk):	X11/��̦�����
Source0:	http://ulli.linuxave.net/gtkstep/%{name}-%{version}.tar.bz2
Icon:		gtkstep.xpm
URL:		http://ulli.linuxave.net/gtkstep/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.1.6
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A NEXTSTEP(tm) theme for GTK. It emulates the look and feel of the
NEXTSTEP(tm) GUI.

%description -l pl
Temat NEXTSTEP(tm) dla GTK. Emuluje wygl�d graficznego interfejsu
NEXTSTEP(tm).

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/gtk/themes/engines/lib*.so
%{_datadir}/themes/Step
