from subprocess import call
import os.path
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)

GPIO.setup(37, GPIO.OUT)

# Pozostale piny ustawic
GPIO.output(23,True)
GPIO.output(29,False)
if not os.path.exists("/dev/sdd1"):	
	GPIO.output(37,False)
flag_sdd1 = 1

#GPIO.cleanup()

while(1):
		if os.path.exists("/dev/sdd1") and flag_sdd1 == 1:
			GPIO.output(37,True)
			time.sleep(1)
			GPIO.output(23,False)
			GPIO.output(29,True)
			call(['bash', '/home/pi/Desktop/Zgrywanie_SD/sdd1'])
			time.sleep(0.1)
			GPIO.output(29,False)
			GPIO.output(23,True)
			print "sdd1"
			flag_sdd1 = 0
		elif not os.path.exists("/dev/sdd1") and flag_sdd1==0:
			flag_sdd1 = 1
			time.sleep(0.5)
		# elif not os.path.exists("/dev/sdd1"):
			GPIO.output(37,False)
		time.sleep(1)
