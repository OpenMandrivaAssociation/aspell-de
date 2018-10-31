%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 20030222-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageeng german
%define languageenglazy German
%define languagecode de

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Epoch:		1
Version:	20030222.1
Release:	21
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.sourceforge.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
Provides:	aspell-de_CH
Provides:	aspell-de_AT
Provides:	aspell-de_DE
Provides:	spell-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

%build
./configure
%make

%install
%makeinstall_std

%files
%doc README COPYING doc/*
%{_libdir}/aspell-%{aspell_ver}/*

