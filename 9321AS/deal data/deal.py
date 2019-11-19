import pandas as pd
data_1 = pd.read_csv("188outchart(2)(1).csv")
data_2 = pd.read_csv("humidity1(2)(1).csv")

L = len(data_1)
k = len(data_2)
list = []
data_1 = data_1.drop(["humidity"],axis = 'columns')
for x in range(0,L):
    con = 0
    time = data_1['datetime'][x]
    name = data_1['COUNTY_NAME'][x]
    for i in range(0,k):
        if data_2['datetime'][i] == time:
            con = 1
            list.append(data_2[name][i])
            break
    if con == 0:
        list.append('')
data_1["humidity"] = list
data_1.to_csv('data.csv')