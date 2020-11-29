import turtle
pen = turtle.Pen()
pen.speed(0)

family_name_list = ['李', '王', '张', '刘', '陈', '杨', '赵', '黄', '周', '吴',
                    '徐', '孙', '胡', '朱', '高', '林', '何', '郭', '马', '罗',
                    '梁', '宋', '郑', '谢', '韩', '唐', '冯', '于', '董', '萧',
                    '程', '曹', '袁', '邓', '许', '傅', '沈', '曾', '彭', '吕',
                    '苏', '卢', '蒋', '蔡', '贾', '丁', '魏', '薛', '叶', '阎',
                    '余', '潘', '杜', '戴', '夏', '钟', '汪', '田', '任', '姜',
                    '范', '方', '石', '姚', '谭', '廖', '邹', '熊', '金', '陆',
                    '郝', '孔', '白', '崔', '康', '毛', '邱', '秦', '江', '史',
                    '顾', '侯', '邵', '孟', '龙', '万', '段', '漕', '钱', '汤',
                    '尹', '黎', '易', '常', '武', '乔', '贺', '赖', '龚', '文']

def get(family_name):
    for i in family_name_list:
        if i == family_name:
            return "你的姓在百家姓中排：" + str(family_name_list.index(i) + 1)

    else:
        return "你居然拥有这么罕见的姓，幸会幸会！"

def draw(info):
    index = 0
    for k in range(10):
        for j in range(10):
            pen.penup()
            x = -250 + j*50
            y = 250 - 50*k
            pen.goto(x, y)
            pen.pendown()
            for i in range(4):
                pen.forward(50)
                pen.right(90)
            pen.up()
            pen.goto(x + 25, -25-15+y)
            pen.pendown()
            pen.write(family_name_list[index], align="center", font=("楷体", 20, "normal"))
            index += 1
    pen.penup()
    pen.goto(0, -300)
    pen.write(info, align="center", font=("楷体", 20, "normal"))

family_name = turtle.textinput("百家姓", "请输入你的姓")
info = get(family_name)
draw(info)

turtle.done()