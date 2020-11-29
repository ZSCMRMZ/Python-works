from pyecharts import Pie
import webbrowser
import os

tag = ["11岁", "12岁", "13岁", "14岁", "15岁", "16岁"]
people = [6, 10, 18, 6, 10, 30]
pie = Pie("学习小组年龄分布", title_pos="center")
pie.add(
    " ",
    tag,
    people,
    legend_pos="left",
    legend_orient="vertical",
    is_label_show=True
)
pie.render()
webbrowser.open("file://" + os.path.realpath("学习小组年龄分布.html"))
