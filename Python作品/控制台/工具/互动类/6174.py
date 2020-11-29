def max_num(num):
    ls = list(str(num))
    ls.sort(reverse=True)
    s  = ''.join(ls)
    return int(s)

def min_num(num):
    ls = list(str(num))
    ls.sort()
    s = ''.join(ls)
    return int(s)

while True:
    num = int(input("请输入一个不完全相同的四位正整数："))
    times = 0
    while num != 6174 and times <=7:
        maximum = max_num(num)
        minimum = min_num(num)
        num = maximum - minimum
        print(maximum, "-", minimum, "=", num)
        times = times + 1