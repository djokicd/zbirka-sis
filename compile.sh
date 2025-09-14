#!/bin/bash
rm -f main.aux && python3 generate.py && pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
