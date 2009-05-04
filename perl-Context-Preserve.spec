%define module   Context-Preserve
%define version    0.01
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Run code after a subroutine call, preserving the context the subroutine would have seen if it were the last statement in the caller
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Context/%{module}-%{version}.tar.gz
BuildRequires: perl(Exporter)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl-Test-use-ok
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Sometimes you need to call a function, get the results, act on the results,
then return the result of the function. This is painful because of
contexts; the original function can behave different if it's called in
void, scalar, or list context. You can ignore the various cases and just
pick one, but that's fragile. To do things right, you need to see which
case you're being called in, and then call the function in that context.
This results in 3 code paths, which is a pain to type in (and maintain).

This module automates the process. You provide a coderef that is the
"original function", and another coderef to run after the original runs.
You can modify the return value (aliased to @_) here, and do whatever else
you need to do. 'wantarray' is correct inside both coderefs; in "after",
though, the return value is ignored and the value 'wantarray' returns is
related to the context that the original function was called in.



%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


