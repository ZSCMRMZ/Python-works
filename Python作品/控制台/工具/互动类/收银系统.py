shop = {"烤鱼干":5,"绿茶":3,"柠檬茶":3,"牛奶":4,"巧克力":5,"坚果零食":8}
shopping_car = {}
total = 0

while True:
    print('''
        ------------------
        商品          单价
        ------------------
        绿茶           3元
        柠檬茶         3元
        牛奶           4元
        巧克力         5元
        烤鱼干         5元
        坚果零食       8元
        ------------------''')
    goods = input("请输入你想要购买的商品名称，退出输入exit，结账输入pay：")
    if goods == "exit":
        print("已退出")
        break
    
    elif goods == "pay":
        print("购物清单")
        for key in shopping_car:
            print("商品：", key, "数量：", shopping_car[key], "单价：",shop[key], "总价：", shopping_car[key]*shop[key])
            total = total + shopping_car[key] * shop[key]
        print("您需支付：",total)
        break
    else:
        if goods in shop:
            goods_number = int(input("请输入购买数量："))
            if goods in shopping_car:
                shopping_car[goods] = shopping_car[goods] + goods_number
            else:
                shopping_car[goods] = goods_number
        else:
                print("无此商品，请重新输入：")
input()
