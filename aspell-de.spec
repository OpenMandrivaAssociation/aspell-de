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
Release:	%mkrel 2
Summary:	%{languageenglazy} files for aspell
Group:		System/Internationalization
Source:		http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		http://aspell.sourceforge.net/
License:	GPL
Epoch:		1

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


