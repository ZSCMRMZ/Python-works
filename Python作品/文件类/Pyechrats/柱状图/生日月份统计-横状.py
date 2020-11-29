import json
from pyecharts import Bar
import webbrowser
import os

with open("birthday.json", "r") as f:
    data = json.load(f)

# print(data)

# for i in data:
#     print(int(i))

# print(len(data))

list_month = [0] * 12
# print(list_month)

for i in data:
    list_month[int(i)-1] += 1
# print(list_month)

x_axis = ["1月", "2月", "3月", "4月", "5月", "6月",
          "7月", "8月", "9月", "10月", "11月", "12月"]
y_axis = list_month

bar = Bar("生日月份统计")
bar.add("", x_axis, y_axis, is_convert = True, xaxis_rotate = 30, yaxis_rotate = 30)
bar.render()
webbrowser.open("file://" + os.path.realpath("生日月份统计-横状.html"))
