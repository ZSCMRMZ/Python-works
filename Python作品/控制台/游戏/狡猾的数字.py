import random

# 猜想范围最小值
min_num = random.randint(0, 50)
# 猜想范围最大值
max_num = random.randint(200, 300)
# 答案
answer = random.randint(min_num, max_num)
# 用户猜想数字
guess_num = (-1)
# 用户猜想次数
guess_times = 7

print('狡猾的数字')
while (guess_num != answer):
    # 猜想次数用完
    if (guess_times == 0):
        print('很遗憾，没猜对！')
        break
    # 打印猜想范围
    print(min_num, '<= ? <=', max_num)
    # 输入猜想数字
    guess_num = int(input('请输入猜想数字：'))
    # 判断范围
    if (guess_num > max_num or guess_num < min_num):
        print('注意范围！')
        continue
    # 判断猜想结果
    if (guess_num == answer):
        print('恭喜你，猜对了！')
    elif (guess_num > answer):
        max_num = guess_num
    else:
        min_num = guess_num
    # 更新猜想次数
    guess_times = (guess_times - 1)
input()
