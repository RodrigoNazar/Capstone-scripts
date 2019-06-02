#include <PWM.h>
#define F_CPU 16000000UL

int motor1 = 9;
int motor2 = 3;
int32_t frequency = 24000;

#define MAX 170
#define MIN 30

void setup()
{
  //initialize all timers except for 0, to save time keeping functions
  InitTimersSafe();
  Serial.begin(9600);

  //sets the frequency for the specified pin
  bool success1 = SetPinFrequencySafe(motor1, frequency);
  bool success2 = SetPinFrequencySafe(motor2, frequency);
  //while(!(success1 & success2));

}


void loop()
{
  //use this functions instead of analogWrite on 'initialized' pins
  pwmWrite(motor1, MAX);
  pwmWrite(motor2, MAX);
  Serial.println("Calibracion en 6s");
  delay(6000);

  Serial.println("Empezando calib");
  
  for (int i = MAX - 1; i > MIN; i--) {
    pwmWrite(motor1, i);
    pwmWrite(motor2, i);
    delay(1);
  }
  
  /*for (int i = MAX - 1; i > MIN; i--) {
    pwmWrite(motor2, i);
    delay(1);
  }*/
  
  Serial.println("listo");

  int f = MIN;
  int d = 1;

  delay(3000);
  while(1){
    Serial.println(f);

    pwmWrite(motor1, f);
    pwmWrite(motor2, f);
    f = f + d;
    if (f == MAX-120){
      f = MIN;
      pwmWrite(motor1, f);
      pwmWrite(motor2, f);
      delay(3000);
      f = MIN + 1;
    }
    delay(1000);

  }
}
