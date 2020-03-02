import board
import digitalio
import busio
import adafruit_si7021
import adafruit_mpl3115a2
import adafruit_lis3mdl
import adafruit_lsm6ds
import board
import neopixel
import time
import adafruit_gps

SL_PRESSURE=101490
TEAL=(12,45,64)
GREEN=(0,255,0)

pixels=neopixel.NeoPixel(board.D18, 7)

pixels.fill(TEAL)



print ("starting system check...")

# digitalio test
pin=digitalio.DigitalInOut(board.D4)
print("Digitalio ok")
pixels.fill(GREEN)
time.sleep(0.25)
pixels.fill(TEAL)

# I2C test
i2c=busio.I2C(board.SCL,board.SDA)
print("i2c ok")
pixels.fill(GREEN)
time.sleep(0.25)
pixels.fill(TEAL)

humid_sensor=adafruit_si7021.SI7021(i2c)
print ("Temp_1={} C".format(humid_sensor.temperature))
print ("humidity={} %".format(humid_sensor.relative_humidity))
print("si7021 sensor array OK.")
pixels.fill(GREEN)
time.sleep(0.25)
pixels.fill(TEAL)

alt_sensor=adafruit_mpl3115a2.MPL3115A2(i2c)
alt_sensor.sealevel_pressure=SL_PRESSURE
print ("pressure={0:0.3f} pascals".format(alt_sensor.pressure))
print ("altitude={0:0.3f} meters".format(alt_sensor.altitude))
print ("altitude sensor array OK.")
pixels.fill(GREEN)
time.sleep(0.25)
pixels.fill(TEAL)

comp_sensor=adafruit_lis3mdl.LIS3MDL(i2c)
magx,magy,magz=comp_sensor.magnetic
print ("X={0:10.2f} Y={1:10.2f} Z={2:10.2f}".format(magx,magy,magz))
print ("Compass OK.")
pixels.fill(GREEN)
time.sleep(0.25)
pixels.fill(TEAL)

sox_sensor=adafruit_lsm6ds.LSM6DS33(i2c)
accx,accy,accz=sox_sensor.acceleration
print ("X={0:10.2f} Y={1:10.2f} Z={2:10.2f}".format(accx,accy,accz))
print ("accelerometers OK.")
pixels.fill(GREEN)
time.sleep(0.25)
pixels.fill(TEAL)

gyrox,gyroy,gyroz=sox_sensor.gyro
print ("X={0:10.2f} Y={1:10.2f} Z={2:10.2f}".format(gyrox,gyroy,gyroz))
print ("gyrometer OK.")
pixels.fill(GREEN)
time.sleep(0.25)
pixels.fill(TEAL)

gps=adafruit_gps.GPS_GtopI2C(i2c)
print ("gps={}".format(gps.readline()))
print ("lat={}".format(gps.latitude))
print ("lon={}".format(gps.longitude))
print ("gps OK.")
pixels.fill(GREEN)
time.sleep(0.25)
pixels.fill(TEAL)

print ("DONE!")
pixels.fill ((204,103,1))
