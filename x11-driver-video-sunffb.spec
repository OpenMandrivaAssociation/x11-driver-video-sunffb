Name: x11-driver-video-sunffb
Version: 1.1.0
Release: %mkrel 1
Summary: The X.org driver for sun ffb Cards
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sunffb-%{version}.tar.bz2
Patch0: sunffb-compile_sparc.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for sun ffb Cards


%prep
%setup -q -n xf86-video-sunffb-%{version}
%patch0 -p1 -b .compile_fix

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/sunffb_drv.la
%{_libdir}/xorg/modules/drivers/sunffb_drv.so
%{_mandir}/man4/sunffb.*


