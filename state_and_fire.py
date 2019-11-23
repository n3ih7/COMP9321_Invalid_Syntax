import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from flask import Flask
from flask import request
'''

df1 = df1['STATE'].value_counts()
df1.plot.bar(subplots=True)
plt.xlabel('state')
plt.ylabel("fire number")
img = plt.savefig('df1.png')

plt.show()
#print(df1.head(5))
'''
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

    def print_it(self):
        print('start:{0}'.format(self.s))
        print('end:{0}'.format(self.e))

    def api_1(self):
        dataset = pd.read_csv('origin_data.csv')
        number = {}
        name = []
        for data in dataset.values:
            date = data[2]
            dy, dm, dd = date.split('-')
            dy, dm, dd = int(dy), int(dm), int(dd)
            d = dy * 10000 + dm * 100 + dd
            if self.s <= d <= self.e:
                if data[0] not in number:
                    name.append(data[0])
                    number[data[0]] = 1
                if data[0] in number:
                    number[data[0]] = number[data[0]] + 1
        name.sort()
        count = []
        for n in name:
            count.append(number[n])
        df = pd.DataFrame()
        df['state_name'] = name
        df['counts'] = count
        df.plot.bar(x='state_name', y='counts')
        #plt.show()
        img = plt.savefig('api_1.png')
        return img

da1 = DA('2014-1-1', '2014-12-30')
da1.api_1()