from subprocess import call
import os.path
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

GPIO.setup(33, GPIO.OUT)

# Pozostale piny ustawic
GPIO.output(7,True)
GPIO.output(11,False)
if not os.path.exists("/dev/sdb1"):	
	GPIO.output(33,False)
flag_sdb1 = 1

#GPIO.cleanup()

while(1):
		if os.path.exists("/dev/sdb1") and flag_sdb1 == 1:
			GPIO.output(33,True)
			time.sleep(1)
			GPIO.output(7,False)
			GPIO.output(11,True)
			call(['bash', '/home/pi/Desktop/Zgrywanie_SD/sdb1'])
			time.sleep(0.1)
			GPIO.output(11,False)
			GPIO.output(7,True)
			print "sdb1"
			flag_sdb1 = 0
		elif not os.path.exists("/dev/sdb1") and flag_sdb1==0:
			flag_sdb1 = 1
			time.sleep(0.5)
		# elif not os.path.exists("/dev/sdb1"):
			GPIO.output(33,False)
		time.sleep(1)
