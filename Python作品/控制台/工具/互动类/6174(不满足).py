def max_num(num):
    ls = list(str(num))
    ls.sort(reverse=True)
    s = ''.join(ls)
    return int(s)


def min_num(num):
    ls = list(str(num))
    ls.sort()
    s = ''.join(ls)
    return int(s)


for num in range(1000,10000):
    tmp = num
    times = 0
    while num != 6174 and times <= 7:
        maximum = max_num(num)
        minimum = min_num(num)
        num = maximum - minimum
        #print(maximum, "-", minimum, "=", num)
        times = times + 1

        if num != 6174:
            print(tmp)
            print("最终结果：",num)
input()
