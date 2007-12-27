ExclusiveArch:	sparc sparc64
Name: x11-driver-video-sunffb
Version: 1.1.0
Release: %mkrel 4
Summary: The X.org driver for sun ffb Cards
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-video-sunffb-1.1.0@mandriva suggested on upstream
# Tag at git checkout 5c1e059cfed608b1f051cc8825c1243db76e8995
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-sunffb  xorg/drivers/xf86-video-sunffb
# cd xorg/drivers/xf86-video/sunffb
# git-archive --format=tar --prefix=xf86-video-sunffb-1.1.0/ xf86-video-sunffb-1.1.0@mandriva | bzip2 -9 > xf86-video-sunffb-1.1.0.tar.bz2
########################################################################
Source0: xf86-video-sunffb-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-sunffb-1.1.0@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
BuildRequires: GL-devel
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for sun ffb Cards

%package devel
Summary: Development files for %{name}
Group: Development/X11
License: MIT

%description devel
Development files for %{name}

%prep
%setup -q -n xf86-video-sunffb-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# Create list of dependencies
x-check-deps.pl
for deps in *.deps; do
    install -D -m 644 $deps %{buildroot}/%{_datadir}/X11/mandriva/$deps
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/sunffb_drv.so
%{_mandir}/man4/sunffb.*

%files devel
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/*.la
%{_datadir}/X11/mandriva/*.deps
