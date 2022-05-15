import turtle as t
class player(t.Turtle):
    def_init_(self,color,shape,goto):
    super(player,self)._init_()
    self.ht()  #隐藏动画
    self.up()  #抬起画笔
    self.score = 0
