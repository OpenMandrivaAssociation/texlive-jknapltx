%global tl_name jknapltx
%global tl_revision 19440

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Miscellaneous packages by Joerg Knappen
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jknappen
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jknapltx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jknapltx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Miscellaneous macros by Jorg Knappen, including: represent counters in
greek; Maxwell's non-commutative division; latin1jk, latin2jk and
latin3jk, which are their inputenc definition files that allow verbatim
input in the respective ISO Latin codes; blackboard bold fonts in maths;
use of RSFS fonts in maths; extra alignments for \parboxes; swap Roman
and Sans fonts; transliterate semitic languages; patches to make (La)TeX
formulae embeddable in SGML; use maths "minus" in text as appropriate;
simple Young tableaux.

