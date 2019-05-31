#include <ESP8266WiFi.h>
#define MOTOR1 12
#define MOTOR2 13
#define MOTOR3 0
#define MOTOR4 2
#define MAX 1000
#define MIN 100

void setup() {
  analogWriteFreq(24000);

  pinMode(MOTOR1,OUTPUT);
  pinMode(MOTOR2,OUTPUT);
  pinMode(MOTOR3,OUTPUT);
  pinMode(MOTOR4,OUTPUT);

  analogWrite(MOTOR1,MAX);
  analogWrite(MOTOR2,MAX);
  analogWrite(MOTOR3,MAX);
  analogWrite(MOTOR4,MAX);

  delay(5000);

  for (size_t i = MAX - 1; i > MIN; i--) {
      analogWrite(MOTOR1,i);
      analogWrite(MOTOR2,i);
      analogWrite(MOTOR3,i);
      analogWrite(MOTOR4,i);
  }
}


void loop() {

    analogWrite(MOTOR1,105);
    analogWrite(MOTOR2,105);
    analogWrite(MOTOR3,105);
    analogWrite(MOTOR4,105);

    delay(1000);

    analogWrite(MOTOR1,110);
    analogWrite(MOTOR2,110);
    analogWrite(MOTOR3,110);
    analogWrite(MOTOR4,110);

    delay(1000);

    analogWrite(MOTOR1,100);
    analogWrite(MOTOR2,100);
    analogWrite(MOTOR3,100);
    analogWrite(MOTOR4,100);

    delay(1000);
}
