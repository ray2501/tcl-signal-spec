#
# spec file for package tcl-signal
#

%define pkgname tclsignal

Name:           tcl-signal
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  tcl-devel
Url:            https://github.com/wjoye/tclsignal
Summary:        Signal extension for Tcl
License:        MIT
Group:          Development/Libraries/Tcl
Version:        1.4.4
Release:        0
Source0:        %{pkgname}-%{version}.tar.gz
Patch0:         signal_ext.c.patch
Patch1:         Makefile.in.patch
Patch2:         configure.ac.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This extension adds dynamically loadable signal handling to Tcl/Tk scripts.
It provides a very limited subset of the functionality of tclX (just the signal
part, and about 3/4 of the functions for signals), but as a result is quite
small and quick to load.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0
%patch1
%patch2

%build
autoconf
%configure \
        --libdir=%tcl_archdir \
        --with-tcl=%_libdir
make

%install
make DESTDIR=%buildroot pkglibdir=%tcl_archdir/%pkgname%version install

%files
%defattr(-,root,root,-)
%tcl_archdir/*

%changelog

