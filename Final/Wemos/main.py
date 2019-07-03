import time
import mpu6050
import micropython
from hcsr04 import HCSR04
from PID import PID
from machine import UART, freq, Pin
from Mediana import Mediana

freq(160000000)
micropython.alloc_emergency_exception_buf(100)

mediana_roll = Mediana()
mediana_pitch = Mediana()

led = Pin(2, Pin.OUT)
led.value(1)

# roll = PID(kp=0.135 + .1, ki=.2251, kd=0.0343, ref=0, ilim=(-10, 10))
roll = PID(kp=.01, ki=.0, kd=.0, ref=0, ilim=(-10, 10))

# pitch = PID(kp=0.5 * .45, ki=1.18 * .5 / .806, kd=0.074 * .5 * .806, ref=0, ilim=(-10, 10))
pitch = PID(kp=0.1, ki=0, kd=0, ref=0, ilim=(-10, 10))

# gyro_roll = PID(kp=0.7, ki=0, kd=0, ref=0, ilim=(-10, 10))
# gyro_pitch = PID(kp=0.7, ki=0, kd=0, ref=0, ilim=(-10, 10))

# D3 interrupcion boton
p0 = Pin(0, Pin.IN, Pin.PULL_UP)

pwmi = 140
subir = True


def cambio_duty(x):
    if x <= 43:
        return x

    return round(1.5249 * x - 16.222)


def algo_super_bacan():
    global pwmi
    global subir
    led.value(0)
    # uart.write(bytes([7]))
    # uart.write(bytes([100]))
    # time.sleep(.2)
    # uart.write(bytes([7]))
    # uart.write(bytes([70]))
    # time.sleep(.2)
    # uart.write(bytes([7]))
    # uart.write(bytes([50]))
    # time.sleep(.2)
    uart.write(bytes([6]))
    uart.write(bytes([42]))
    roll.reset()
    pitch.reset()
    roll.kp += 0.1
    pitch.kp += 0.1
    if subir:
        roll.kp += 0.01
        pitch.kp += 0.01
        # pwmi += 10
    else:
        roll.kp -= 0.01
        pitch.kp -= 0.01
        # pwmi -= 10

    # if pwmi == 190:
    #     subir = False
    # elif pwmi == 60:
    #     subir = True
    if roll.kp == 1:
        subir = False
    elif roll.kp == .1:
        subir = True

    time.sleep(5)
    led.value(1)


interrupcion = False


def f_int(v):
    global interrupcion
    interrupcion = True


p0.irq(handler=f_int, trigger=Pin.IRQ_FALLING)


def sat(valor, a=50, b=190):
    if a < valor < b:
        return valor
    elif valor <= a:
        return a
    else:
        return b


uart = UART(0)  # init with given baudrate
uart.init(57600, bits=8, parity=None, stop=1)  # init with given parameters

sensor = HCSR04(trigger_pin=14, echo_pin=12)

mpu = mpu6050.MPU()
mpu.calibrate()
print('\n\n\t\tConecta los ESC\n\n')
led.value(0)
time.sleep(5)

led.value(1)

uart.write(bytes([0]))
time.sleep(5)

uart.write(bytes([6]))
uart.write(bytes([pwmi]))

while True:
    if interrupcion:
        algo_super_bacan()
        interrupcion = False

    medicion = mpu.read_position()
    filtro = medicion[0]
    mediana_pitch.add(filtro[0])
    mediana_roll.add(filtro[1])
    # gyro_rate = mpu.read_sensors_scaled()[4:7]
    # distance = sensor.distance_cm()
    # d = pitch.calcular(filtro[0])
    d = pitch.calcular(mediana_pitch.medicion())
    # gyro_pitch.ref = d1
    # d = gyro_pitch.calcular(gyro_rate[0])

    # pwm1 = sat(cambio_duty(pwmi + round(d / 2)))
    # pwm2 = sat(pwmi - round(d / 2))
    # uart.write(bytes([1]))
    # uart.write(bytes([sat(cambio_duty(pwm1))]))
    # uart.write(bytes([2]))
    # uart.write(bytes([sat(pwm1)]))

    # d = roll.calcular(filtro[1])
    d = roll.calcular(mediana_roll.medicion())
    # print('control1: ', d1)
    # gyro_roll.ref = d1
    # d = gyro_roll.calcular(gyro_rate[1])
    # print('control2: ', d)

    pwm3 = sat(pwmi - round(d / 2))
    pwm4 = sat(pwmi + round(d / 2))
    uart.write(bytes([3]))
    uart.write(bytes([sat(pwm3)]))
    uart.write(bytes([4]))
    uart.write(bytes([sat(pwm4)]))
