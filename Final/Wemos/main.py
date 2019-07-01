import time
import mpu6050
import micropython
from hcsr04 import HCSR04
from PID import PID
from machine import UART, freq, Pin

freq(160000000)


def sat(valor, a=50, b=170):
    if a < valor < b:
        return valor
    elif valor <= a:
        return a
    else:
        return b


micropython.alloc_emergency_exception_buf(100)

led = Pin(2, Pin.OUT)
led.value(1)

uart = UART(0)  # init with given baudrate
uart.init(57600, bits=8, parity=None, stop=1)  # init with given parameters

sensor = HCSR04(trigger_pin=14, echo_pin=12)

mpu = mpu6050.MPU()
mpu.calibrate()
print('\n\n\t\tConecta los ESC\n\n')
led.value(0)
time.sleep(5)

roll = PID(kp=2, ki=0, kd=0, ref=0, ilim=(-5, 5))
pitch = PID(kp=2, ki=0, kd=0, ref=0, ilim=(-5, 5))

# gyro_roll = PID(kp=0.7, ki=0, kd=0, ref=0, ilim=(-10, 10))
# gyro_pitch = PID(kp=0.7, ki=0, kd=0, ref=0, ilim=(-10, 10))

pwmi = 70
pwm1 = pwmi
pwm2 = pwmi
pwm30 = pwmi
pwm40 = pwmi

led.value(1)

uart.write(bytes([0]))
time.sleep(5)

uart.write(bytes([6]))
uart.write(bytes([pwmi]))
uart.write(bytes([1]))


while True:
    medicion = mpu.read_position()
    filtro = medicion[0]
    # gyro_rate = mpu.read_sensors_scaled()[4:7]
    # distance = sensor.distance_cm()
    # d1 = pitch.calcular(filtro[0])
    # gyro_pitch.ref = d1
    # d = gyro_pitch.calcular(gyro_rate[0])
    # pwm1 = sat(pwm1 + round(d / 2))
    # pwm2 = sat(pwm2 - round(d / 2))
    # uart.write(bytes([1]))
    # uart.write(bytes([pwm1]))
    # uart.write(bytes([2]))
    # uart.write(bytes([pwm2]))

    d = roll.calcular(filtro[1])
    # print('control1: ', d1)
    # gyro_roll.ref = d1
    # d = gyro_roll.calcular(gyro_rate[1])
    # print('control2: ', d)

    pwm3 = sat(pwm30 - round(d / 2))
    pwm4 = sat(pwm40 + round(d / 2))
    uart.write(bytes([3]))
    uart.write(bytes([pwm3]))
    uart.write(bytes([4]))
    uart.write(bytes([pwm4]))
