
import sys
import RPi.GPIO   
import time
import os
from flask import Flask, render_template, Response, request
import signal
import atexit

from getcpu import *

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera




RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(18,RPi.GPIO.OUT)
RPi.GPIO.setup(23,RPi.GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def main():
        return render_template("main.html")




def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')






        
@app.route("/on")
def ledon():
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setup(18,RPi.GPIO.OUT)
        RPi.GPIO.setup(23,RPi.GPIO.OUT)
      
        RPi.GPIO.output(23,True)
                
        return render_template("main.html")

@app.route("/off")
def ledoff():
    
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setup(18,RPi.GPIO.OUT)
        RPi.GPIO.setup(23,RPi.GPIO.OUT)
    
    
        RPi.GPIO.output(23,False)         
        RPi.GPIO.cleanup()

        return render_template("main.html")


@app.route("/shining")
def shining():
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setup(18,RPi.GPIO.OUT)
        RPi.GPIO.setup(23,RPi.GPIO.OUT)
        
        pwm = RPi.GPIO.PWM(23,180)
        pwm.start(0)
        for i in range(0,5):
            for x in range (0,101,1):
                pwm.ChangeDutyCycle(x)
                time.sleep(.02)

            for x in range(100,-1,-1):
                pwm.ChangeDutyCycle(x)
                time.sleep(.02)
        pwm.stop()       
        RPi.GPIO.cleanup()
                                
        return render_template("main.html")

@app.route("/cpu")
def cpu():

    
    return CPU_temp


@app.route('/cmd',methods=['POST'])
def cmd():

    atexit.register(RPi.GPIO.cleanup)    
    RPi.GPIO.setmode(RPi.GPIO.BCM)  
    RPi.GPIO.setup(12, RPi.GPIO.OUT)  
    RPi.GPIO.setup(21, RPi.GPIO.OUT)
    b = RPi.GPIO.PWM(21,50)
    p = RPi.GPIO.PWM(12,50) #50HZ  
    p.start(0) 
    b.start(0)
    time.sleep(2)  
    cont = str(request.get_data())
    
    if "left" in cont:
        atexit.register(RPi.GPIO.cleanup)
        p.ChangeDutyCycle(5)
        time.sleep(1)

    if "right" in cont:
        
        atexit.register(RPi.GPIO.cleanup)
        p.ChangeDutyCycle(10)
        time.sleep(1)

    if "up" in cont:
        atexit.register(RPi.GPIO.cleanup)
        b.ChangeDutyCycle(5)
        time.sleep(1)



    if "down" in cont:
        atexit.register(RPi.GPIO.cleanup)
        b.ChangeDutyCycle(10)
        time.sleep(1)











    return request.get_data()







@app.route('/video_feed')


def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')





if __name__ == "__main__":
    app.run(host="0.0.0.0",port=1111)
