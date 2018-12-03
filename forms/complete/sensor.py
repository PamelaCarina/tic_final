from datetime import datetime
from app import db, ma

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float())
    humedad = db.Column(db.Float())
    pH = db.Column(db.Float())
    luminosidad = db.Column(db.Float())
    date = db.Column(db.DateTime)

    def __init__(self, temperature, humedad, pH, luminocidad, date=None):
        self.temperature = temperature
        self.humedad = humedad
        self.pH = pH
        self.luminosidad = luminosidad
        if date is None:
            date = datetime.utcnow()
        self.date = date


class SensorSchema(ma.ModelSchema):
    class Meta:
        model = Sensor
