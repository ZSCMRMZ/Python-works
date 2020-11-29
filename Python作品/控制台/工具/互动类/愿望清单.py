wish_list = ['去草原骑马', '去天安门看升旗', '养一只小动物', '在游戏中无可匹敌', '学会画画', '考上自己喜欢的高中']
my_wish = []
while (len(wish_list) != 2):
    print('愿望清单：')
    print(wish_list)
    input_wish = input('请输入你想实现的愿望：')
    if ((input_wish in wish_list) and (input_wish not in my_wish)):
        my_wish.append(input_wish)
        print()
        print('已选择的愿望', input_wish)
        print('你的愿望是', my_wish)
    else:
        print('输入错误，请重新输入！')
input()
