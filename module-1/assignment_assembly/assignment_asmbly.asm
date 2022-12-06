.include "/sdcard/Download/iith_Prath/assignment_assembly/m328Pdef.inc"

ldi r16, 0b11000011 ; identifying input pins 2,3,4,5
out DDRD,r16	; declaring pins as input
	
ldi r16, 0b00100000 ;identifying output pin 13
out DDRB,r16		;declaring pins as output

Start:

ldi r17, 0b11111111 ;
out PORTD,r17		; activating internal pullup for pins 2,3,4,5  
in r17, PIND

ldi r18, 0b00000100
mov r19, r17
and r19, r18

ldi r20, 0b00000010
rcall loop1         ; r19: A

ldi r21, 0b00001000
mov r22, r17
and r22, r21

ldi r23, 0b00000011
rcall loop2        ; r22: B

ldi r24, 0b00010000
mov r25, r17
and r25, r24

ldi r26, 0b00000100
rcall loop3      ; r25: C

ldi r27, 0b00100000
mov r28, r17
and r28, r27

ldi r29, 0b00000101
rcall loop4       ; r28: D

mov r5,r19
com r5  ; A'

mov r6, r25
com r6   ; C'

mov r7, r28
com r7 ; D'

mov r1, r22
and r1, r25  ; B.C

mov r2, r19
and r2, r22 ; A.B
and r2, r7  ; A.B.D'

and r5, r6
and r5, r28 ; A'.C'D

or r1,r2
or r1,r5

ldi r30, 0b00000101	;counter = 5
rcall loopw  ;calling the loopw routine

out PORTB, r1		;writing output to pin 13

rjmp Start

;loop for bit shifting
loop1: lsr r19
	dec r20
	brne loop1
	ret

;loop for bit shifting
loop2: lsr r22
	dec r23
	brne loop2

loop3: lsr r25
	dec r26
	brne loop3
	ret

loop4: lsr r28
	dec r29
	brne loop4
	ret

loopw:	lsl r1			;left shift
	dec r30			;counter --
	brne loopw	;if counter != 0
	ret

;comp:
;	mov r0,A			;using r0 for computations
;	ldi A,0b00000001	;loading 1
;	
;	eor A,r0			;A'=A XOR 1
;	ret 				;returning from comp
	

