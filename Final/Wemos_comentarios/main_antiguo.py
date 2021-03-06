import utime
from machine import I2C, Pin, freq
from mpu9250 import MPU9250
from mpu6500 import MPU6500, SF_G, SF_DEG_S, GYRO_FS_SEL_1000DPS
# import ADXL345 as ADXL345
import math

freq(160000000)

i2c = I2C(scl=Pin(5, Pin.PULL_UP), sda=Pin(4, Pin.PULL_UP), freq=400000)
mpu6500 = MPU6500(i2c, gyro_sf=SF_DEG_S)
sensor = MPU9250(i2c, mpu6500=mpu6500)
# adx = ADXL345.ADXL345(i2c)
print()

print('\nOFSET', sensor.mpu6500.calibrate())
sensor.mpu6500.calibrate(delay=10)
print("MPU9250 id: " + hex(sensor.whoami))

angx = 0
angy = 0
angz = 0
dt2 = 0
gy1 = (0, 0, 0)
gy2 = (0, 0, 0)

accelerationX = sensor.acceleration[0]
accelerationY = sensor.acceleration[1]
accelerationZ = sensor.acceleration[2]

pitch0 = 180 * math.atan(accelerationX/math.sqrt(accelerationY *
                                                 accelerationY + accelerationZ*accelerationZ))/math.pi
roll0 = 180 * math.atan(accelerationY/math.sqrt(accelerationX *
                                                accelerationX + accelerationZ*accelerationZ))/math.pi

yaw0 = 180 * math.atan(accelerationZ/math.sqrt(accelerationX *
                                               accelerationX + accelerationZ*accelerationZ))/math.pi

# x0 = adx.xValue
# y0 = adx.yValue
# z0 = adx.zValue


while True:
    # tic = utime.ticks_us()
    # print('\nNueva Medicion\n')
    # print(math.sqrt(sensor.acceleration[0]**2 +
    #                 sensor.acceleration[1]**2 +
    #                 sensor.acceleration[2]**2))

    accelerationX = sensor.acceleration[0]
    accelerationY = sensor.acceleration[1]
    accelerationZ = sensor.acceleration[2]

    pitch = 180 * math.atan(accelerationX/math.sqrt(accelerationY *
                                                    accelerationY + accelerationZ*accelerationZ))/math.pi
    roll = 180 * math.atan(accelerationY/math.sqrt(accelerationX *
                                                   accelerationX + accelerationZ*accelerationZ))/math.pi

    yaw = 180 * math.atan(accelerationZ/math.sqrt(accelerationX *
                                                  accelerationX + accelerationZ*accelerationZ))/math.pi

    print('\npitch: ', pitch-pitch0, end='')
    print('\troll: ', roll-roll0, end='')
    print('\tyaw: ', yaw-yaw0)
    # print('aceleracion:', sensor.acceleration)
    # print('giro:', sensor.gyro)
    # gy2 = sensor.gyro
    # dt = utime.ticks_us() - tic

    ''' Integración Mathi
    # angx += (gy2[0]+gy1[0])*(dt+dt2)/2000000
    # angy += (gy2[1]+gy1[1])*(dt+dt2)/2000000
    # angz += (gy2[2]+gy1[2])*(dt+dt2)/2000000
    '''
    # print(angx, angy, angz)

    # x = adx.xValue - x0
    # y = adx.yValue - y0
    # z = adx.zValue - z0
    # print('The Position info of x, y, z are: %d, %d, %d' % (x, y, z))

    # utime.sleep_ms(1000)
    # gy1 = gy2
    # dt2 = utime.ticks_us() - tic - dt
