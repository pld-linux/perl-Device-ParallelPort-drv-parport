
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Device
%define	pnam	ParallelPort-drv-parport
Summary:	Device::ParallelPort
Name:		perl-Device-ParallelPort-drv-parport
Version:	1.0
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	901987e4a37bfe2d7241530bda05f36e
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Device::ParallelPort)
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you run your program with `perl -d:Trace program', this module will
print a message to standard error just before each line is executed.
This is is something like the shell's `-x' option.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Device/ParallelPort/drv/parport.pm
%{perl_vendorarch}/auto/Device/ParallelPort/drv/parport/parport.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Device/ParallelPort/drv/parport/parport.so
%{_mandir}/man3/*
