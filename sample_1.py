import pandas as pd
import numpy as np


#csvout = pd.read_csv("188outchart.csv", thousands = ',',error_bad_lines=False,lineterminator="\n")
#csvout = pd.read_csv("188outchart.csv",thousands = ',')





#humidity = humidity.set_index(['datetime'])
# for item in humidity['datetime']:
#    item = item.split(" ")[0]
#humidity = humidity.groupby('datetime').mean()
pressure = pd.read_csv("pressure.csv", thousands=',')
pressure = pressure.set_index(['datetime'])
pressure = pressure.groupby('datetime').mean()
temperature = pd.read_csv("temperature.csv", thousands=',')
temperature = temperature.set_index(['datetime'])
temperature = temperature.groupby('datetime').mean()
# weather_description=pd.read_csv("weather_description.csv",thousands = ',')
# weather_description=weather_description.set_index(['datetime'])
# weather_description = weather_description.groupby('datetime').mean()

wind_direction = pd.read_csv("wind_direction.csv",thousands = ',')
wind_direction = wind_direction.set_index(['datetime'])
wind_direction = wind_direction.groupby('datetime').mean()

wind_speed = pd.read_csv("wind_speed.csv",thousands = ',')
wind_speed = wind_speed.set_index(['datetime'])
wind_speed = wind_speed.groupby('datetime').mean()

pressure=pressure.to_csv('pressure1.csv')
temperature = temperature.to_csv('temperature1.csv')
wind_direction = wind_direction.to_csv('wind_direction1.csv')
wind_speed = wind_speed.to_csv('wind_speed1.csv')
