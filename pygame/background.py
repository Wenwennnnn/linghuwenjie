import turtle as t
import pygame
import sys
class player(t.Turtle):
    def __init__(self, color, shape, goto):
        super(player, self).__init__()
        self.ht()  # 隐藏动画
        self.up()  # 抬起画笔
        self.score = 1  # 设置默认成绩
# aaaa
