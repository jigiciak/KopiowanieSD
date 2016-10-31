from subprocess import call
import os.path
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.setup(31, GPIO.OUT)

# Pozostale piny ustawic
GPIO.output(19,True)
GPIO.output(21,False)
if not os.path.exists("/dev/sda1"):
	GPIO.output(31,False)
flag_sda1 = 1

#GPIO.cleanup()

while(1):
		if os.path.exists("/dev/sda1") and flag_sda1 == 1:
			GPIO.output(31,True)
			time.sleep(1)
			GPIO.output(19,False)
			GPIO.output(21,True)
			call(['bash', '/home/pi/Desktop/Zgrywanie_SD/sda1'])
			time.sleep(0.1)
			GPIO.output(21,False)
			GPIO.output(19,True)
			print "sda1"
			flag_sda1 = 0
		elif not os.path.exists("/dev/sda1") and flag_sda1==0:
			flag_sda1 = 1
			time.sleep(0.5)
		# elif not os.path.exists("/dev/sda1"):
			GPIO.output(31,False)
		time.sleep(1)
