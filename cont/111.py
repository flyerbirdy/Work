  
import RPi.GPIO as GPIO  
import time  
import signal  
import atexit  
  
atexit.register(GPIO.cleanup)    
  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(12, GPIO.OUT)  
p = GPIO.PWM(12,50) #50HZ  
p.start(0)  
time.sleep(2)  



p.ChangeDutyCycle(2.5)
time.sleep(1)

p.ChangeDutyCycle(6.25)
time.sleep(1)
p.ChangeDutyCycle(2.5)

