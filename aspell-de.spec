%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 20030222-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageeng german
%define languageenglazy German
%define languagecode de

Name:		aspell-%{languagecode}
Version:	20030222.1
Release:	%mkrel 12
Summary:	%{languageenglazy} files for aspell
Group:		System/Internationalization
Source:		http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		http://aspell.sourceforge.net/
License:	GPL
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
Obsoletes:	aspell-de_CH
Provides:	aspell-de_CH
Provides:	aspell-de_AT
Provides:	aspell-de_DE
Obsoletes:	spell-%{languagecode}
Provides:	spell-%{languagecode}

# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
./configure
%make

%install
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING doc/*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:20030222.1-10mdv2011.0
+ Revision: 662805
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1:20030222.1-9mdv2011.0
+ Revision: 603200
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1:20030222.1-8mdv2010.1
+ Revision: 518914
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1:20030222.1-7mdv2010.0
+ Revision: 413060
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1:20030222.1-6mdv2009.1
+ Revision: 350006
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1:20030222.1-5mdv2009.0
+ Revision: 220369
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 1:20030222.1-4mdv2008.1
+ Revision: 182412
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1:20030222.1-3mdv2008.1
+ Revision: 148746
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 20030222.1-2mdv2007.0
+ Revision: 123237
- Import aspell-de

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 20030222.1-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Tue Oct 04 2005 Thierry Vignaud <tvignaud@mandriva.com> 20030222.1-2mdk
- should not be a noarch packag

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 20030222.1-1mdk
- new release

