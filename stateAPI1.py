from flask import Flask
from flask import render_template
from flask import request
from flask_restplus import Resource, Api
from flask_restplus import fields

app = Flask(__name__)
api = Api(app)

data_model = api.model('data', {
    'start': fields.String,
    'end': fields.String,
    'state': fields.String,
})

@api.route('/api_1')
class DataAnalysis(Resource):
    @api.expect(data_model)
    def post(self):
        dates = request.json
        da = DA(dates['start'], dates['end'])
        img = da.api_1()
        return {'api_1': 'api_1.png'}, 200

if __name__ == '__main__':
    app.run()


