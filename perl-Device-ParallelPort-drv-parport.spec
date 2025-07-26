#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	Device
%define		pnam	ParallelPort-drv-parport
Summary:	Device::ParallelPort - driver that uses direct I/O access
Summary(pl.UTF-8):	Device::ParallelPort - sterownik używający bezpośredniego wejścia/wyjścia
Name:		perl-Device-ParallelPort-drv-parport
Version:	1.0
Release:	20
# same as perl (?)
# README says it is Artistic only, LICENSE says it is LGPL or Artistic
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	901987e4a37bfe2d7241530bda05f36e
URL:		http://search.cpan.org/dist/Device-ParallelPort-drv-parport/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Device-ParallelPort
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Device::ParallelPort driver that uses direct I/O access on
Linux. It uses the Linux parport driver and is definitely the prefered
access method on Linux. It also means that you do not require root
access.

%description -l pl.UTF-8
To jest sterownik Device::ParallelPort używający bezpośredniego
dostępu do wejścia/wyjścia pod Linuksem. Korzysta z linuksowego
sterownika portu równoległego i jest preferowaną metodą dostępu na
Linuksie. Oznacza to także, że nie trzeba mieć praw roota.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Device/ParallelPort
%dir %{perl_vendorarch}/Device/ParallelPort/drv
%{perl_vendorarch}/Device/ParallelPort/drv/parport.pm
%dir %{perl_vendorarch}/auto/Device/ParallelPort
%dir %{perl_vendorarch}/auto/Device/ParallelPort/drv
%dir %{perl_vendorarch}/auto/Device/ParallelPort/drv/parport
%attr(755,root,root) %{perl_vendorarch}/auto/Device/ParallelPort/drv/parport/parport.so
%{_mandir}/man3/*
