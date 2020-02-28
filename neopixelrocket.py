import board
import neopixel

pixels=neopixel.NeoPixel(board.D18,30)

pixels[0]=(255,0,0)
pixels[1]=(255,255,0)
pixels[2]=(255,0,255)
pixels[3]=(0,255,255)
pixels[4]=(42,17,76)
pixels[5]=(255,3,231)

