#include <Arduino.h>
int X;
int A,B,C,D;

void setup() {
    pinMode(13, OUTPUT);
    pinMode(2, INPUT);  
    pinMode(3, INPUT);
    pinMode(4, INPUT);
    pinMode(5, INPUT);
    
}

// the loop function runs over and over again forever
void loop() { 

A = digitalRead(2);//LSB  
B = digitalRead(3);  
C = digitalRead(4);  
D = digitalRead(5);//MSB  
  
X= (B&&C) || (A&&B&&!D) || (!A&&!C&&D);

digitalWrite(13, X);
}

