import turtle as t
class player(t.Turtle):
    def_init_(self,color,shape,goto):
    super(player,self)._init_()
    self.ht()  #隐藏动画
    self.up()  #抬起画笔
    self.score = 0 #设置默认成绩
    self.color(color) #设置颜色
    self.speed()
 
