#!dev/bin/python
import json
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)


def send_request_weather_forecast(cityName: str = "New York"):
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


def send_request_weather_current(cityName: str = "New York"):
    # Weather API
    # GET https://api.openweathermap.org/data/2.5/forecast

    try:
        response = requests.get(
            url="https://api.openweathermap.org/data/2.5/weather",
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


@app.route('/todo/api/v1.0/weather_forecast', methods=['GET'])
def get_weather_forecast():
    city = request.args.get('cityName', default='New York', type=str)
    dataset = send_request_weather_forecast(city)
    forecast = []
    round_temp = 0.0
    for index, item in enumerate(dataset['list']):
        if (index + 1) % 8 == 0:
            forecast.append(str(round(round_temp / 8 - 273.15, 2)))
            round_temp = 0.0
        round_temp += item['main']['temp']

    return jsonify(forecast)


@app.route('/todo/api/v1.0/weather_current', methods=['GET'])
def get_weather_current():
    city = request.args.get('cityName', default='New York', type=str)
    weather_current_dict = send_request_weather_current(city)
    current = weather_current_dict['coord']
    current.update(weather_current_dict['main'])
    current.pop('temp_min', None)
    current.pop('temp_max', None)
    current.update(weather_current_dict['wind'])

    return jsonify(current)


if __name__ == '__main__':
    app.run()
