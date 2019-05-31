// #include <ESP8266WiFi.h>
#define MOTOR1 5
#define MOTOR2 6
#define MOTOR3 9
#define MOTOR4 10
#define MAX 700
#define MIN 200

void setup() {
  // analogWriteFreq(24000);

  Serial.begin(9600);
  pinMode(MOTOR1,OUTPUT);
  pinMode(MOTOR2,OUTPUT);
  pinMode(MOTOR3,OUTPUT);
  pinMode(MOTOR4,OUTPUT);
}


void loop() {
    analogWrite(MOTOR1,MAX);
    analogWrite(MOTOR2,MAX);
    analogWrite(MOTOR3,MAX);
    analogWrite(MOTOR4,MAX);

    Serial.println("hola espera 5s");
    delay(9000);
    Serial.println("emp");


    for (int i = MAX - 1; i > MIN; i--) {
    analogWrite(MOTOR1,i);
    analogWrite(MOTOR2,i);
    analogWrite(MOTOR3,i);
    analogWrite(MOTOR4,i);
    delay(1);
    }

//    analogWrite(MOTOR1,MIN);
//    analogWrite(MOTOR2,MIN);
//    analogWrite(MOTOR3,MIN);
//    analogWrite(MOTOR4,MIN);

    Serial.println("calibracion lista");


    while(1){
    analogWrite(MOTOR1,MIN + 5);
    analogWrite(MOTOR2,MIN + 5);
    analogWrite(MOTOR3,MIN + 5);
    analogWrite(MOTOR4,MIN + 5);

    delay(1000);

    analogWrite(MOTOR1,MIN + 10);
    analogWrite(MOTOR2,MIN + 10);
    analogWrite(MOTOR3,MIN + 10);
    analogWrite(MOTOR4,MIN + 10);

    delay(1000);

    analogWrite(MOTOR1,MIN);
    analogWrite(MOTOR2,MIN);
    analogWrite(MOTOR3,MIN);
    analogWrite(MOTOR4,MIN);

    delay(1000);
    }
}
