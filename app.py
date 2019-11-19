#!dev/bin/python

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


def send_request(cityName: str="New York"):
    # Weather API
    # GET https://api.openweathermap.org/data/2.5/forecast

    try:
        response = requests.get(
            url="https://api.openweathermap.org/data/2.5/forecast",
            params={
                "q": cityName,
                "mode": "json",
                "APPID": "5276bdc5394d77211678f28c6ff82721",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        return response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/weather', methods=['GET'])
def get_weather():
    city = request.args.get('cityName', default = 'New York', type = str)
    dataset = send_request(city)
    final = []
    round_temp = 0.0
    for index, item in enumerate(dataset['list']):
        if (index + 1) % 8 == 0:
            final.append(str(round(round_temp / 8 - 273.15, 2)))
            round_temp = 0.0
        round_temp += item['main']['temp']

    return jsonify(final)

if __name__ == '__main__':
    app.run()
