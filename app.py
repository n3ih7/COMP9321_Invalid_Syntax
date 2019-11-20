#!dev/bin/python
import json
import requests
import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from model.Modeling import Model

app = Flask(__name__)
CORS(app)


def send_request_weather_forecast(cityName: str = "Sydney"):
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


def send_request_weather_current(cityName: str = "Sydney"):
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


@app.route('/todo/api/v1.0/weather_current', methods=['GET'])
def get_weather_current():
    city = request.args.get('cityName', default='Sydney', type=str)
    weather_current_dict = send_request_weather_current(city)
    current = weather_current_dict['main']
    current.pop('temp_min', None)
    current.pop('temp_max', None)
    current.update(weather_current_dict['wind'])
    data_humidity = float(current['humidity'])
    data_pressure = float(current['pressure'])
    data_temp = float(current['temp'])
    data_wind_deg = float(current['deg'])
    data_wind_speed = float(current['speed'])
    data = Model(data_humidity, data_pressure, data_temp, data_wind_deg, data_wind_speed)
    fire_probability = round(data.svm_predict()[0][0] * 0.68 * 100, 2)
    current.update({'fire_probability': fire_probability})
    current['temp'] = round(current['temp'] - 273.15, 2)

    if current['deg']:
        current['deg'] = float(current['deg'])
        if 348.75 < current['deg'] <= 360 or 0 <= current['deg'] <= 11.25:
            current['deg'] = 'north'
        elif 11.25 < current['deg'] <= 33.75:
            current['deg'] = 'north-northeast'
        elif 33.75 < current['deg'] <= 56.25:
            current['deg'] = 'northeast'
        elif 56.25 < current['deg'] <= 78.75:
            current['deg'] = 'east-northeast'
        elif 78.75 < current['deg'] <= 101.25:
            current['deg'] = 'east'
        elif 101.25 < current['deg'] <= 123.75:
            current['deg'] = 'east-southeast'
        elif 123.75 < current['deg'] <= 146.25:
            current['deg'] = 'southeast'
        elif 146.25 < current['deg'] <= 168.75:
            current['deg'] = 'south-southeast'
        elif 168.75 < current['deg'] <= 191.25:
            current['deg'] = 'south'
        elif 191.25 < current['deg'] <= 213.75:
            current['deg'] = 'south-southwest'
        elif 213.75 < current['deg'] <= 236.25:
            current['deg'] = 'southwest'
        elif 236.25 < current['deg'] <= 258.75:
            current['deg'] = 'west-southwest'
        elif 258.75 < current['deg'] <= 281.25:
            current['deg'] = 'west'
        elif 281.25 < current['deg'] <= 303.75:
            current['deg'] = 'west-northwest'
        elif 303.75 < current['deg'] <= 326.25:
            current['deg'] = 'northwest'
        elif 326.25 < current['deg'] <= 348.75:
            current['deg'] = 'north-northwest'

    today = str(datetime.date.today())
    a = {'cityName': weather_current_dict['name'], 'Country': weather_current_dict['sys']['country'], today: current}
    a.update(weather_current_dict['coord'])

    forecast = send_request_weather_forecast(city)
    # for index, item in enumerate(forecast['list']):

    return jsonify(a)


if __name__ == '__main__':
    app.run()
