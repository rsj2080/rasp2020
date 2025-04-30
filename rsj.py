import RPi.GPIO as GPIO

from time import sleep

LED = 8
Switch = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Switch,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT)


try:
	while True:
		if GPIO.input(Switch) ==GPIO.HIGH:
			GPIO.output(LED, GPIO.HIGH)
			print("LED ON")
			sleep(0.5)
		else:
			GPIO.output(LED, GPIO.LOW)
			print("LED OFF")
			sleep(0.5)
finally:
	GPIO.cleanup()
