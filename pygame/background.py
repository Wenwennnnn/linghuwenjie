import turtle as t
import pygame
import sys
class player(t.Turtle):
    def __init__(self, color, shape, goto):
        super(player, self).__init__()
        self.ht()  # 隐藏动画
        self.up()  # 抬起画笔
        self.score = 1  # 设置默认成绩
        self.color(color) #设置颜色
        self.speed(0) #设置速度
        self.goto(goto) #设置默认位置
        self.shape(shape) #设置形状
        self.shapesize(5,1) #设置形状比例
        self.st() #显示动画

def run_game():
    """初始化游戏，并创建一个屏幕对象"""