#!/usr/bin/python

import os 
import re
from functools import cmp_to_key

output = open('content.tex', 'w')

def compare_strs(a, b):
    try:
        af = float(re.match(r"(?:.*/|^)([^/_]*)_", a).group(1))
    except:
        af = 0.0
    
    try:
        bf = float(re.match(r"(?:.*/|^)([^/_]*)_", b).group(1))
    except:
        bf = 0.0

    print(a,b,af,bf)

    if af > bf:
        return 1    
    elif af < bf:
        return -1
    else:
        return 0


def Problem_ID():
    ID = 1
    while True:
        yield ID
        ID += 1

Problem_ID_generator = Problem_ID()

def set_problem(directory, problem):
    ID = next(Problem_ID_generator)
    output.write( '\n\n' )
    output.write( r"\refstepcounter{ID}" + '\n' )
    output.write( r"\setcounter{fid}{0}" + '\n' )
    output.write( r"\graphicspath{{" + str(directory) + "/}}" + '\n')
    output.write( r"\noindent" + '\n' )
    output.write( r"\input{" + problem + "}\n" )
    output.write( r"\vspace*{\ProblemSep}" + '\n' )
    output.write( r"\goodbreak" + '\n' )

sections = sorted ( [ f.path for f in os.scandir(".") if f.is_dir() ], key=cmp_to_key(compare_strs) )

for section in sections:
    if ".git" in section: continue
    if "xcircuit" in section: continue
    if ".vscode" in section: continue
    if "appendix" in section: continue
    f = open(section + "/title.tex", "r")
    title = f.read() 
    output.write( r"\section{" + title + r"}" + '\n' )
    print( r"\section{" + title + r"}" )
    f.close()
    
    #subsections = sorted ( [ f.path for f in os.scandir(section) if f.is_dir() ] )
    subsections = sorted([ f.path for f in os.scandir(section) if f.is_dir() ], key=cmp_to_key(compare_strs))

    if subsections == []:
        continue

    for subsection in subsections:
        f = open(subsection + "/title.tex", "r")
        title = f.read() 
        output.write( r"\subsection{" + title + r"}" + '\n' )
        print( r"\subsection{" + title + r"}" )
        f.close()

        problems = sorted ( [ f.path for f in os.scandir(subsection) if f.is_file() ] , key=cmp_to_key(compare_strs) )
        
        for problem in problems:
            if "title.tex" in problem: continue
            set_problem(subsection, problem)
            print (problem)
        

output.write(r"\appendix" + '\n')


for section in sections:
    if not "appendix" in section: continue
    
    output.write( r"\appendix" + '\n' )
    output.write( r"\graphicspath{{" + str(section) + "/}}" + '\n')
    output.write( r"\counterwithin{figure}{chapter}" + '\n' )
    output.write( r"\counterwithin{equation}{chapter}" + '\n' )
    
    #print( r"\section{" + title + r"}" )

    topics = sorted ( [ f.path for f in os.scandir(section) if f.is_file() ] , key=cmp_to_key(compare_strs) )

    if topics == []:
        continue

    for topic in topics:
        output.write( r"\input{" + topic + r"}" + '\n' )
        


output.close()


