print('''星座填写格式：××座 血型填写格式：×型
    姓名处输入0打印''')
# 十二星座
star_12 = ("白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座",
           "天枰座", "天蝎座", "射手座", "摩羯座", "水瓶座", "双鱼座") 
# 血型
blood_4 = ("A型", "B型", "AB型", "O型")   

name = ""
star = ""
motto = ""
blood = ""
qq = ""
phone = ""
live = ""
yearbook = []
while True:
    ls = []
    name = input("姓名：")
    if name == "0":
        break
    ls.append(name)

    qq = input("QQ:")
    ls.append(qq)

    phone = input("电话号码:")
    ls.append(phone)

    live = input("住址:")
    ls.append(live)

    star = input("星座：")
    while star not in star_12:
        print("这是什么星座？")
        star = input("星座：")
    ls.append(star)

    motto = input("人生格言：")
    ls.append(motto)

    blood = input("血型：")
    while blood not in blood_4:
        print("这是什么血型？")
        blood = input("血型：")
    ls.append(blood)
    yearbook.append(ls)
    print()
print("===============================================")

print("打印同学录")
print(yearbook)
print("===============================================")

print("学生名单")
for x in range(len(yearbook)):
    print(yearbook[x][0])
input()
