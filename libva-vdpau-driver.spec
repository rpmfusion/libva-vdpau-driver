#global preversion .pre4

Name:		libva-vdpau-driver
Version:	0.7.4
Release:	1%{?preversion}%{?dist}
Summary:	HW video decode support for VDPAU platforms
Group:		System Environment/Libraries
License:	GPLv2+
URL:		http://cgit.freedesktop.org/vaapi/vdpau-driver
Source0:        http://www.freedesktop.org/software/vaapi/releases/%{name}/%{name}-%{version}%{?preversion}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildRequires:	libtool
BuildRequires:	libva-devel
BuildRequires:	libvdpau-devel
BuildRequires:	mesa-libGL-devel

#Introduced in F-17
Provides:	vdpau-video-freeworld = %{version}-%{release}
Obsoletes:	vdpau-video-freeworld < %{version}-%{release}

%description
HW video decode support for VDPAU platforms.


%prep
%setup -q -n %{name}-%{version}%{?preversion}

%build
%configure --enable-glx
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_libdir}/dri/*.so

%changelog
* Sun Oct 07 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-1
- Update to 0.7.4

* Mon Jan 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-2
- Rename to libva-vdpau-driver

* Wed Mar 02 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Sun Jan 09 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-0.2.pre4
- Update to 0.7.3 pre4

* Wed Dec 15 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-0.1.pre2
- Update to 0.7.3.pre2
- Switch to vdpau-video-freeworld

* Mon Mar 15 2010 Adam Williamson <adamwill AT shaw.ca> - 0.6.5-1
- new release

* Thu Jan 21 2010 Adam Williamson <adamwill AT shaw.ca> - 0.6.2-1
- new release

* Thu Jan 14 2010 Adam Williamson <adamwill AT shaw.ca> - 0.6.1-1
- new release

* Thu Dec 3 2009 Adam Williamson <adamwill AT shaw.ca> - 0.6.0-1
- new release

* Tue Nov 17 2009 Adam Williamson <adamwill AT shaw.ca> - 0.5.2-1
- new release

* Wed Oct 7 2009 Adam Williamson <adamwill AT shaw.ca> - 0.5.0-1
- new release

* Thu Sep 10 2009 Adam Williamson <adamwill AT shaw.ca> - 0.4.1-1
- new release

* Thu Sep 3 2009 Adam Williamson <adamwill AT shaw.ca> - 0.4.0-1
- initial package
