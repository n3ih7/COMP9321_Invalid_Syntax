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
    current['temp'] = round(current['temp'] - 273.15, 2)

    if current['deg']:
        current['deg'] = float(current['deg'])
        if 348.75 < current['deg'] <= 360 & 0 <= current['deg'] <= 11.25:
            current['deg'] = 'North'
        elif 11.25 < current['deg'] <= 33.75:
            current['deg'] = 'NNE'
        elif 33.75 < current['deg'] <= 56.25:
            current['deg'] = 'NE'
        elif 56.25 < current['deg'] <= 78.75:
            current['deg'] = 'ENE'
        elif 78.75 < current['deg'] <= 101.25:
            current['deg'] = 'East'
        elif 101.25 < current['deg'] <= 123.75:
            current['deg'] = 'ESE'
        elif 123.75 < current['deg'] <= 146.25:
            current['deg'] = 'SE'
        elif 146.25 < current['deg'] <= 168.75:
            current['deg'] = 'SSE'
        elif 168.75 < current['deg'] <= 191.25:
            current['deg'] = 'South'
        elif 191.25 < current['deg'] <= 213.75:
            current['deg'] = 'SSW'
        elif 213.75 < current['deg'] <= 236.25:
            current['deg'] = 'SW'
        elif 236.25 < current['deg'] <= 258.75:
            current['deg'] = 'WSW'
        elif 258.75 < current['deg'] <= 281.25:
            current['deg'] = 'West'
        elif 281.25 < current['deg'] <= 303.75:
            current['deg'] = 'WNW'
        elif 303.75 < current['deg'] <= 326.25:
            current['deg'] = 'NW'
        elif 326.25 < current['deg'] <= 348.75:
            current['deg'] = 'NNW'

    return jsonify(current)


if __name__ == '__main__':
    app.run(debug=True, port=8090)
