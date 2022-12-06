//Code for boolean equation: Y = B.C + A.B.D' + A'.C'.D

#include <avr/io.h>
#include <stdbool.h>
 
int main (void)
{
bool A=0,B=0,C=0,D=0, Y=0;

// set pin 2,3,4,5 of arduino as input
DDRD = 0b00111100 ;	

//set PB5, pin 13 of arduino as output
DDRB |= ((1 << DDB5));

PORTD = 0b11000000;
//PORTB = 0b00000000;
	
   while (1) {
	Y = (B && C) || (A && B && (!D))  || ((!A) && (!C) && D);

	A = (PIND & (1 << PIND2)) == (1 << PIND2);
	B = (PIND & (1 << PIND3)) == (1 << PIND3);
	C = (PIND & (1 << PIND4)) == (1 << PIND4);
	D = (PIND & (1 << PIND5)) == (1 << PIND5);

     	PORTB |= (Y << 5);
  }

  /* . */
  return 0;
}
