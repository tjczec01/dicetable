# dicetable
Computes every combination for a dicetable given number of dice and number of sides per die. Output is copyable and can be directly pasted into a Latex renderer i.e. [TexWorks](http://www.tug.org/texworks/). 

# Output

    \documentclass{article}
    \usepackage[a4paper, bindingoffset=0.15in, left=0.25in, right=0.25in, top=0.25in, bottom=0.25in, footskip=0.15in]{geometry} 
    \usepackage{epsdice} 
    \usepackage{pdflscape} 
    \usepackage{graphicx} 
    \usepackage{adjustbox} 
    \begin{document}
    \begin{landscape}
    \begin{table}[ht]
    \centering
    \caption{Dice Table}
    \begin{adjustbox}{width=\textwidth}
    \begin{tabular}{ |c|c|c|c|c|c| }
     \hline 

    \epsdice{1}\epsdice{1} & \epsdice{1}\epsdice{2} & \epsdice{1}\epsdice{3} & \epsdice{1}\epsdice{4} & \epsdice{1}\epsdice{5} & \epsdice{1}\epsdice{6} \\ 
     \hline
    \epsdice{2}\epsdice{1} & \epsdice{2}\epsdice{2} & \epsdice{2}\epsdice{3} & \epsdice{2}\epsdice{4} & \epsdice{2}\epsdice{5} & \epsdice{2}\epsdice{6} \\ 
     \hline
    \epsdice{3}\epsdice{1} & \epsdice{3}\epsdice{2} & \epsdice{3}\epsdice{3} & \epsdice{3}\epsdice{4} & \epsdice{3}\epsdice{5} & \epsdice{3}\epsdice{6} \\ 
     \hline
    \epsdice{4}\epsdice{1} & \epsdice{4}\epsdice{2} & \epsdice{4}\epsdice{3} & \epsdice{4}\epsdice{4} & \epsdice{4}\epsdice{5} & \epsdice{4}\epsdice{6} \\ 
     \hline
    \epsdice{5}\epsdice{1} & \epsdice{5}\epsdice{2} & \epsdice{5}\epsdice{3} & \epsdice{5}\epsdice{4} & \epsdice{5}\epsdice{5} & \epsdice{5}\epsdice{6} \\ 
     \hline
    \epsdice{6}\epsdice{1} & \epsdice{6}\epsdice{2} & \epsdice{6}\epsdice{3} & \epsdice{6}\epsdice{4} & \epsdice{6}\epsdice{5} & \epsdice{6}\epsdice{6} \\ 
     \hline


    \end{tabular}
    \end{adjustbox}
    \end{table}
    \end{landscape}
    \end{document}

