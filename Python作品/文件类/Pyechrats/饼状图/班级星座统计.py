from pyecharts import Pie
import webbrowser
import os
import json

with open("birthdaylist.json", "r") as f:
    data = json.load(f)

constellation = {
    "水瓶座": 0,
    "双鱼座": 0,
    "白羊座": 0,
    "金牛座": 0,
    "双子座": 0,
    "巨蟹座": 0,
    "狮子座": 0,
    "处女座": 0,
    "天秤座": 0,
    "天蝎座": 0,
    "射手座": 0,
    "摩羯座": 0,
}

for birthday in data:
    if 1.20 <= birthday <= 2.18:
        constellation["水瓶座"] += 1
    elif 2.19 <= birthday <= 3.20:
        constellation["双鱼座"] += 1
    elif 3.21 <= birthday <= 4.19:
        constellation["白羊座"] += 1
    elif 4.20 <= birthday <= 5.20:
        constellation["金牛座"] += 1
    elif 5.21 <= birthday <= 6.21:
        constellation["双子座"] += 1
    elif 6.22 <= birthday <= 7.22:
        constellation["巨蟹座"] += 1
    elif 7.23 <= birthday <= 8.22:
        constellation["狮子座"] += 1
    elif 8.23 <= birthday <= 9.22:
        constellation["处女座"] += 1
    elif 9.23 <= birthday <= 10.23:
        constellation["天秤座"] += 1
    elif 10.24 <= birthday <= 11.22:
        constellation["天蝎座"] += 1
    elif 11.23 <= birthday <= 12.21:
        constellation["射手座"] += 1
    else:
        constellation["摩羯座"] += 1

key = list(constellation.keys())
value = list(constellation.values())

pie = Pie("班级星座统计", title_pos="center")
pie.add(
    " ",
    key,
    value,
    legend_pos="left",
    legend_orient="vertical",
    is_label_show=True,
)
pie.render()
webbrowser.open("file://" + os.path.realpath("render.html"))