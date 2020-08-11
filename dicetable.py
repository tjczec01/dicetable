# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 19:20:22 2020

Github: https://github.com/tjczec01

@author: Travis J Czechorski

E-mail: tjczec01@gmail.com
"""


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


DN = 4
DS = 6
DICE = dicec(DN, DS)
DT = []

print("\documentclass{article}")
print("usepackage[a4paper, bindingoffset=0.15in, left=0.25in, right=0.25in, top=0.25in, bottom=0.25in, footskip=0.15in]{geometry}".join("\ "))
print("usepackage{epsdice}".join("\ "))
print("usepackage{pdflscape}".join("\ "))
print("usepackage{graphicx}".join("\ "))
print("usepackage{adjustbox}".join("\ "))
print("\\begin{document}")
print("\\begin{landscape}")
print("\\begin{table}[ht]")
print("\centering")
print("\caption{Dice Table}")
print("\\begin{adjustbox}{width=\\textwidth}")
cc = "|" + "c|"*(len(DICE[0]))
print("\\begin{tabular}" + "{}{}{}".format('{ ', cc , " }"))
print(" \hline \n")
for di in range(len(DICE)):
    DTx = []
    for dii in range(len(DICE[di])):

        diix = DICE[di][dii]
        dstr = []
        for diii in range(len(DICE[di][dii])):
            df = ("epsdice{}{}{}".format('{', str("{}".format(int(diix[diii]))), '}'))
            dstr.append(df)
        dfs = dstr[0]
        for ids in range(1, len(dstr), 1):
            dfs += dstr[ids]
        DFS = dfs + " &" + " "
        DF1 = DFS.replace('eps', "eps")
        DTx.append(DFS.replace('\\eps', "\eps"))
        DFF = "{}".format(DFS)
    DTx[-1] = DTx[-1].replace(' & ', " \\\ ")
    DT.append("".join(DTx))
    DTx = []
    print(DT[-1].replace("eps", "\eps"))
    print(" \hline")

print("\n")
print("\end{tabular}")
print("\\end{adjustbox}")
print("\\end{table}")
print("\\end{landscape}")
print("\\end{document}")