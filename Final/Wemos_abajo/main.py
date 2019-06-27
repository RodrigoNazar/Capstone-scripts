import time
import mpu6050
import micropython
from hcsr04 import HCSR04

micropython.alloc_emergency_exception_buf(100)

sensor = HCSR04(trigger_pin=14, echo_pin=12)

mpu = mpu6050.MPU()
mpu.calibrate()


while 1:

    init = time.ticks_ms()
    medicion = mpu.read_position()
    filtro = medicion[0]
    distance = sensor.distance_cm()

    a = 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a *= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2
    a /= 2

    print(filtro[0])
    print(filtro[1])
    print(distance)
