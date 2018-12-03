from flask.ext.restful import Resource
from flask import request, jsonify
from app import app, api, db, auth, users
from sensor import Sensor, SensorSchema

schema = SensorSchema()

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

class Index(Resource): #acepta el log in y devuelve un saludo al usuario que se logueo
    decorators = [auth.login_required]
    def get(self):
        return "Hello, %s!" % auth.username()

class Sensorslist(Resource):
    decorators = [auth.login_required] #recursos que requieren autenticacion
    def get(self):
        allSensors = Sensor.query.all()
        result = schema.dump(allSesnors, many=True).data
        return result
    def post(self):
        args = request.get_json()
        sensor_read = Sensor(args['temperature, humedad, pH, luminosidad'])
        db.session.add(sensor_read)
        return 'Sensors added', 200

class Sensors(Resource): #obtener un valor especifico de base de datos del que conocemos su identificador
    decorators = [auth.login_required]
    def get(self, id):
        temperature = Sensor.query.get(id)
        humedad = Sensor.query.get(id)
        pH = Sensor.query.get(id)
        luminosidad = Sensor.query.get(id)
        result1 = schema.dump(temperature).data
        result2 = schema.dump(humedad).data
        result3 = schema.dump(pH).data
        result4 = schema.dump(luminosidad).data
        return result1 and result2 and result3 and result4


api.add_resource(Index, '/api/v1.0', endpoint='index')
api.add_resource(Sensorslist, '/api/v1.0/sensores', endpoint='sensores')
api.add_resource(Sensors, '/api/v1.0/sensores/<string:id>', endpoint='sensores1')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
