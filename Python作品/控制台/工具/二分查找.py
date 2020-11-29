list_num =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_num)
target = int(input("请输入目标数字："))

def binary_search(target, list_num):
    low = 0
    high = len(list_num) - 1
    while True:
        middle = (low +high) // 2
        temp = list_num[middle]
        if temp == target:
            print("找到了， 它的位置是", middle+1, "个数字")
            break
        elif temp < target:
            low = middle + 1
        else:
            high = middle - 1

binary_search(target, list_num)
input()
