import random

puzzle_list = ['一只黑狗，不叫不吼', '一口咬定', '一加一', '一只狗四个口', '九点', '十二点']
riddle_list = ['默', '交', '王', '器', '丸', '斗']

while (len(puzzle_list) != 0):
    random_index = random.randint(0, (len(puzzle_list) - 1))
    puzzle = puzzle_list[random_index]
    print('请根据以下谜题，输入谜底进行解答，猜一个字')
    answer = input((puzzle + ':'))
    if (answer == riddle_list[random_index]):
        print('恭喜你猜对了~~~')
        puzzle_list.pop(random_index)
        riddle_list.pop(random_index)
    else:
        print('很遗憾，猜错了')
input()
