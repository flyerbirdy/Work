from flask import Flask
import sys
import RPi.GPIO   
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(18,RPi.GPIO.OUT)
RPi.GPIO.setup(4,RPi.GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def ledon():
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setup(18,RPi.GPIO.OUT)
        RPi.GPIO.setup(4,RPi.GPIO.OUT)
      
        RPi.GPIO.output(4,True)
        #RPi.GPIO.output(4,False)  
        #RPi.GPIO.cleanup()
        
        return "Led is on"

@app.route("/close")
def ledoff():
    
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setup(18,RPi.GPIO.OUT)
        RPi.GPIO.setup(4,RPi.GPIO.OUT)
    
    
        RPi.GPIO.output(4,False)         
        RPi.GPIO.cleanup()

        return "Closed"





if __name__ == "__main__":
    app.run(host="0.0.0.0",port=1111)
