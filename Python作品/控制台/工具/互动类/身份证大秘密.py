id_number = input('请输入身份证号：')
while (len(id_number) != 18):
    print('输入有误')
    id_number = input('请输入身份证号：')

gender = int(id_number[(-2)])
if (gender % 2 == 0):
    print('性别：女')
else:
    print('性别：男')

year = id_number[6:10]
month = id_number[10:12]
day = id_number[12:14]
birthday = ((((year + '-') + month) + '-') + day)
print('出生日期：', birthday)
input()
