%define upstream_name    Class-Load
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:    A working (require "Class::Name") and more
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
'require EXPR' only accepts 'Class/Name.pm' style module names, not
'Class::Name'. How frustrating! For that, we provide 'load_class
'Class::Name''.

It's often useful to test whether a module can be loaded, instead of
throwing an error when it's not available. For that, we provide
'try_load_class 'Class::Name''.

Finally, sometimes we need to know whether a particular class has been
loaded. Asking '%INC' is an option, but that will miss inner packages and
any class for which the filename does not correspond to the package name.
For that, we provide 'is_class_loaded 'Class::Name''.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


