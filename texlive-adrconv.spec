%global tl_name adrconv
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	BibTeX styles to implement an address database
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/adrconv
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adrconv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adrconv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adrconv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides a collection of BibTeX style files to turn an
address database stored in the .bib format into files suitable for
printing as address books or included into letter classes like akletter
or scrletter2. The data may be sorted either by name or birthday and
output provides files in various formats for address books or time
planners.

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
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/adrconv
%dir %{_datadir}/texmf-dist/doc/latex/adrconv
%dir %{_datadir}/texmf-dist/source/latex/adrconv
%dir %{_datadir}/texmf-dist/tex/latex/adrconv
%dir %{_datadir}/texmf-dist/doc/latex/adrconv/adrconv_pages08.pages
%dir %{_datadir}/texmf-dist/doc/latex/adrconv/adrconv_pages08.pages/Contents
%dir %{_datadir}/texmf-dist/doc/latex/adrconv/adrconv_pages08.pages/QuickLook
%{_datadir}/texmf-dist/bibtex/bst/adrconv/adrbirthday.bst
%{_datadir}/texmf-dist/bibtex/bst/adrconv/adrconv.bst
%{_datadir}/texmf-dist/bibtex/bst/adrconv/adrfax.bst
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/2latex.vim
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/README
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/adrconv.pdf
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/adrconv.tex
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/adrconv_pages08.pages/Contents/PkgInfo
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/adrconv_pages08.pages/QuickLook/Thumbnail.jpg
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/adrconv_pages08.pages/index.xml.gz
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/adrdir.tex
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/adrfax.tex
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/adrguide.pdf
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/adrguide.tex
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/adrmontage1.tex
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/adrmontage2.tex
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/birthday.tex
%doc %{_datadir}/texmf-dist/doc/latex/adrconv/example.bib
%doc %{_datadir}/texmf-dist/source/latex/adrconv/adrconv.dtx
%doc %{_datadir}/texmf-dist/source/latex/adrconv/adrconv.ins
%{_datadir}/texmf-dist/tex/latex/adrconv/adrdir.cfg
%{_datadir}/texmf-dist/tex/latex/adrconv/adrplaner.cfg
%{_datadir}/texmf-dist/tex/latex/adrconv/adrsmall.cfg
