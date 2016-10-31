from subprocess import call
import os.path
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.setup(35, GPIO.OUT)

# Pozostale piny ustawic
GPIO.output(13,True)
GPIO.output(15,False)
if not os.path.exists("/dev/sdc1"):	
	GPIO.output(35,False)
flag_sdc1 = 1

#GPIO.cleanup()

while(1):
		if os.path.exists("/dev/sdc1") and flag_sdc1 == 1:
			GPIO.output(35,True)
			time.sleep(1)
			GPIO.output(13,False)
			GPIO.output(15,True)
			call(['bash', '/home/pi/Desktop/Zgrywanie_SD/sdc1'])
			time.sleep(0.1)
			GPIO.output(15,False)
			GPIO.output(13,True)
			print "sdc1"
			flag_sdc1 = 0
		elif not os.path.exists("/dev/sdc1") and flag_sdc1==0:
			flag_sdc1 = 1
			time.sleep(0.5)
		# elif not os.path.exists("/dev/sdc1"):
			GPIO.output(35,False)
		time.sleep(1)
