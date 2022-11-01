#!/bin/bash


#Download python and latex templates

#svn co https://github.com/gadepall/training/trunk/math/sdcard/Download/math

#Test Latex Installation
#Uncomment only the following lines and comment the above line

cd /sdcard/Download/iith_Prath/assignment/codes
pio run

cd /sdcard/Download/iith_Prath/assignment 
texfot pdflatex assignment_ide.tex
termux-open assignment_ide.pdf
