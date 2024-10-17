Name:		texlive-erw-l3
Version:	61799
Release:	2
Summary:	Utilities based on LaTeX3
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/erw-l3
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/erw-l3.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/erw-l3.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/erw-l3.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Utilities based on LaTeX3. Highlight: \erw_merge_sort.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/erw-l3
%{_texmfdistdir}/tex/latex/erw-l3
%doc %{_texmfdistdir}/doc/latex/erw-l3

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
