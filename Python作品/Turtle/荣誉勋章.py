import turtle  # 导入海龟库
print("ps.只支持100分及以下~")
chinese_score = turtle.numinput('成绩单', '语文')  # 获取用户输入的语文分数并存储到变量chinese_score中
math_score = turtle.numinput('成绩单', '数学')  # 获取用户输入的数学分数并存储到变量math_score中
english_score = turtle.numinput('成绩单', '英语')  # 获取用户输入的英语分数并存储到变量english_score中
if 0 <= chinese_score <= 100 and 0 <= math_score <= 100 and 0 <= english_score <= 100:
    print('语文分数：', chinese_score)  # 打印变量chinese_score
    print('数学分数：', math_score)     # 打印变量math_score
    print('英语分数：', english_score)  # 打印变量english_score

    if chinese_score > 90 and math_score > 90 and english_score > 90:  # 判断三科成绩是否都大于90分
        print('获得荣誉勋章啦！别太骄傲喔~')
        pen = turtle.Pen()
        pen.dot(100, 'gold')
        pen.dot(90, 'orange')
        pen.dot(80, 'gold')
        pen.dot(70, 'orange')
        pen.up()
        # 画笔上移
        pen.goto(0, 10)
        # 设置画笔填充颜色
        pen.fillcolor('red')
        # 设置画笔形状
        pen.shape('turtle')
        # 拓印海龟
        pen.stamp()
        # 画笔下移
        pen.goto(-25, -20)
        # 写出优秀训练师
        pen.write('优秀训练师')
        # 隐藏画笔
        pen.hideturtle()
        turtle.done()
    elif chinese_score < 60 or math_score < 60 or english_score < 60:  # 判断三科中是否有不及格的
        print('别灰心，下次努力吧~')
    else:
        print('再接再厉，我看好你哦~')
else:
    print("emmm不看ps嘛")
