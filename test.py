#!dev/bin/python
import base64
import json
import requests
import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from model.Modeling import Model
from API_Additions import DA

app = Flask(__name__)
cors = CORS(app)


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


@app.route('/api/weather', methods=['GET'])
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

    current.pop('gust', None)
    today = datetime.date.today()
    a = {'cityName': weather_current_dict['name'], 'Country': weather_current_dict['sys']['country'],
         str(today): current}
    a.update(weather_current_dict['coord'])

    forecast = send_request_weather_forecast(city)
    n = 1
    final = {}
    for item in enumerate(forecast['list']):
        if item[1]['dt_txt'].split(' ')[1].split(':')[0] == '09' and item[1]['dt_txt'].split(' ')[0] != str(
                today) and n < 5:
            j = item[1]['main']
            k = item[1]['wind']
            j.update(k)
            j.pop('temp_max', None)
            j.pop('temp_min', None)
            j.pop('temp_kf', None)
            j.pop('sea_level', None)
            j.pop('grnd_level', None)
            m = {str(today + datetime.timedelta(days=n)): j}
            final.update(m)
            n += 1

    for key in final.keys():
        data_humidity_1 = float(final[key]['humidity'])
        data_pressure_1 = float(final[key]['pressure'])
        data_temp_1 = float(final[key]['temp'])
        data_wind_deg_1 = float(final[key]['deg'])
        data_wind_speed_1 = float(final[key]['speed'])
        data_1 = Model(data_humidity_1, data_pressure_1, data_temp_1, data_wind_deg_1, data_wind_speed_1)
        fire_probability_1 = round(data_1.svm_predict()[0][0] * 0.68 * 100, 2)
        final[key].update({'fire_probability': fire_probability_1})
        final[key]['temp'] = round(final[key]['temp'] - 273.15, 2)
        if final[key]['deg']:
            if 348.75 < final[key]['deg'] <= 360 or 0 <= final[key]['deg'] <= 11.25:
                final[key]['deg'] = 'north'
            elif 11.25 < final[key]['deg'] <= 33.75:
                final[key]['deg'] = 'north-northeast'
            elif 33.75 < final[key]['deg'] <= 56.25:
                final[key]['deg'] = 'northeast'
            elif 56.25 < final[key]['deg'] <= 78.75:
                final[key]['deg'] = 'east-northeast'
            elif 78.75 < final[key]['deg'] <= 101.25:
                final[key]['deg'] = 'east'
            elif 101.25 < final[key]['deg'] <= 123.75:
                final[key]['deg'] = 'east-southeast'
            elif 123.75 < final[key]['deg'] <= 146.25:
                final[key]['deg'] = 'southeast'
            elif 146.25 < final[key]['deg'] <= 168.75:
                final[key]['deg'] = 'south-southeast'
            elif 168.75 < final[key]['deg'] <= 191.25:
                final[key]['deg'] = 'south'
            elif 191.25 < final[key]['deg'] <= 213.75:
                final[key]['deg'] = 'south-southwest'
            elif 213.75 < final[key]['deg'] <= 236.25:
                final[key]['deg'] = 'southwest'
            elif 236.25 < final[key]['deg'] <= 258.75:
                final[key]['deg'] = 'west-southwest'
            elif 258.75 < final[key]['deg'] <= 281.25:
                final[key]['deg'] = 'west'
            elif 281.25 < final[key]['deg'] <= 303.75:
                final[key]['deg'] = 'west-northwest'
            elif 303.75 < final[key]['deg'] <= 326.25:
                final[key]['deg'] = 'northwest'
            elif 326.25 < final[key]['deg'] <= 348.75:
                final[key]['deg'] = 'north-northwest'

    a.update(final)
    return jsonify(a)


@app.route('/api/jay', methods=['GET'])
def get_image_jay():
    start_date = request.args.get('start_date', type=str)
    end_date = request.args.get('end_date', default='2013-12-31', type=str)
    api_type = request.args.get('api_type', default='1', type=str)
    da1 = DA(start_date, end_date)
    if api_type == '1':
        da1.api_1()
        with open("api_1.png", "rb") as f:
            data = f.read()
            img_stream = base64.b64encode(data)
    return img_stream


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8090)
