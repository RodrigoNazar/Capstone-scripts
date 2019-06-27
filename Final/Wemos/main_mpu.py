import time
import mpu6050
import micropython

micropython.alloc_emergency_exception_buf(100)


mpu = mpu6050.MPU()

while 1:
    init = time.ticks_ms()
    medicion = mpu.read_position()
    filtro = medicion[0]
    gyro = medicion[2]

    # print('x:\t\t', filtro[0], 'y:\t\t', filtro[1], 'z:\t\t', filtro[2])
    #
    # print('\nGyroo:\t\t', gyro)

    print('Tiempo:', 1000/(time.ticks_ms()-init))

    time.sleep(.2)
