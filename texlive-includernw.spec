Name:		includeRnw
Version:	0.1.0
Release:	1
Summary:	This package is for including .Rnw (knitr/sweave)-files inside .tex-files. 
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/includernw
License:	The LATEX Project Public License 1.3c
Source0:	http://ctan.altspu.ru/systems/texlive/tlnet/archive/includernw.tar.xz
Source1:	http://ctan.altspu.ru/systems/texlive/tlnet/archive/includernw.doc.tar.xz
BuildArch:	noarch
BuildRequires: texlive-tlpkg
Requires(pre): texlive-tlpkg
Requires(post):texlive-kpathsea	

%description
This package is for including .Rnw (knitr/sweave)-files inside .tex-files. 

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/includernw
%doc %{_texmfdistdir}/doc/latex/includernw

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
