import time
import mpu6050
import micropython
from hcsr04 import HCSR04
from PID import PID


def sat(valor):
    if 42 < valor < 130:
        return valor
    elif valor <= 42:
        return 42
    else:
        return 130


micropython.alloc_emergency_exception_buf(100)

uart = UART(0)  # init with given baudrate
uart.init(57600, bits=8, parity=None, stop=1)  # init with given parameters

sensor = HCSR04(trigger_pin=14, echo_pin=12)

mpu = mpu6050.MPU()
mpu.calibrate()

roll = PID(kp=1, ki=0.1, kd=0.2)
pitch = PID(kp=1, ki=0.1, kd=0.2)

pwmi = 60
pwm1 = pwmi
pwm2 = pwmi
pwm3 = pwmi
pwm4 = pwmi

uart.write(bytes([0]))
time.sleep(1)

uart.write(bytes([7]))
uart.write(bytes([pwmi]))


while True:
    medicion = mpu.read_position()
    filtro = medicion[0]
    # distance = sensor.distance_cm()
    d = roll.calcular(filtro[0])
    pwm1 = sat(pwm1 + int(d / 2))
    pwm2 = sat(pwm2 - int(d / 2))
    uart.write(bytes([1]))
    uart.write(bytes([pwm1]))
    uart.write(bytes([2]))
    uart.write(bytes([pwm2]))

    d = pitch.calcular(filtro[1])
    pwm3 = sat(pwm3 + int(d / 2))
    pwm4 = sat(pwm4 - int(d / 2))
    uart.write(bytes([3]))
    uart.write(bytes([pwm3]))
    uart.write(bytes([4]))
    uart.write(bytes([pwm4]))


