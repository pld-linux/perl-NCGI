#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	NCGI
Summary:	NCGI - A Common Gateway Interface (CGI) Class
Summary(pl):	NCGI - klasa dla CGI (Common Gateway Interface)
Name:		perl-NCGI
Version:	0.05
Release:	0.1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	b2eba415d26650d10efb33b40d20c82c
URL:		http://search.cpan.org/dist/NCGI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Log-Delta >= 0.02
BuildRequires:	perl-XML-API >= 0.07
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NCGI is an aid for authors writing CGI scripts. It has the same basic
function as the well known CGI module although with a completely
different interface.

%description -l pl
NCGI jest pomoc± dla autorów pisz±cych skrypty CGI. Ma te same funkcje
podstawowe co dobrze znany modu³ CGI, lecz z zupe³nie innym
interfejsem.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

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
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/NCGI
%{_mandir}/man3/*
