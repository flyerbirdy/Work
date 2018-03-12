from flask import Flask
import sys
import RPi.GPIO   
import time




app = Flask(__name__)

@app.route("/")
def led():
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setup(18,RPi.GPIO.OUT)
        RPi.GPIO.setup(4,RPi.GPIO.OUT)
        for i in range(0,10):
            RPi.GPIO.output(18,True)  
            time.sleep(0.1)  
            RPi.GPIO.output(18,False)   
            time.sleep(0.1) 
            RPi.GPIO.output(4,True)
            time.sleep(0.1)
            RPi.GPIO.output(4,False)
            time.sleep(0.1)

        RPi. GPIO.cleanup()    

        return "Led is flash"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=1111)
