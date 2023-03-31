Name:		texlive-adrconv
Version:	46817
Release:	2
Summary:	BibTeX styles to implement an address database
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/adrconv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adrconv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adrconv.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adrconv.source.r%{version}.tar.xz
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
%{_texmfdistdir}/bibtex/bst/adrconv
%{_texmfdistdir}/tex/latex/adrconv
%doc %{_texmfdistdir}/doc/latex/adrconv
#- source
%doc %{_texmfdistdir}/source/latex/adrconv

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
