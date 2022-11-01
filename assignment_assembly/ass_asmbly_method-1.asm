.include "/sdcard/Download/iith_Prath/assignment_assembly/m328Pdef.inc"

Start:

.def A = r16
.def B = r17
.def C = r18
.def D = r19
.def Y = r25


ldi A, 0b11000011 ; identifying input pins 2,3,4,5
out DDRD,A
;in A, PIND

ldi A, 0b00100000 ; identifying output pin 13
out DDRB,A		;declaring pins as input



ldi A, 0b00000000 
ldi B, 0b00000000
ldi C, 0b00000000
ldi D, 0b00000000

mov r21,A
com r21  ; A'

mov r22, C
com r22   ; C'

mov r23,D
com r23 ; D'

mov r1,B
and r1,C

mov r2,A
and r2,B
and r2,r23

and r21, r22
and r21, D

or r1,r2
or r1,r21


;rcall comp ; jumping to comp routine below


ldi r20, 0b00000101	;counter = 5

rcall loopw		;calling the loopw routine

out PORTB, r1		;writing output to pins 2,3,4,5



rjmp Start

;loop for bit shifting
loopw:	lsl r1			;left shift
	dec r20			;counter --
	brne	loopw	;if counter != 0
	ret

;comp:
	mov r0,A			;using r0 for computations
	ldi A,0b00000001	;loading 1
	
	eor A,r0			;A'=A XOR 1
	ret 				;returning from comp
	
