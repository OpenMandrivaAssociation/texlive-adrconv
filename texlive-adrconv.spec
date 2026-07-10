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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides a collection of BibTeX style files to turn an
address database stored in the .bib format into files suitable for
printing as address books or included into letter classes like akletter
or scrletter2. The data may be sorted either by name or birthday and
output provides files in various formats for address books or time
planners.

