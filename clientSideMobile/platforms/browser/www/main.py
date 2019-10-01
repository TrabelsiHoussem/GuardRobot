#!/usr/bin/env python
 #-*- coding: utf-8 -*-
import time
import web
import mysql.connector
import datetime
import os
import json
import collections
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 23
Motor2B = 21
Motor2E = 19


pir=7

TRIG = 13
ECHO = 6








mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="robot"
)



#definit GPIO en sortie
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setwarnings(False)
pwm=GPIO.PWM(8,100)
pwm.start(8)




GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
GPIO.setup(pir,GPIO.IN)

GPIO.setup(TRIG,GPIO.OUT)                
GPIO.setup(ECHO,GPIO.IN)  



'''
def servo_camera (angle):
     angle =float(angle)*1.8
     duty=float(angle)/10.0+2.5
     pwm.ChangeDutyCycle(duty)
     print(angle)'''
def avancer ():
     print("avancer")
     '''GPIO.output(Motor1A,GPIO.HIGH)
     GPIO.output(Motor1B,GPIO.LOW)
     GPIO.output(Motor1E,GPIO.HIGH)
    '''


def arriere():
     print("arriere")
     '''
     GPIO.output(Motor1A,GPIO.LOW)
     GPIO.output(Motor1B,GPIO.HIGH)
     GPIO.output(Motor1E,GPIO.HIGH)
     '''
def agauche():
    print("agauche")
    '''
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
     '''
    
def adroite():
    print("adroite")
    '''
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    '''
  
def stop():
    print("stop")

  
'''def capteurGaz():
     while True:
        if GPIO.input(gaz)==0 :
            print "probleme gaz"
            return 1
            #GPIO.input(gaz)=0
            time.sleep(5)
        else:
            print "pas de prob"
            return 0
            time.sleep(5)
'''
def pirSensor():
     while True:
         if GPIO.input(pir)==0 :
             print "no intruders"
             return 0
             time.sleep(2)
                             
         else:
             print "intruder detected"
             return 1
             mycursor = mydb.cursor()
             sql = "INSERT INTO pirevents (date,time) VALUES (%s,%s)"
             
             val = (now.strftime("%Y-%m-%d"),now.strftime("%H:%M"))
             mycursor.execute(sql, val)
             mydb.commit()
             time.sleep(2)
                         

def robotAuto(varbool):
     stop()
     count=0
     while varbool==True:
      i=0
      avgDistance=0
      for i in range(5):
       GPIO.output(TRIG, False)                 #Set TRIG as LOW
       time.sleep(0.1)                                   #Delay

       GPIO.output(TRIG, True)                  #Set TRIG as HIGH
       time.sleep(0.00001)                           #Delay of 0.00001 seconds
       GPIO.output(TRIG, False)                 #Set TRIG as LOW

       while GPIO.input(ECHO)==0:              #Check whether the ECHO is LOW
                
           pulse_start = time.time()
       while GPIO.input(ECHO)==1:              #Check whether the ECHO is HIGH
           pulse_end = time.time()
       pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor

       distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
       distance = round(distance,2)                 #Round to two decimal points
       avgDistance=avgDistance+distance
      avgDistance=avgDistance/5
      print avgDistance
      flag=0
      if avgDistance < 15:      #Check whether the distance is within 15 cm range
         count=count+1
         stop()
         time.sleep(1)
         arriere()
         time.sleep(1.5)
         if (count%3 ==1) & (flag==0):
          adroite()
          flag=1
         else:
          agauche()
          flag=0
         time.sleep(1.5)
         stop()
         time.sleep(1)
      else:
         avancer()
         flag=0


def listalert():
     mycursor = mydb.cursor()
     mycursor.execute("SELECT * FROM pirevents")
     myresult = mycursor.fetchall()
     lis=[]
     for row in myresult:
         d = collections.OrderedDict()
         d['datetime']  = row[0]+" "+row[1]
         #d['time']   = row[1]
         lis.append(d)
     print json.dumps(lis)
     mydb.commit()

     
            
# definit la page de nom index pour le site web 

