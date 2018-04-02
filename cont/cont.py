  
import RPi.GPIO as GPIO  
import time  
import signal  
import atexit  
  
atexit.register(GPIO.cleanup)    
  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(12, GPIO.OUT, initial=False)  
p = GPIO.PWM(12,50) #50HZ  
p.start(0)  
time.sleep(2)  



p.ChangeDutyCycle(90)

while(True):  
  for i in range(0,90,5):  
    p.ChangeDutyCycle(2.5 + 10 * i / 180) #设置转动角度  
    time.sleep(0.02)                      #等该20ms周期结束  
    p.ChangeDutyCycle(0)                  #归零信号  
    time.sleep(0.2)  
    
  for i in range(90,0,-5):  
    p.ChangeDutyCycle(2.5 + 10 * i / 180)  
    time.sleep(0.02)  
    p.ChangeDutyCycle(0)  
    time.sleep(0.2)  
