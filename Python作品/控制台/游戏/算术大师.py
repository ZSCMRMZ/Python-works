import random
import time


print('欢迎使用CodeMao减法智能出题器')
x = int(input('请输入你想挑战的减数范围，例如：0-100(输入100)'))
print('您已经选择0-', x, '范围，请在5秒内作答，否则按照错误处理，挑战马上开始')
score = 0

for i in range(10):
    a = 0
    b = 0
    while (a <= b):
        a = random.randint(0, x)
        b = random.randint(0, x)
    prompt = (((str(a) + '-') + str(b)) + '等于几？')
    print(prompt)
    start_time = time.time()
    answer = int(input('请输入你的答案:'))
    end_time = time.time()
    if (end_time - start_time >= 5):
        print('回答错误，您已经超时')
        break
    else:
        if (answer == a - b):
            print('回答正确')
            score = (score + 1)
        else:
            print('回答错误')
            break

title = ''
if (x <= 10 and score >= 6):
    title = '白银小将'
elif (x <= 50 and score >= 7):
    title = '黄金大师'
elif (x <= 100 and score >= 8):
    title = '荣耀宗师'
elif (x > 100 and score >= 9):
    title = '至尊王者'
else:
    pass
print('获得的称号是：', title)
input()
