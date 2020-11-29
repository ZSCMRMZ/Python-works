import json
from pyecharts import Line
import webbrowser
import os

with open("weather.json","r") as f:
    data = json.load(f)

# print(data)

mean_temp = data["mean_temp"]
high_temp = data["high_temp"]
low_temp = data["low_temp"]
# print(mean_temp)

x_axis = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line = Line("一周温度变化")
line.add("最高气温",x_axis,high_temp)
line.add("最低气温",x_axis,low_temp)
line.add("平均气温",x_axis,mean_temp,yaxis_formatter="°C")
line.render()

webbrowser.open("file://"+os.path.realpath("一周温度变化.html"))
