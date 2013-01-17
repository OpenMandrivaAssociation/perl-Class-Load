%define upstream_name    Class-Load
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	A working (require "Class::Name") and more
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
'require EXPR' only accepts 'Class/Name.pm' style module names, not
'Class::Name'. How frustrating! For that, we provide 'load_class
'Class::Name''.

It's often useful to test whether a module can be loaded, instead of
throwing an error when it's not available. For that, we provide
'try_load_class 'Class::Name''.

Finally, sometimes we need to know whether a particular class has been
loaded. Asking '%%INC' is an option, but that will miss inner packages and
any class for which the filename does not correspond to the package name.
For that, we provide 'is_class_loaded 'Class::Name''.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-6mdv2012.0
+ Revision: 765088
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-5
+ Revision: 763532
- rebuilt for perl-5.14.x

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.60.0-4
+ Revision: 658280
- rebuild

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.60.0-3
+ Revision: 657768
- rebuild for updated spec-helper
- rebuild for updated spec-helper

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 602042
- import perl-Class-Load

