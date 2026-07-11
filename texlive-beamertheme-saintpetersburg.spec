%global tl_name beamertheme-saintpetersburg
%global tl_revision 45877

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A beamer theme that incorporates colours and fonts of Saint Petersburg State ...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-saintpetersburg
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-saintpetersburg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-saintpetersburg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-saintpetersburg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This minimalistic beamer theme incorporates Saint Petersburg State
University colours and fonts. It is suitable for both presentations and
posters.

