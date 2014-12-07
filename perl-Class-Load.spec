%define upstream_name    Class-Load
%define upstream_version 0.22

Summary:	A working (require "Class::Name") and more
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz
Source1:	%{name}.rpmlintrc
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires: perl(namespace::clean)
BuildRequires:	perl(Data::OptList)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Implementation)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Package::Stash)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)

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
%{perl_vendorlib}/*
%{_mandir}/man3/*
