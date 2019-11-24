from flask import Flask
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask import request
from LeoAPI import DB

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
        da = DB(dates['start'], dates['end'])
        img = da.api_1()
        return {'api_1': img}, 200


if __name__ == '__main__':
    app.run()
