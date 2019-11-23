import pandas as pd
import matplotlib.pyplot as plt


class DA:
    def __init__(self, start, end):
        sy, sm, sd = start.split('-')
        ey, em, ed = end.split('-')
        sy, sm, sd = int(sy), int(sm), int(sd)
        ey, em, ed = int(ey), int(em), int(ed)
        self.start = start
        self.end = end
        self.s = sy * 10000 + sm * 100 + sd
        self.e = ey * 10000 + em * 100 + ed

    def api_1(self):
        dataset = pd.read_csv('model/origin_data.csv')
        number = {}
        name = []
        for data in dataset.values:
            date = data[2]
            dy, dm, dd = date.split('-')
            dy, dm, dd = int(dy), int(dm), int(dd)
            d = dy * 10000 + dm * 100 + dd
            if self.s <= d <= self.e:
                if data[4] not in number:
                    name.append(data[4])
                    number[data[4]] = 1
                if data[4] in number:
                    number[data[4]] = number[data[4]] + 1
        name.sort()
        count = []
        for n in name:
            count.append(number[n])
        df = pd.DataFrame()
        df['cause_name'] = name
        df['counts'] = count
        df.plot.bar(x='cause_name', y='counts')
        # plt.show()
        img = plt.savefig('api_1.png')
        # return img

    def api_2(self):
        dataset = pd.read_csv('model/origin_data.csv')
        classes = {}
        name = []
        for data in dataset.values:
            date = data[2]
            dy, dm, dd = date.split('-')
            dy, dm, dd = int(dy), int(dm), int(dd)
            d = dy * 10000 + dm * 100 + dd
            if self.s <= d <= self.e:
                if data[6] not in classes:
                    name.append(data[6])
                    classes[data[6]] = 1
                if data[6] in classes:
                    classes[data[6]] = classes[data[6]] + 1
        name.sort()
        count = []
        for n in name:
            count.append(classes[n])
        df = pd.DataFrame()
        df['fire_class'] = name
        df['counts'] = count
        df.plot.bar(x='fire_class', y='counts')
        # plt.show()
        img = plt.savefig('api_2.png')
        # return img

    def api_3(self):
        dataset = pd.read_csv('model/origin_data.csv')
        human_factors = ['Campfire', 'Arson', 'Smoking', 'Equipment Use', 'Children', 'Fireworks', 'Railroad',
                         'Powerline', 'Structure']
        classes = {}
        human = {}
        name = []
        for data in dataset.values:
            date = data[2]
            dy, dm, dd = date.split('-')
            dy, dm, dd = int(dy), int(dm), int(dd)
            d = dy * 10000 + dm * 100 + dd
            if self.s <= d <= self.e:
                if data[6] not in classes:
                    name.append(data[6])
                    classes[data[6]] = 1
                    human[data[6]] = 1
                if data[6] in classes:
                    classes[data[6]] = classes[data[6]] + 1
                    if data[4] in human_factors:
                        human[data[6]] = human[data[6]] + 1
        name.sort()
        count_human = []
        count_not_human = []
        for n in name:
            count_human.append(human[n] / classes[n])
            count_not_human.append((classes[n] - human[n]) / classes[n])
        df = pd.DataFrame()
        df['class_name'] = name
        df['human_factors'] = count_human
        df['not_human_factors'] = count_not_human
        df.plot.barh(x='class_name')
        # plt.show()
        img = plt.savefig('api_3.png')
        # return img

    def api_4(self, city_name):
        humidity = pd.read_csv('model/humidity.csv', index_col='datetime')
        humidity = humidity[city_name]

        pressure = pd.read_csv('model/pressure.csv', index_col='datetime')
        pressure = pressure[city_name]

        temperature = pd.read_csv('model/temperature.csv', index_col='datetime')
        temperature = temperature[city_name]

        wind_direction = pd.read_csv('model/wind_direction.csv', index_col='datetime')
        wind_direction = wind_direction[city_name]

        wind_speed = pd.read_csv('model/wind_speed.csv', index_col='datetime')
        wind_speed = wind_speed[city_name]

        result_h = [humidity.loc[self.start]]
        result_p = [pressure.loc[self.start]]
        result_t = [temperature.loc[self.start]]
        result_wd = [wind_direction.loc[self.start]]
        result_ws = [wind_speed.loc[self.start]]

        position = list(humidity.index.values).index(self.start)
        for i in range(1, min(8, len(humidity.values) - 1 - position)):
            result_h.append(humidity.values[position + i])
            result_p.append(pressure.values[position + i])
            result_t.append(temperature.values[position + i])
            result_wd.append(wind_direction.values[position + i])
            result_ws.append(wind_speed.values[position + i])
        df = pd.DataFrame()
        df['day'] = range(len(result_h))
        df['humidity'] = result_h
        df['pressure'] = result_p
        df['temperature'] = result_t
        df['wind_direction'] = result_wd
        df['wind_speed'] = result_ws
        df.plot(x='day')
        # plt.show()
        img = plt.savefig('api_4.png')
        # return img

# 
# da1 = DA('2012-1-1', '2013-12-31')
# da1.print_it()
# da1.api_1()
# da1.api_2()
# da1.api_3()
# 
# da2 = DA('2013-8-31', '2013-8-31')
# da2.api_4('San Diego')
