#coding:utf-8
import random

secret = random.randint(1,10)
print('----------------------我爱鱼C工作室--------------------------')
temp = input('不妨猜一下小甲鱼现在的心里想的是哪个数字：')
guess = int(temp)
while guess != secret:
    temp = input('哎呀，猜错了，请重新输入吧：')
    guess = int(temp)
    if guess == secret:
        print('我草，你是小甲鱼心里的蛔虫吗？！')
        print('哼，猜中了也没有奖励呀！')
    else:
        if guess > secret:
            print('哥,大了大了~~~')
        else:
            print('嘿嘿，小了小了~~~~')
print('游戏结束，不玩了^_^')
