from flask import Flask
from flask import request
from flask_restplus import Resource, Api
from flask_restplus import fields
from model import *

app = Flask(__name__)
api = Api(app)

fire_model = api.model('fire', {
    'humidity': fields.Integer,
    'pressure': fields.Integer,
    'temprature': fields.Integer,
    'wind_direction': fields.Integer,
    'wind_speed': fields.Integer,
})


@api.route('/prediction')
class Prediction(Resource):
    @api.expect(fire_model)
    def post(self):
        fire = request.json
        hum = fire['humidity']
        result = mechanical(hum)
        return {"prediction": result}, 200


if __name__ == '__main__':
    app.run()