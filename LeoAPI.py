import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import time


class DB:
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
        df = pd.read_csv("model/origin_data.csv")
        df = df.drop(df.columns[3:], axis=1)
        df = df.drop(df.columns[0], axis=1)
        df['date'] = df['datetime'].str.split('-')
        df['month'] = df['date'].str[1]
        final_df = df.drop(df.columns[1:3], axis=1)
        final_df.columns = ['city', 'month']
        month = {}
        for data in df.values:
            date_time = data[1]
            dty, dtm, dtd = date_time.split('-')
            dty, dtm, dtd = int(dty), int(dtm), int(dtd)
            d = dty * 10000 + dtm * 100 + dtd
            if self.s <= d <= self.e:
                if dtm not in month:
                    month[dtm] = 1
                if dtm in month:
                    month[dtm] = month[dtm] + 1
        df2 = pd.DataFrame()
        a = []
        b = []
        for n in range(0, len(month)):
            a.append(n + 1)
            b.append(month[n + 1])
        df2['month'] = a
        df2['count'] = b
        df2.plot.bar(x='month', y='count')
        plt.xticks(rotation=360)
        # plt.show()
        plt.savefig('api_5.png')
        # return img


# da1 = DA('2012-1-1', '2013-12-31')
# da1.print_it()
# da1.api_1()

# if __name__ == "__main__":
#     process()
