Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from gpiozero import LED
from time import sleep
red = LED(25)
amber = LED(8)
green = LED(7)
green.on()
amber.off()
red.off()
while True:
sleep(10)
green.off()
amber.on()
sleep(1)
amber.off()
red.on()
sleep(10)
amber.on()
sleep(1)
green.on()
amber.off()
red.off()
