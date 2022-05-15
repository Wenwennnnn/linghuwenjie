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
    pygame.init()  #初始化背景设置
    screen = pygame.display.set_mode((1200,800))  #创建一个名为screen的窗口
    pygame.display.set_caption("Aline Invasion") #设置当前窗口标题
    bg_color = (230,230,230) #设置背景颜色
#开始游戏的主循环
while True:
    for envent in pygame.event.get(): #监听用户事件
        if event.type == pygame.QUIT: #判断用户是否点击了关闭按钮
                 sys.exit() #用户退出
        scrren.fill(bg_color)