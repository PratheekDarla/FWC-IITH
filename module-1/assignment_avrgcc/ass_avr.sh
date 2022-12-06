# shel script for AVR_GCC assigment

cd /sdcard/Download/iith_Prath/assignment_avrgcc
make

#rm *.hex

texfot pdflatex assignment_avrgcc.tex
termux-open assignment_avrgcc.pdf
