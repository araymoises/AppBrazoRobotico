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

class Mover(Resource):
    def get(self, x, y):
	#z = 0
	#global x_brazo
        #x_brazo = x_brazo + int(x)
	#z = z + int(x)
	#GPIO.cleanup()
	#for j in range(0, 500):
	while True:
		for i in range(0,4):
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
	return x_brazo

class Tracks(Resource):
    def get(self):
        #conn = db_connect.connect()
        #query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        #result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        #return jsonify(result)
	return true

class Employees_Name(Resource):
    def get(self, employee_id):
        #conn = db_connect.connect()
        #query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        #result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        #return jsonify(employee_id)
	return employee_id

api.add_resource(Mover, '/move/<x>/<y>') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')
