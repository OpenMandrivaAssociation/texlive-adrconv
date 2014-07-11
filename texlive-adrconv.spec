# revision 17683
# category Package
# catalog-ctan /macros/latex/contrib/adrconv
# catalog-date 2010-04-05 11:11:18 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-adrconv
Version:	1.3
Release:	8
Summary:	BibTeX styles to implement an address database
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/adrconv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adrconv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adrconv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adrconv.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Adrconv is a collection of BibTeX style files to turn an
address database stored in the .bib format into files suitable
for printing as address books or included into letter classes
like akletter or scrletter2. Adrconv will sort the data either
by name or birthday and create output files in various formats
for address books or time planers.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/adrconv/adrbirthday.bst
%{_texmfdistdir}/bibtex/bst/adrconv/adrconv.bst
%{_texmfdistdir}/bibtex/bst/adrconv/adrfax.bst
%{_texmfdistdir}/tex/latex/adrconv/adrdir.cfg
%{_texmfdistdir}/tex/latex/adrconv/adrplaner.cfg
%{_texmfdistdir}/tex/latex/adrconv/adrsmall.cfg
%doc %{_texmfdistdir}/doc/latex/adrconv/2latex.vim
%doc %{_texmfdistdir}/doc/latex/adrconv/adrconv.tex
%doc %{_texmfdistdir}/doc/latex/adrconv/adrconv_pages08.pages/Contents/PkgInfo
%doc %{_texmfdistdir}/doc/latex/adrconv/adrconv_pages08.pages/QuickLook/Thumbnail.jpg
%doc %{_texmfdistdir}/doc/latex/adrconv/adrconv_pages08.pages/index.xml.gz
%doc %{_texmfdistdir}/doc/latex/adrconv/adrdir.tex
%doc %{_texmfdistdir}/doc/latex/adrconv/adrfax.tex
%doc %{_texmfdistdir}/doc/latex/adrconv/adrguide.pdf
%doc %{_texmfdistdir}/doc/latex/adrconv/adrguide.tex
%doc %{_texmfdistdir}/doc/latex/adrconv/adrmontage1.tex
%doc %{_texmfdistdir}/doc/latex/adrconv/adrmontage2.tex
%doc %{_texmfdistdir}/doc/latex/adrconv/birthday.tex
%doc %{_texmfdistdir}/doc/latex/adrconv/example.bib
#- source
%doc %{_texmfdistdir}/source/latex/adrconv/adrconv.dtx
%doc %{_texmfdistdir}/source/latex/adrconv/adrconv.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 749090
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 717798
- texlive-adrconv
- texlive-adrconv
- texlive-adrconv
- texlive-adrconv
- texlive-adrconv

