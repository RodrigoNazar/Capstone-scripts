from machine import Pin, PWM
import time


class Motores:
    def __init__(self, pin1=12, pin2=13, pin3=0, pin4=2):

        self.max = 1000
        self.min = 100

        self._duty1 = 100
        self._duty2 = 100
        self._duty3 = 100
        self._duty4 = 100

        self.motor1 = PWM(Pin(pin1), freq=24000, duty=self.max)
        self.motor2 = PWM(Pin(pin2), freq=24000, duty=self.max)
        self.motor3 = PWM(Pin(pin3), freq=24000, duty=self.max)
        self.motor4 = PWM(Pin(pin4), freq=24000, duty=self.max)

    def calibracion(self):
        for i in range(self.max-1,self.min-1, -1):
            self.motor1.duty = i
            self.motor2.duty = i
            self.motor3.duty = i
            self.motor4.duty = i

    @property
    def duty1(self):
        return self._duty1

    @duty1.setter
    def duty1(self, x):
        self._duty1 = x
        self.motor1.duty(self._duty1)

    @property
    def duty2(self):
        return self._duty2

    @duty2.setter
    def duty2(self, x):
        self._duty2 = x
        self.motor2.duty(self._duty2)

    @property
    def duty3(self):
        return self._duty3

    @duty3.setter
    def duty3(self, x):
        self._duty3 = x
        self.motor3.duty(self._duty3)

    @property
    def duty4(self):
        return self._duty4

    @duty4.setter
    def duty4(self, x):
        self._duty4 = x
        self.motor4.duty(self._duty4)

    def increase_duty_all(self):
        self.duty1 += 1
        self.duty2 += 1
        self.duty3 += 1
        self.duty4 += 1

    def decrease_duty_all(self):
        self.duty1 -= 1
        self.duty2 -= 1
        self.duty3 -= 1
        self.duty4 -= 1

    def turn_off(self):
        self.duty1 = 0
        self.duty2 = 0
        self.duty3 = 0
        self.duty4 = 0

    def turn_on(self):
        self.duty1 = 58
        self.duty2 = 58
        self.duty3 = 58
        self.duty4 = 51

    def set_duty_motor(self, new_duty, motor):
        motor = int(motor)
        if motor == 1:
            self.motor1.duty(new_duty)
        elif motor == 2:
            self.motor2.duty(new_duty)
        elif motor == 3:
            self.motor3.duty(new_duty)
        elif motor == 4:
            self.motor4.duty(new_duty)

    def test(self):
        self.turn_on()
        for _ in range(5):
            self.increase_duty_all()
            time.sleep(0.5)
        for _ in range(5):
            self.increase_duty_all()
            time.sleep(0.5)
        self.turn_off()
