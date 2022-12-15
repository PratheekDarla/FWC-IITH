#include <Arduino.h>

byte filter;
byte saw;
byte sqr;
int sine;
int angle;

void setup() {
  Serial.begin(19200);
}

void loop() {
  delay(5);
  saw_square_gen();
  filter_lowpass();
  sine_gen();

  //Comment out one the below Serial.println() waveform you want to plot (one at a time):
  //Serial.println(saw);
  //Serial.println(sqr);
  //Serial.println(filter);
  Serial.println(sine);
}

void saw_square_gen() {     //SAW & SQUARE WAVE GEN
  saw = saw + 1;
  if (saw > 127 && saw < 256) sqr = 255; else sqr = 1;
}

void sine_gen() {            //SINE WAVE GEN
  angle = angle + 1;  if (angle > 360) angle = 0;
  //sine = 50 * sin((angle * PI / 180));
  sine = 50 * sin(angle * 0.0174532925);
  //sine = abs(sine);
}

void filter_lowpass() {      //DIGITAL FILTER
  filter = filter * 0.9 + sqr * 0.1;
}

