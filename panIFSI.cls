\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{panIFSI}[2025/01/01 classe de document PanIFSI pour mémoires en sciences infirmières] % Date de la version de la classe

\LoadClass[10pt]{article} % Charge la classe book avec une taille de police de 10pt

\newif\if@ecran % Crée un commutateur pour l'affichage à l'écran
\newif\if@impression % Crée un commutateur pour l'impression

\DeclareOption{ecran}{\@ecrantrue\@impressionfalse} % Active l'affichage à l'écran
\DeclareOption{impression}{\@impressiontrue\@ecranfalse} % Active l'affichage pour impression
\ExecuteOptions{ecran} % Par défaut, l'affichage est configuré pour l'écran
\ProcessOptions\relax % Traite les options du document

\RequirePackage{caption} % Pour la gestion des légendes de tableaux et figures
% Redéfinir les légendes des tableaux selon les paramètres linguistiques en cours
\iflanguage{english}{}{%
    \def\frenchtablename{Tableau}
}
\captionsetup{textfont=it, aboveskip=15pt, skip=3pt, justification=centering, labelsep=endash}
\usepackage{subcaption} % Pour la gestion des figures contenant des sous-figures
\RequirePackage{pdflscape,afterpage} % Pour la gestion des pages en mode paysage
\RequirePackage{xcolor} % Pour la gestion des couleurs
\RequirePackage{graphicx} % Pour la gestion des images

\RequirePackage{geometry} % Pour le format des pages
\geometry{
    paperwidth=210mm,
    paperheight=297mm,
    top=22mm,
    bottom=22mm,
    inner=18mm,
    outer=25mm,
    footskip=12mm,
    footnotesep=12mm plus 1pt minus 1pt
}
\usepackage{hyperref} % Pour la gestion des hyperliens et des signets
\if@ecran
  \hypersetup{colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue}
\else
  \hypersetup{colorlinks=false,pdfborder={0 0 0}}
  \AtBeginDocument{\begin{NoHyper}}
  \AtEndDocument{\end{NoHyper}}
  \RequirePackage[cam,center,width=210mm,height=297mm]{crop}
\fi

% Options pour les notes de bas de page
\usepackage[bottom]{footmisc} % Force les notes en bas de page

\RequirePackage[skip=1pt plus 1pt minus 1pt]{parskip} % Pour la gestion des paragraphes

\RequirePackage{termes-otf} % Pour utiliser la police TeX Gyre Termes
% Définir la police principale et la police mathématique
\setmainfont{TeX Gyre Termes}
\setmathfont{TeX Gyre Termes Math}
\setsansfont{Arial} % Définit la police sans empattement comme Arial

% Gestion de la bibliographie
\RequirePackage[
  style=ext-authoryear-comp, 
  giveninits=true,
  articlein=false,
  backend=biber, 
  language=autobib, 
  doi=false,
  autolang=other, 
  doi=false, 
  isbn=false, 
  url=false, 
  eprint=false]{biblatex}


  \newcommand{\TFEAuthor}[1]{\def\@TFEAuthor{#1}} % Définit l'auteur du TFE
  \newcommand{\TFETitle}[1]{\def\@TFETitle{#1}} % Définit le titre du TFE
  % et en attendant mieux :
  \let\TFEAuthor\author
  \let\TFETitle\title
  \let\tightlist\relax
  