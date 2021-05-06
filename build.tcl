#!/usr/bin/tclsh

set arch "x86_64"
set base "tclsignal-1.4.4"
set fileurl "https://github.com/wjoye/tclsignal/archive/refs/tags/v1.4.4.tar.gz"

set var [list wget $fileurl -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force signal_ext.c.patch build/SOURCES
file copy -force Makefile.in.patch build/SOURCES
file copy -force configure.ac.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tcl-signal.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
#file delete $base.tar.gz
