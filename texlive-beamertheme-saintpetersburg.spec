Name:		texlive-beamertheme-saintpetersburg
Version:	45877
Release:	2
Summary:	A beamer theme that incorporates colours and fonts of Saint Petersburg State University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-saintpetersburg
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-saintpetersburg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-saintpetersburg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-saintpetersburg.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This minimalistic beamer theme incorporates Saint Petersburg
State University colours and fonts. It is suitable for both
presentations and posters.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/beamertheme-saintpetersburg
%{_texmfdistdir}/tex/latex/beamertheme-saintpetersburg
%doc %{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
