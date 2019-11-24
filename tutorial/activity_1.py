import json
import math

import pandas as pd
from flask import Flask
from flask import request, jsonify
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_restplus import inputs
from flask_restplus import reqparse

app = Flask(__name__)
api = Api(app, title='My Book API', description='Few methods', version='0.0.5')

# The following is the schema of Book
book_model = api.model('Book', {
    'Flickr_URL': fields.String,
    'Publisher': fields.String,
    'Author': fields.String,
    'Title': fields.String,
    'Date_of_Publication': fields.Integer,
    'Identifier': fields.Integer,
    'Place_of_Publication': fields.String
})

parser = reqparse.RequestParser()
parser.add_argument('order_by', choices=[c for c in book_model.keys()], required=True)
parser.add_argument('ascending', type=inputs.boolean, default=True)


@api.route("/books")
class Books(Resource):
    @api.expect(parser)
    @api.doc(description='This method returns a list of books')
    def get(self):
        """
        Get the lists of books
        """
        ret = []

        args = parser.parse_args()
        order_by = args['order_by']
        ascending = args['ascending']

        df.sort_values(by=order_by, ascending=ascending, inplace=True)

        for key, row in df.iterrows():
            d = dict(row)

            to_remove = []
            for k in d:
                if not isinstance(d[k], str) and math.isnan(d[k]):
                    to_remove.append(k)

            for k in to_remove:
                d.pop(k)

            ret.append(d)

        return jsonify(ret)

    @api.expect(book_model)
    def post(self):
        book = request.json
        id = max(df.index) + 1

        for key in book:
            df.loc[id, key] = book[key]

        return jsonify(message="The books has been created", book_id=id)


@api.route('/books/<int:id>')
@api.param(name='id', description='a unique identifier')
class Books(Resource):
    @api.response(404, 'Not Found')
    @api.response(200, 'Successful')
    def get(self, id):
        if id not in df.index:
            api.abort(404, "Book {} doesn't exist".format(id))

        book = dict(df.loc[id])
        return book

    def delete(self, id):
        if id not in df.index:
            api.abort(404, "Book {} doesn't exist".format(id))

        df.drop(id, inplace=True)
        return {"message": "Book {} is removed.".format(id)}, 200

    @api.expect(book_model)
    def put(self, id):

        if id not in df.index:
            api.abort(404, "Book {} doesn't exist".format(id))

        # get the payload and convert it to a JSON
        book = request.json

        # Book ID cannot be changed
        if 'Identifier' in book and id != book['Identifier']:
            return {"message": "Identifier cannot be changed".format(id)}, 400

        # Update the values
        for key in book:
            if key not in book_model.keys():
                # unexpected column
                return {"message": "Property {} is invalid".format(key)}, 400
            df.loc[id, key] = book[key]

        df.append(book, ignore_index=True)
        return {"message": "Book {} has been successfully updated".format(id)}, 200


if __name__ == '__main__':
    columns_to_drop = ['Edition Statement',
                       'Corporate Author',
                       'Corporate Contributors',
                       'Former owner',
                       'Engraver',
                       'Contributors',
                       'Issuance type',
                       'Shelfmarks'
                       ]
    csv_file = "Books.csv"
    df = pd.read_csv(csv_file)

    # drop unnecessary columns
    df.drop(columns_to_drop, inplace=True, axis=1)

    # clean the date of publication & convert it to numeric data
    new_date = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
    new_date = pd.to_numeric(new_date)
    new_date = new_date.fillna(0)
    df['Date of Publication'] = new_date

    # replace spaces in the name of columns
    df.columns = [c.replace(' ', '_') for c in df.columns]

    # set the index column; this will help us to find books with their ids
    df.set_index('Identifier', inplace=True)

    # run the application
    app.run(debug=True, host='0.0.0.0', port=8090)