render = web.template.render('templates/')
urls = ('/','myrobot',
        '/se','return_num',
        '/login','login',
        '/.*','pirsensor',
        '/(.*)','listvideo',
        '/alert','alert',
        '/.*','listalert',
        
        ) 
app = web.application(urls, globals())
# definit l action a effectuer quand la page index est appele 
class myrobot:
    # utilise quand la page est demande 
    '''def GET(self):  
        return render.login() '''
    
    # traite une requete ajax 
    def POST(self):
        userdata = web.input()                
        if hasattr(userdata,'direction'):
            if userdata.direction == 'avant':
                avancer()
            elif userdata.direction == 'gauche':
                agauche()         
            elif userdata.direction == 'droite':
                adroite()      
            elif userdata.direction == 'arriere':
                arriere()
            elif userdata.direction == 'stop':
                stop()
        if hasattr(userdata,'mode'):
              if userdata.mode == 'auto':
                   #robotAuto(True)
                   print "auto"
              elif userdata.mode == 'manuelle':
                   print "manuelle"
                   #robotAuto(False)
                   
              
                   
                  
                   
        #hasattr(userdata,'vol')
        #print userdata.vol
        #elif hasattr(userdata,'vol'):
            #servo_camera(userdata.vol)  
'''class return_num:
    def GET(self):
        return capteurGaz()
'''
'''
class login: 
    def GET(self): 
         return render.login()
    def POST(self):
        name, passwd = web.input().user, web.input().passwd
        print name
        print passwd
        if (name=='admin' and passwd=='admin'):
            return render.myrobot()
        else:
             return render.login()
'''
class pirsensor:
     def GET(self):
          web.header('Access-Control-Allow-Origin', '*') 
          return pirSensor()
     

class listalert:
     def GET(self):
          web.header('Access-Control-Allow-Origin', '*') 
          return listalert()
          

'''
class alert:
     def GET(self):  
     return render.alert()
     
'''

'''          
class listvideo:
    def GET(self, path):
        if path =='':
            path = 'Python/' + path
        else:
            path=''+path
        #if not os.path.normpath(path).startswith('Python/'):
         #   return 'Error'
        
        #path = '/Python/'+path
        if os.path.isdir(path):
            lista = '<html> <body><ul>'
            caminhos = [os.path.join(path, nome) for nome in os.listdir(path)]
            diretorios = [dire for dire in caminhos if os.path.isdir(dire)]
            for dire in diretorios:
    #            lista = lista+dire+'<br>'
                lista = lista+'<a href='+dire+'>'+dire+'</a><br>'
                print "********je suis un repertoir*****"+dire
            arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
            for arq in arquivos:  
                if ".mp4" in arq:
                #lista = lista+'<a href='+arq+' target="_blank">'+arq+'</a><br>'
                    lista = lista+'<li><video src=http://192.168.1.15:8089/'+arq+' controls ></li><br>'
                    print "*************je suis une ficher ***********"+arq
    #            lista = lista+arq+'<br>'
            lista = lista+'</ul><br><br><a href="javascript:window.history.go(-1)">Voltar</a></body> </html>'
            return lista
        else :
            return open(path,'r').read()
'''
class listvideo:
    def GET(self, path):
        #self.send_header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Origin', '*') 
        if path =='':
            path = 'Python/'+ path
        else:
            path=''+path
        #if not os.path.normpath(path).startswith('Python/'):
         #   return 'Error'
        
        #path = '/Python/'+path
        if os.path.isdir(path):
           
            caminhos = [os.path.join(path, nome) for nome in os.listdir(path)]
            diretorios = [dire for dire in caminhos if os.path.isdir(dire)]
            
            arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
            lis=[]
            for arq in arquivos:  
                if ".mp4" in arq:
                     print "mp4"
                     print arq
                     d = collections.OrderedDict()
                     d['video']=arq       
                     lis.append(d)
                else:
                     
                    print "autre"
            print json.dumps(lis)
            return json.dumps(lis)
        else :
            return open(path,'r').read()
     
# programme 
if __name__ == '__main__':
    app.run()    

                  
