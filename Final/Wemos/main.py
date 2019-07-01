import time
import micropython
from machine import UART, freq, Pin

freq(160000000)
micropython.alloc_emergency_exception_buf(100)

led = Pin(2, Pin.OUT)
led.value(1)

# D3 interrupcion boton
p0 = Pin(0, Pin.IN, Pin.PULL_UP)

pwmi = 42

inc = True


def cambio_duty(x):
    if x <= 43:
        return x

    return round(1.5249 * x - 16.222)


def sat(valor, a=42, b=100):
    global inc
    if a < valor < b:
        return valor
    elif valor <= a:
        inc = True
        return a
    else:
        inc = False
        return b


def algo_super_bacan():
    global pwmi
    global inc
    led.value(0)
    if inc:
        pwmi += 5
    else:
        pwmi -= 5
    uart.write(bytes([2]))
    uart.write(bytes([sat(pwmi)]))
    uart.write(bytes([1]))
    uart.write(bytes([sat((pwmi))]))
    led.value(1)


interrupcion = False


def f_int(v):
    global interrupcion
    interrupcion = True


p0.irq(handler=f_int, trigger=Pin.IRQ_FALLING)

uart = UART(0)  # init with given baudrate
uart.init(57600, bits=8, parity=None, stop=1)  # init with given parameters

print('\n\n\t\tConecta los ESC\n\n')
led.value(0)
time.sleep(5)

led.value(1)

uart.write(bytes([0]))
time.sleep(9)

uart.write(bytes([6]))
uart.write(bytes([pwmi]))
print('Iniciado')

while True:
    if interrupcion:
        algo_super_bacan()
        interrupcion = False
