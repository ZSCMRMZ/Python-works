list1 = [1, 7, 11, 14, 18, 20, 70, 90, 95, 100, 150 , 200, 240, 280, 300, 320, 340, 440, 500]
print(list1)
target = int(input("请输入目标数字："))
n = 0
for i in range(len(list1)):
    n += 1
    if target == list1[i]:
        print("查询了", n, "次找到了，是第", i+1, "个数字")
        break
else:
    print("没有找到")
input()
