#!/usr/bin/env python
#-*- coding: utf-8 -*-


''' This Project created by Houssem Trabelsi
    email : trabelsi.houssem93@gmail.com
    under MIT license 
'''
import time
import web
import RPi.GPIO as GPIO



Motor1A = 20
Motor1B = 21
Motor2A = 26
Motor2B = 19



pir=17






#definit GPIO en sortie
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False) 


GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)

 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)

GPIO.setup(pir,GPIO.IN)





def forward ():
     print("avancer")
     GPIO.output(Motor2A,GPIO.HIGH)
     GPIO.output(Motor2B,GPIO.LOW)
     GPIO.output(Motor1A,GPIO.LOW)
     GPIO.output(Motor1B,GPIO.HIGH)
     
    


def backward():
     print("backward")
     
     GPIO.output(Motor2A,GPIO.LOW)
     GPIO.output(Motor2B,GPIO.HIGH)
     GPIO.output(Motor1A,GPIO.HIGH)
     GPIO.output(Motor1B,GPIO.LOW)
     
def left():
    print("to the left ")
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    
     
    
def right():
    print("to the right")
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    
    
    
  
def stop():
    print("stop")
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)

def pirSensor():
     
     while True:
         if GPIO.input(pir)==0 :
             print "no intruders"
             return 0
             time.sleep(2)
                             
         else:
             print "intruder detected"
             return 1
             time.sleep(2)
                       



     
            

urls = ('/','myrobot',
        '/be','pirsensor',
        ) 
app = web.application(urls, globals())

class myrobot:

    def POST(self):
        userdata = web.input()                
        if hasattr(userdata,'direction'):
            if userdata.direction == 'forward':
                forward()
            elif userdata.direction == 'left':
                left()         
            elif userdata.direction == 'right':
                right()      
            elif userdata.direction == 'backward':
                backward()
            elif userdata.direction == 'stop':
                stop()
             


class pirsensor:
     def GET(self):
          web.header('Access-Control-Allow-Origin', '*') 
          return pirSensor()

# programme 
if __name__ == '__main__':
    app.run()    

                  
