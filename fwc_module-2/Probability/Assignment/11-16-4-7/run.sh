#! /bin/bash
# Bash file for 11-16-4-7


pdflatex $1tex
xdg-open $1pdf

## if using termux
#texfot pdflatex $1tex
#termux-open $1pdf
## end if
