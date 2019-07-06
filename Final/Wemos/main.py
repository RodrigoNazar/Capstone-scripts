import time
import mpu6050
import micropython
from hcsr04 import HCSR04
from PID import PID
from machine import UART, freq, Pin
from Mediana import Mediana

freq(160000000)
micropython.alloc_emergency_exception_buf(100)

######################## Iniciar UART #########################################

uart = UART(0)  # init with given baudrate
uart.init(57600, bits=8, parity=None, stop=1)  # init with given parameters

########################### Instanciar filtros ################################
roll = PID(kp=0.5 + 1 + 0.5+.2+0.5, ki=0.146 + .2 + 0.5, kd=0.25 + 0.05, ref=0, ilim=(-10, 10))
gyro_roll = PID(kp=0.2 + 0.1, ki=0.017+0.02, kd=0.021, ref=0, ilim=(-10, 10))
pitch = PID(kp=0.5 + 0.3 + 0.7 + 0.5, ki=0.146 + 1.9 + 0.3 + 0.2, kd=0.25 + 0.2, ref=0, ilim=(-10, 10))
gyro_pitch = PID(kp=0.2 , ki=0.017 + 0.06, kd=0.021, ref=0, ilim=(-10, 10))

mediana_roll = Mediana(n=5)
mediana_gyro_roll = Mediana(n=3)
mediana_pitch = Mediana(n=5)
mediana_gyro_pitch = Mediana(n=3)

####################### Pines de interrupcion #################################
d3 = Pin(0, Pin.IN, Pin.PULL_UP)  #D3 interrupcion boton
d5 = Pin(14, Pin.IN, Pin.PULL_UP) #D5
d6 = Pin(12, Pin.IN, Pin.PULL_UP) #D6
d7 = Pin(13, Pin.IN, Pin.PULL_UP) #D7
d8 = Pin(15, Pin.IN, Pin.PULL_UP) #D8

####################### Funciones de interrupcion #############################

interrupcion_d3 = False
interrupcion_d5 = False
interrupcion_d6 = False
interrupcion_d7 = False
interrupcion_d8 = False

def int_d3(v):
    global interrupcion_d3
    interrupcion_d3 = True

def int_d5(v):
    global interrupcion_d5
    interrupcion_d5 = True

def int_d6(v):
    global interrupcion_d6
    interrupcion_d6 = True

def int_d7(v):
    global interrupcion_d7
    interrupcion_d7 = True

def int_d8(v):
    global interrupcion_d8
    interrupcion_d8 = True

d3.irq(handler=int_d3, trigger=Pin.IRQ_FALLING)
d5.irq(handler=int_d5, trigger=Pin.IRQ_FALLING)
d6.irq(handler=int_d6, trigger=Pin.IRQ_FALLING)
d7.irq(handler=int_d7, trigger=Pin.IRQ_FALLING)
d8.irq(handler=int_d8, trigger=Pin.IRQ_FALLING)

############################# LED para indicar calibracion ####################

led = Pin(2, Pin.OUT)
led.value(1)

############################ Funcion para el ESC malo ########################

def cambio_duty(x):
    if x <= 43:
        return x
    return round(1.5249 * x - 16.222)

############################ Funcion saturacion ###############################

def sat(valor, a=50, b=190):
    if a < valor < b:
        return valor
    elif valor <= a:
        return a
    else:
        return b

########################### Variables globales ################################

pwmi = 100
ref_altura = 5 # en cm

########################### Funciones desatadas por int #######################

def int_desatada_d3():
    led.value(0)
    uart.write(bytes([7]))
    uart.write(bytes([42]))
    time.sleep(5)
    led.value(1)

def int_desatada_d5():
    global pwmi
    if pwmi < 190:
        pwmi += 1

def int_desatada_d6():
    global pwmi
    if pwmi > 42:
        pwmi -= 1

def int_desatada_d7():
    global ref_altura
    if ref_altura < 120:
        ref_altura += 10

def int_desatada_d8():
    global ref_altura
    if ref_altura > 20:
        ref_altura -= 10

######################## Iniciar sensores #####################################

# sensor = HCSR04(trigger_pin=14, echo_pin=12) # cambiar pines
mpu = mpu6050.MPU()

####################### Calibrar e iniciar ####################################

calibrado = mpu.calibrate()
if calibrado:
    led.value(0)
    time.sleep(6)
    led.value(1)
    uart.write(bytes([0]))
    time.sleep(5)
    led.value(0)
    uart.write(bytes([7]))
    uart.write(bytes([pwmi]))
else:
    while True:
        led.value(0)
        time.sleep(0.125)
        led.value(1)
        time.sleep(0.125)


####################### Ciclo principal #######################################

while True:
    if interrupcion_d3:
        int_desatada_d3()
        interrupcion_d3 = False

    if interrupcion_d5:
        int_desatada_d5()
        interrupcion_d5 = False

    if interrupcion_d6:
        int_desatada_d6()
        interrupcion_d6 = False

    if interrupcion_d7:
        int_desatada_d7()
        interrupcion_d7 = False

    if interrupcion_d8:
        int_desatada_d8()
        interrupcion_d8 = False

    medicion = mpu.read_position()
    filtro = medicion[0]
    if -0.1 < filtro[0] < 0.1:
        filtro[0] = 0
    if -0.7 < filtro[1] < 0.7:
        filtro[1] = 0
    mediana_pitch.add(filtro[0])
    mediana_roll.add(filtro[1])
    gyro_rate = mpu.read_sensors_scaled()[4:7]
    mediana_gyro_roll.add(gyro_rate[1])
    mediana_gyro_pitch.add(gyro_rate[0])

    d = pitch.calcular(mediana_pitch.medicion(), mediana_gyro_pitch.medicion())
    gyro_pitch.ref = d
    d = gyro_pitch.calcular(mediana_gyro_pitch.medicion())
    pwm1 = sat(cambio_duty(pwmi + round(d / 2)))
    pwm2 = sat(pwmi - round(d / 2))
    uart.write(bytes([1]))
    uart.write(bytes([pwm1]))
    uart.write(bytes([2]))
    uart.write(bytes([pwm2]))

    d = roll.calcular(mediana_roll.medicion(), mediana_gyro_roll.medicion())
    gyro_roll.ref = d
    d = gyro_roll.calcular(mediana_gyro_roll.medicion())

    pwm3 = sat(pwmi - round(d / 2))
    pwm4 = sat(pwmi + round(d / 2))
    uart.write(bytes([3]))
    uart.write(bytes([sat(pwm3)]))
    uart.write(bytes([4]))
    uart.write(bytes([sat(pwm4)]))
