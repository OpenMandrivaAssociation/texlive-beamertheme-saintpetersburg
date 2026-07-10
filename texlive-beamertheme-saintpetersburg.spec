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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This minimalistic beamer theme incorporates Saint Petersburg State
University colours and fonts. It is suitable for both presentations and
posters.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg
%dir %{_datadir}/texmf-dist/source/latex/beamertheme-saintpetersburg
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-saintpetersburg
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/figures
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/SaintPetersburg.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/example.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/figures/propagating-elevation.eps
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/figures/propagating-wave-height-x.eps
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/figures/propagating-wave-length-x.eps
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/figures/propagating-wave-period.eps
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/figures/standing-elevation.eps
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/figures/standing-wave-height-x.eps
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/figures/standing-wave-length-x.eps
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/figures/standing-wave-period.eps
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-saintpetersburg/SaintPetersburg.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-saintpetersburg/SaintPetersburg.ins
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-saintpetersburg/beamercolorthemeSaintPetersburg.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-saintpetersburg/beamerfontthemeSaintPetersburg.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-saintpetersburg/beamerthemeSaintPetersburg.dtx
%{_datadir}/texmf-dist/tex/latex/beamertheme-saintpetersburg/beamercolorthemeSaintPetersburg.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-saintpetersburg/beamerfontthemeSaintPetersburg.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-saintpetersburg/beamerthemeSaintPetersburg.sty
