#sudo webiopi -d -c /etc/webiopi/config
#User: webiopi; Pass: raspberry
#source venv/bin/activate
import RPi.GPIO as GPIO
import time

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

#GPIO.output(17, GPIO.HIGH)

app = Flask(__name__)
api = Api(app)
x_brazo = 0
y_brazo = 0
z_brazo = 0

agarrar = 0

class Mover(Resource):
    def get(self, x, y):
        if int(x)>=0 and int(y)>=0:
            	global x_brazo
            	global y_brazo
                #x_brazo = x_brazo + int(x)
            	#GPIO.cleanup()
                if int(x)>x_brazo:
                    x_orientacion=1
                    x_rango_1 = 0
                    x_rango_2 = 4
                else:
                    x_orientacion=-1
                    x_rango_1 = 4
                    x_rango_2 = -1

            	while x_brazo != int(x):
            		for i in range(x_rango_1, x_rango_2, x_orientacion):
            			time.sleep(0.01)
            			if i==0:
            				GPIO.output(17, 1)
            				GPIO.output(18, 1)
            				GPIO.output(27, 0)
            				GPIO.output(22, 0)
            				print "i es 0"
            			if i==1:
            				GPIO.output(17, 0)
            				GPIO.output(18, 1)
            				GPIO.output(27, 1)
            				GPIO.output(22, 0)
            				print "i es 1"
            			if i==2:
            				GPIO.output(17, 0)
            				GPIO.output(18, 0)
            				GPIO.output(27, 1)
            				GPIO.output(22, 1)
            				print "i es 2"
            			if i==3:
            				GPIO.output(17, 1)
            				GPIO.output(18, 0)
            				GPIO.output(27, 0)
            				GPIO.output(22, 1)
            				print "i es 3"
            		x_brazo = x_brazo + x_orientacion
            		print "X: " + str(x_brazo)

                if int(y)>y_brazo:
                    y_orientacion=1
                    y_rango_1 = 0
                    y_rango_2 = 4
                else:
                    y_orientacion=-1
                    y_rango_1 = 4
                    y_rango_2 = -1

            	while y_brazo != int(y):
            		for i in range(y_rango_1, y_rango_2, y_orientacion):
            			time.sleep(0.01)
            			if i==0:
            				GPIO.output(17, 1)
            				GPIO.output(18, 1)
            				GPIO.output(27, 0)
            				GPIO.output(22, 0)
            				print "i es 0"
            			if i==1:
            				GPIO.output(17, 0)
            				GPIO.output(18, 1)
            				GPIO.output(27, 1)
            				GPIO.output(22, 0)
            				print "i es 1"
            			if i==2:
            				GPIO.output(17, 0)
            				GPIO.output(18, 0)
            				GPIO.output(27, 1)
            				GPIO.output(22, 1)
            				print "i es 2"
            			if i==3:
            				GPIO.output(17, 1)
            				GPIO.output(18, 0)
            				GPIO.output(27, 0)
            				GPIO.output(22, 1)
            				print "i es 3"
            		y_brazo = y_brazo + y_orientacion
            		print "Y: " + str(y_brazo)
                response = str(x_brazo) + "," + str(y_brazo)
        else:
                response = "Error: Los datos ingresados son menores que cero, o superaron el limite maximo."
	return response

class Estirar(Resource):
    def get(self, z):
        if int(z)>=0:
                global z_brazo
                #x_brazo = x_brazo + int(x)
            	#GPIO.cleanup()
                if int(z)>z_brazo:
                    z_orientacion=1
                    z_rango_1 = 0
                    z_rango_2 = 4
                else:
                    z_orientacion=-1
                    z_rango_1 = 4
                    z_rango_2 = -1

            	while z_brazo != int(z):
            		for i in range(z_rango_1, z_rango_2, z_orientacion):
            			time.sleep(0.01)
            			if i==0:
            				GPIO.output(17, 1)
            				GPIO.output(18, 1)
            				GPIO.output(27, 0)
            				GPIO.output(22, 0)
            				print "i es 0"
            			if i==1:
            				GPIO.output(17, 0)
            				GPIO.output(18, 1)
            				GPIO.output(27, 1)
            				GPIO.output(22, 0)
            				print "i es 1"
            			if i==2:
            				GPIO.output(17, 0)
            				GPIO.output(18, 0)
            				GPIO.output(27, 1)
            				GPIO.output(22, 1)
            				print "i es 2"
            			if i==3:
            				GPIO.output(17, 1)
            				GPIO.output(18, 0)
            				GPIO.output(27, 0)
            				GPIO.output(22, 1)
            				print "i es 3"
            		z_brazo = z_brazo + z_orientacion
            		print "Z: " + str(z_brazo)
                response = str(z_brazo)
        else:
                response = "Error: Los datos ingresados son menores que cero, o superaron el limite maximo."

	return response

class Agarrar(Resource):
    def get(self):
        global agarrar
        j = 0
        #x_brazo = x_brazo + int(x)
        #GPIO.cleanup()
        if agarrar==0:
            a_orientacion=1
            a_rango_1 = 0
            a_rango_2 = 4
            response  = "La pinza agarró correctamente."
        else:
            a_orientacion=-1
            a_rango_1 = 4
            a_rango_2 = -1
            response  = "La pinza soltó correctamente."

        while j < 50:
            for i in range(a_rango_1, a_rango_2, a_orientacion):
                time.sleep(0.01)
                if i==0:
                    GPIO.output(17, 1)
                    GPIO.output(18, 1)
                    GPIO.output(27, 0)
                    GPIO.output(22, 0)
                    print "i es 0"
                if i==1:
                    GPIO.output(17, 0)
                    GPIO.output(18, 1)
                    GPIO.output(27, 1)
                    GPIO.output(22, 0)
                    print "i es 1"
                if i==2:
                    GPIO.output(17, 0)
                    GPIO.output(18, 0)
                    GPIO.output(27, 1)
                    GPIO.output(22, 1)
                    print "i es 2"
                if i==3:
                    GPIO.output(17, 1)
                    GPIO.output(18, 0)
                    GPIO.output(27, 0)
                    GPIO.output(22, 1)
                    print "i es 3"
                j = j + 1
        agarrar = 1
	return response

api.add_resource(Mover, '/mover/<x>/<y>')
api.add_resource(Estirar, '/estirar/<z>')
api.add_resource(Agarrar, '/agarrar/')


if __name__ == '__main__':
     app.run(port=5002,host='0.0.0.0')
