%define module   Context-Preserve

Name:		perl-%{module}
Version:	0.01
Release:	5
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Run code after a subroutine call preserving the context
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Context/%{module}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::use::ok)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.01-3mdv2011.0
+ Revision: 654901
- rebuild for updated spec-helper

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.01-2mdv2011.0
+ Revision: 375961
- rebuild

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdv2010.0
+ Revision: 371820
- import perl-Context-Preserve


* Mon May 04 2009 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist

