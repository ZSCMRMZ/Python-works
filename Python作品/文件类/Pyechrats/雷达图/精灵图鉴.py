from pyecharts import Radar
import json
import webbrowser
import os

with open("sprites.json", encoding="utf-8") as f:
    sprites = json.load(f)
print(sprites)

sprites_property =[
    sprites["编程猫"]["生命"],
    sprites["编程猫"]["攻击"],
    sprites["编程猫"]["特攻"],
    sprites["编程猫"]["速度"],
    sprites["编程猫"]["防御"],
    sprites["编程猫"]["特防"],
]

mao_schema = [
    {"name": "生命", "max": 800},
    {"name": "攻击", "max": 300},
    {"name": "特攻", "max": 300},
    {"name": "速度", "max": 300},
    {"name": "防御", "max": 300},
    {"name": "特防", "max": 300},
    ]
chart = Radar("精灵属性图谱", title_pos="center")
chart.config(c_schema = mao_schema, shape="circle")
chart.add("编程猫", 
        [sprites_property], 
        legend_pos="left", 
        legend_orient="vertical",
        item_color=["#4e79a7"])
chart.render()
webbrowser.open("file://" + os.path.realpath("精灵属性图谱.html"))
