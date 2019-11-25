from flask import Flask
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask import request
from API_Additions import DA

app = Flask(__name__)
api = Api(app)

data_model = api.model('data', {
    'start': fields.String,
    'end': fields.String,
    'city_name': fields.String,
})


@api.route('/api_1')
class DataAnalysis(Resource):
    @api.expect(data_model)
    def post(self):
        dates = request.json
        da = DA(dates['start'], dates['end'])
        img = da.api_1()
        return {'api_1': 'api_1.png'}, 200


@api.route('/api_2')
class DataAnalysis(Resource):
    @api.expect(data_model)
    def post(self):
        dates = request.json
        da = DA(dates['start'], dates['end'])
        img = da.api_2()
        return {'api_2': 'api_2.png'}, 200


@api.route('/api_3')
class DataAnalysis(Resource):
    @api.expect(data_model)
    def post(self):
        dates = request.json
        da = DA(dates['start'], dates['end'])
        img = da.api_3()
        return {'api_3': 'api_3.png'}, 200


@api.route('/api_4')
class DataAnalysis(Resource):
    @api.expect(data_model)
    def post(self):
        dates = request.json
        da = DA(dates['start'], dates['end'])
        try:
            img = da.api_4(dates['city_name'])
        except:
            return {'api_4': 'No fire'}, 200
        return {'api_4': 'api_4.png'}, 200


if __name__ == '__main__':
    app.run()
