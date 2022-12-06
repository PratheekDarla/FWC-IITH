# Shell script for Assembly assignment

cd /home/user/iith/assembly/assignment_assembly
avra assignment_asmbly.asm 
#avrdude -p atmega328p -c arduino -P /dev/ttyACM0 -b 115200 -U flash:w:assignment_asmbly.hex

texfot pdflatex assignment_asmbly.tex
termux-open assignment_asmbly.pdf
