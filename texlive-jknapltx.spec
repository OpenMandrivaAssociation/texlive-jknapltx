Name:		texlive-jknapltx
Version:	20061215
Release:	1
Summary:	Miscellaneous packages by Joerg Knappen
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jknappen
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jknapltx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jknapltx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Miscellaneous macros by Jorg Knappen, including: - represent
counters in greek; - Maxwell's non-commutative division; -
latin1jk, latin2jk and latin3jk, which are their inputenc
definition files that allow verbatim input in the respective
ISO Latin codes; - blackboard bold fonts in maths; - use of
RSFS fonts in maths; - extra alignments for \parboxes; - swap
Roman and Sans fonts; - transliterate semitic languages; -
patches to make (La)TeX formulae embeddable in SGML; - use
maths "minus" in text as appropriate; - simple Young tableaux.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/jknapltx/greekctr.sty
%{_texmfdistdir}/tex/latex/jknapltx/holtpolt.sty
%{_texmfdistdir}/tex/latex/jknapltx/latin1jk.def
%{_texmfdistdir}/tex/latex/jknapltx/latin2jk.def
%{_texmfdistdir}/tex/latex/jknapltx/latin3jk.def
%{_texmfdistdir}/tex/latex/jknapltx/mathbbol.sty
%{_texmfdistdir}/tex/latex/jknapltx/mathrsfs.sty
%{_texmfdistdir}/tex/latex/jknapltx/parboxx.sty
%{_texmfdistdir}/tex/latex/jknapltx/sans.sty
%{_texmfdistdir}/tex/latex/jknapltx/semtrans.sty
%{_texmfdistdir}/tex/latex/jknapltx/sgmlcmpt.sty
%{_texmfdistdir}/tex/latex/jknapltx/smartmn.sty
%{_texmfdistdir}/tex/latex/jknapltx/tccompat.sty
%{_texmfdistdir}/tex/latex/jknapltx/ursfs.fd
%{_texmfdistdir}/tex/latex/jknapltx/ustmary.fd
%{_texmfdistdir}/tex/latex/jknapltx/young.sty
%doc %{_texmfdistdir}/doc/latex/jknapltx/00readme.txt
%doc %{_texmfdistdir}/doc/latex/jknapltx/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/jknapltx/mathbbol.rme
%doc %{_texmfdistdir}/doc/latex/jknapltx/mathrsfs.rme

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
