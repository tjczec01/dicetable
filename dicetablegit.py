# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 19:20:22 2020

Github: https://github.com/tjczec01

@author: Travis J Czechorski

E-mail: tjczec01@gmail.com
"""

import os
clear = lambda: os.system('cls')
cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
path_fol = "{}\Dicetable".format(dir_path)
try:
       os.mkdir(path_fol)
except:
       pass


def dt(dn, ds):

    def ichange(t, i, u):
        v1 = t[-i]
        tl = len(t)
        while v1 >= u and i <= tl:
            v1 = t[-i-1]
            t[-i] = 1
            t[-i-1] += 1
            v1 = t[-i-1]
            i += 1
        if t[-1] == 1:
            i = 1
        return t, i
    DDS = ds + 1
    dv = [i for i in range(1, DDS, 1)]
    dbt = [1 for i in range(1, dn + 1, 1)]
    dbtf = tuple([dv[-1] for i in range(1, dn + 1, 1)])
    dt = []
    dt.append(tuple(dbt))
    kl = 1
    vgb = list(dt[-1])
    vg = vgb[-1]
    while dbtf not in dt:
        vgb = list(dt[-1])
        vg = vgb[-1]
        vg0 = vgb[-1]
        if vg < DDS and vg0 < DDS:
            dbt = [1 for i in range(1, dn + 1, 1)]
            vg += 1
            vgb[-kl] = vg
            vvi, ii = ichange(vgb, kl, DDS)
            dt.append(tuple(vvi))
        else:
            dbt = [1 for i in range(1, dn + 1, 1)]
            vv = vgb[-kl - 1]
            vvi, ii = ichange(vgb, kl, DDS)
            vv += 1
            vgb[-kl] = 1
            vgb[-kl - 1] = vv
            if vvi[-1] == 1:
                kl = 1
            else:
                kl = ii
            dt.append(tuple(vvi))
    return dt


def dicec(dn, ds):
    DF = []
    dtf = dt(dn, ds)
    for ij in range(1, ds + 1, 1):
        df = []
        for im in dtf:
            ijk = im
            i0 = ijk[0]
            if ij == i0:
                df.append(im)
        DF.append(df)
        df = []
    return DF


DN = int(input("Number of dice --> "))
DS = int(input("Total number of sides per die --> "))
print("")
DICE = dicec(DN, DS)
DCL = len(DICE[0])
DCS = 0
diecs = len(DICE[0])*DS
for i in DICE:
    DCS += len(i)
    print(i)
    print("")

print("")
print("Total number of combinations: {}".format(DCS))

DT = []
texdoc = []
doms = r"""\documentclass[tikz, border=0.5in]{standalone}
\usepackage{tikz}
\usepackage{amsmath}
\usetikzlibrary{shapes}
\usetikzlibrary{matrix}
\usetikzlibrary{calc, positioning}
\usepackage{stackengine, scalerel, xcolor}
\newcommand\domsz{0.8cm}
\newcommand\domwd{70pt}
\newcommand\domcolor{white}
\newcommand\domsq{\fboxsep=0pt\fbox{\textcolor{\domcolor}{\rule{\domwd}{\domwd}}}}
\setstackEOL{-}
\newlength\dotwd
\newlength\dotht
\newcommand\Q{\makebox[\dotwd]{$\bullet$}}
\newcommand\z{\makebox[\dotwd]{\phantom{$\bullet$}}}
\newcommand\scaledom[2][9]{%
    \setlength\dotwd{0.1\dimexpr\domwd}%
    \setlength\dotht{0.1\dimexpr\domwd}%
  \setstackgap{L}{\the\dotht}%
  \savestack\tmpbox{\stackinset{c}{}{c}{-0.1ex}{\Longstack{#2}}{\domsq}}%
  \scaleto{\tmpbox}{\domsz}%
}
\newcommand\dom[1]{\csname dom#1\endcsname}
\expandafter\def\csname dom1\endcsname{\scaledom{
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\Q\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z
}}
\expandafter\def\csname dom2\endcsname{\scaledom{
    \z\z\z\z\z\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\z\z\z\z\z
}}
\expandafter\def\csname dom3\endcsname{\scaledom{
    \z\z\z\z\z\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\Q\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\z\z\z\z\z
}}
\expandafter\def\csname dom4\endcsname{\scaledom{
    \Q\z\z\z\z\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\z\z\z\z\Q
}}
\expandafter\def\csname dom5\endcsname{\scaledom{
    \Q\z\z\z\z\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\Q\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\z\z\z\z\Q
}}
\expandafter\def\csname dom6\endcsname{\scaledom{
    \Q\z\z\z\z\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\z\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\z\z\z\z\Q
}}
\expandafter\def\csname dom7\endcsname{\scaledom{
    \Q\z\z\z\z\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\z\z\z\z\Q
}}
\expandafter\def\csname dom8\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\z\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom9\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom10\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\z\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom11\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\z\z\z\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\z\z\z\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom12\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\z\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\z\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\z\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom13\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\z\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\z\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom14\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\z\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\z\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom15\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\z\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\z\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom16\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\Q\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\Q\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom17\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\Q\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\Q\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom18\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom19\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \z\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\z-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom20\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom21\endcsname{\scaledom{
    \Q\z\z\z\Q\z\z\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\z\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom22\endcsname{\scaledom{
    \Q\z\z\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom23\endcsname{\scaledom{
    \Q\z\z\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\z\z\Q
}}
\expandafter\def\csname dom24\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom25\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom26\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\Q\z\z\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\z\z\Q\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom27\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\Q\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\Q\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom28\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom29\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom30\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom31\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom32\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom33\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom34\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom35\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\z\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\z\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom36\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom37\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom38\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom39\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\z\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\z\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom40\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\z\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom41\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom42\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\Q\z\Q\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom43\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\Q\Q\Q\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom44\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\Q\z\Q\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom45\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\Q\Q\Q\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom46\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom47\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\z\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom48\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom49\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom50\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom51\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom52\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom53\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom54\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\Q\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\Q\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom55\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\Q\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\Q\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom56\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\Q\Q\Q\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\Q\Q\Q\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom57\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\Q\Q\Q\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\Q\Q\Q\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom58\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom59\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom60\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom61\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\z\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom62\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom63\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\z\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\z\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom64\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom65\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom66\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom67\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom68\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom69\endcsname{\scaledom{
    \Q\z\Q\z\Q\z\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\z\Q\z\Q\z\Q
}}
\expandafter\def\csname dom70\endcsname{\scaledom{
    \Q\z\Q\z\Q\Q\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\Q\Q\z\Q\z\Q
}}
\expandafter\def\csname dom71\endcsname{\scaledom{
    \Q\z\Q\z\Q\Q\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\Q\Q\z\Q\z\Q
}}
\expandafter\def\csname dom72\endcsname{\scaledom{
    \Q\z\Q\Q\Q\Q\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\Q\Q\Q\Q\z\Q
}}
\expandafter\def\csname dom73\endcsname{\scaledom{
    \Q\z\Q\Q\Q\Q\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\Q\Q\Q\Q\z\Q
}}
\expandafter\def\csname dom74\endcsname{\scaledom{
    \Q\z\Q\Q\Q\Q\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\Q\Q\Q\Q\z\Q
}}
\expandafter\def\csname dom75\endcsname{\scaledom{
    \Q\z\Q\Q\Q\Q\Q\z\Q-
    \z\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\z-
    \Q\z\Q\Q\Q\Q\Q\z\Q
}}
\expandafter\def\csname dom76\endcsname{\scaledom{
    \Q\z\Q\Q\Q\Q\Q\z\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\z\Q\Q\Q\Q\Q\z\Q
}}
\expandafter\def\csname dom77\endcsname{\scaledom{
    \Q\z\Q\Q\Q\Q\Q\z\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\z\Q\Q\Q\Q\Q\z\Q
}}
\expandafter\def\csname dom78\endcsname{\scaledom{
    \Q\z\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\z\Q
}}
\expandafter\def\csname dom79\endcsname{\scaledom{
    \Q\z\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\z\Q
}}
\expandafter\def\csname dom80\endcsname{\scaledom{
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\z\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q
}}
\expandafter\def\csname dom81\endcsname{\scaledom{
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q-
    \Q\Q\Q\Q\Q\Q\Q\Q\Q
}}
\definecolor{1}{rgb}{1, 0, 0}
\definecolor{2}{rgb}{0, 0, 1}
\definecolor{3}{rgb}{0, 1, 0}
\definecolor{4}{rgb}{0, 1, 1}
\definecolor{5}{rgb}{1, 0, 1}
\definecolor{6}{rgb}{1, 1, 0}
\definecolor{7}{rgb}{1, 1, 1}
\definecolor{8}{rgb}{1, 0.5, 0.5}
\definecolor{9}{rgb}{0.5, 0.5, 0}
\definecolor{10}{rgb}{0.5, 1, 0.5}
\definecolor{11}{rgb}{0, 0.5, 0.5}
\begin{document}
\begin{tikzpicture}
\matrix(m)[matrix of nodes, column sep=-\pgflinewidth, row sep=-\pgflinewidth, nodes={rectangle, draw, line width=1pt, anchor=center, text centered, align=center,text width=4cm, rounded corners, minimum width=1.5cm, minimum height=1cm}, nodes in empty cells]{%
\renewcommand\domcolor{7} """
with open("{}\Output_text.txt".format(path_fol), "w") as text_file:
    print("\documentclass[tikz, border=0.5in]{standalone}", file=text_file)
    print("usepackage{tikz}".join("\ "), file=text_file)
    print("usepackage{amsmath}".join("\ "), file=text_file)
    print("usetikzlibrary{calc, positioning}".join("\ "), file=text_file)
    print("usetikzlibrary{shapes}".join("\ "), file=text_file)
    print("usetikzlibrary{matrix}".join("\ "), file=text_file)
    print(r"""\tikzset{%
  dot hidden/.style={},
  line hidden/.style={},
  dot colour/.style={dot hidden/.append style={color=#1}},
  dot colour/.default=black,
  line colour/.style={line hidden/.append style={color=#1}},
  line colour/.default=black,
}%
\usepackage{xparse}
\NewDocumentCommand{\drawdie}{O{}m}{%
\begin{tikzpicture}[x=1cm,y=1cm,radius=0.06,#1]
\draw[rounded corners=1,line hidden] (0,0) rectangle (1,1);
\ifnum#2<10% "standard die"
  \ifodd#2
    \fill[dot hidden] (0.5,0.5) circle;% 1,3,5,7,9
  \fi
  \ifnum#2>1
    \fill[dot hidden] (0.15,0.15) circle;% 2
    \fill[dot hidden] (0.85,0.85) circle;% 3
    \ifnum#2>3
      \fill[dot hidden] (0.15,0.85) circle;% 4
      \fill[dot hidden] (0.85,0.15) circle;% 5
      \ifnum#2>5
        \fill[dot hidden] (0.85,0.5) circle;% 5
        \fill[dot hidden] (0.15,0.5) circle;% 6
        \ifnum#2>7
          \fill[dot hidden] (0.5,0.85) circle;% 7
          \fill[dot hidden] (0.5,0.15) circle;% 8
        \fi
      \fi
    \fi
  \fi
\fi
\ifnum#2>9% "extended die"
  \ifnum#2<13%
    \fill[dot hidden] (0.15,0.15) circle;
    \fill[dot hidden] (0.15,0.85) circle;
    \fill[dot hidden] (0.85,0.15) circle;
    \fill[dot hidden] (0.85,0.85) circle;
    \fill[dot hidden] (0.15,0.38) circle;
    \fill[dot hidden] (0.15,0.61) circle;
    \fill[dot hidden] (0.85,0.38) circle;
    \fill[dot hidden] (0.85,0.61) circle;
    \ifodd#2
      \fill[dot hidden] (0.50,0.50) circle;
      \fill[dot hidden] (0.50,0.15) circle;
      \fill[dot hidden] (0.50,0.85) circle;
    \else
      \fill[dot hidden] (0.50,0.38) circle;
      \fill[dot hidden] (0.50,0.61) circle;
    \fi
    \ifnum#2>11
      \fill[dot hidden] (0.50,0.15) circle;
      \fill[dot hidden] (0.50,0.85) circle;
    \fi
  \else
    \fill[dot hidden] (0.15,0.15) circle;
    \fill[dot hidden] (0.15,0.85) circle;
    \fill[dot hidden] (0.85,0.15) circle;
    \fill[dot hidden] (0.85,0.85) circle;
    \fill[dot hidden] (0.15,0.38) circle;
    \fill[dot hidden] (0.15,0.61) circle;
    \fill[dot hidden] (0.85,0.38) circle;
    \fill[dot hidden] (0.85,0.61) circle;
    \fill[dot hidden] (0.38,0.15) circle;
    \fill[dot hidden] (0.38,0.85) circle;
    \fill[dot hidden] (0.61,0.15) circle;
    \fill[dot hidden] (0.61,0.85) circle;
    \ifnum#2<14
      \fill[dot hidden] (0.50,0.50) circle;
    \fi
    \ifnum#2>13
      \fill[dot hidden] (0.38,0.38) circle;
      \fill[dot hidden] (0.61,0.61) circle;
      \ifnum#2>14
        \fill[dot hidden] (0.38,0.61) circle;
        \ifnum#2>15
          \fill[dot hidden] (0.61,0.38) circle;
        \fi
      \fi
    \fi
  \fi
\fi
\end{tikzpicture}%
}% """, file=text_file)
    print("\\begin{document}", file=text_file)
    print("\\begin{tikzpicture}", file=text_file)
    print("\\matrix(m)[matrix of nodes, column sep=-\pgflinewidth, row sep=-\pgflinewidth, nodes={rectangle, draw, line width=1pt, anchor=center, text centered, align=center,text width=4cm, rounded corners, minimum width=1.5cm, minimum height=1cm}, nodes in empty cells]{%", file=text_file)
    for di in range(len(DICE)):
        DTx = []
        for dii in range(len(DICE[di])):

            diix = DICE[di][dii]
            dstr = []
            for diii in range(len(DICE[di][dii])):
                df = ("drawdie{}{}{}".format('{', str("{}".format(int(diix[diii]))), '}'))
                dstr.append(df)
            dfs = dstr[0]
            for ids in range(1, len(dstr), 1):
                dfs += dstr[ids]
            DFS = dfs + " &" + " "
            DF1 = DFS.replace('draw', "draw")
            DTx.append(DFS.replace('\\draw', "\draw"))
            DFF = "{}".format(DFS)
        DTx[-1] = DTx[-1].replace(' & ', " \\\ ")
        DT.append("".join(DTx))
        DTx = []
        print(DT[-1].replace("draw", "\draw"), file=text_file)

    print("};", file=text_file)
    print('\\node[font=\huge, above=2.0cm]  at ($(m-1-{})!0.5!(m-1-{})$)'.format(int(DCL/2), int((DCL/2) + 1)) + '{Dice Table};', file=text_file)
    print("\\node[font=\large, above=1.25cm]  at ($(m-1-{})!0.5!(m-1-{})$)".format(int(DCL/2), int((DCL/2) + 1)) + "{}Total Dice: {}  Faces per die: {} Total combinations: {}{};".format('{', DN, DS, DCS, '}'), file=text_file)
    print("\\end{tikzpicture}", file=text_file)
    print("\\end{document}", file=text_file)
    text_file.close()


with open("{}\Output_text.txt".format(path_fol)) as fin:
    for line in fin:
        texdoc.append(line)

with open("{}\Tex_Output.tex".format(path_fol), 'w') as fout:
    for i in range(len(texdoc)):
        fout.write(texdoc[i])

texdom = []

with open("{}\Output_text_dom.txt".format(path_fol), "w") as text_file2:
    print(doms, file=text_file2)
    for di in range(len(DICE)):
        DTx = []
        for dii in range(len(DICE[di])):

            diix = DICE[di][dii]
            dstr = []
            for diii in range(len(DICE[di][dii])):
                df = ("dom{}{}{}".format('{', str("{}".format(int(diix[diii]))), '}'))
                dstr.append(df)
            dfs = dstr[0]
            for ids in range(1, len(dstr), 1):
                dfs += dstr[ids]
            DFS = dfs + " & "
            DF1 = DFS.replace('dom', "dom")
            DTx.append(DFS.replace('\\dom', "\dom"))
            DFF = "{}".format(DFS)
        DTx[-1] = DTx[-1].replace('} & ', "} \\\ ")
        DT.append("".join(DTx))
        DTx = []
        print(DT[-1].replace("dom", "\dom"), file=text_file2)
    print("};", file=text_file2)
    print('\\node[font=\huge, above=2.0cm]  at ($(m-1-{})!0.5!(m-1-{})$)'.format(int(DCL/2), int((DCL/2) + 1)) + '{Dice Table};', file=text_file2)
    print("\\node[font=\large, above=1.25cm]  at ($(m-1-{})!0.5!(m-1-{})$)".format(int(DCL/2), int((DCL/2) + 1)) + "{}Total Dice: {}  Faces per die: {} Total combinations: {}{};".format('{', DN, DS, DCS, '}'), file=text_file2)
    print("\\end{tikzpicture}", file=text_file2)
    print("\\end{document}", file=text_file2)
with open("{}\Output_text_dom.txt".format(path_fol)) as fin2:
    for line2 in fin2:
        texdom.append(line2)

with open("{}\Tex_Output_dom.tex".format(path_fol), 'w') as fout2:
    for i2 in range(len(texdom)):
        fout2.write(texdom[i2])
