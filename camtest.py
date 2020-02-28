import subprocess
from pathlib import Path
import time
import os
import neopixel
import board

home_dir = '/home/pi/picam/'
pixels= neopixel.NeoPixel(board.D18,7)

pixels.fill((0,0,255))
time.sleep(0.25)
pixels.fill((255,0,0))
time.sleep(0.25)
pixels.fill((255,255,255))
time.sleep(0.25)
pixels.fill((255,0,0))

os.chdir(home_dir)
camera = subprocess.Popen(['./make_dirs.sh'])
time.sleep(3)
#camera = subprocess.Popen(['./picam','--alsadev','hw:1,0'])

pixels.fill((0,255,0))
Path('./hooks/start_record').touch()

startTime = time.time()
print('Starting to record')

while (time.time() - startTime) < 30:
    pixels.fill((0,255,0))
    if os.path.isfile('./hooks/subtitle'):
        os.remove('./hooks/subtitle')
    with open('./hooks/subtitle','a') as subtitle:
        subtitle.write('text={}'.format(time.time()))
        print('text={}'.format(time.time()))

    time.sleep(0.75)
    pixels.fill((255,255,255))
    time.sleep(0.25)

Path('./hooks/stop_record').touch()
pixels.fill((255,0,0))

camera.kill()
print('Done recording')
