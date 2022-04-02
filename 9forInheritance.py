import random
class Person:
	def __init__(self,strength,dexterity,constitution,intelligence,wisdom,charisma):
		self.strength = strength
		self.dexterity = dexterity
		self.constitution = constitution
		self.intelligence = intelligence
		self.wisdom = wisdom
		self.charisma = charisma

class Student(Person):
    def  __init__(self,strength,dexterity,constitution,intelligence,wisdom,charisma):#调用这个函数将覆盖最初的父函数
        super().__init__(strength,dexterity,constitution,intelligence,wisdom,charisma)
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

p1 = Student(15,16,17,18,19,20)
print("strength="+str(p1.strength))
print("dexterity="+str(p1.dexterity))
print("constitution="+str(p1.constitution))
print("intelligence"+str(p1.intelligence))
print("wisdom="+str(p1.wisdom))
print("charisma="+str(p1.charisma))

mana = p1.intelligence*30+50
print("mana="+str(mana))
magicMissile = random.randint(5,10)
mana = mana-5
print("mana="+str(mana))
fireball = random.randint(10,20)
mana = mana-10
print("mana="+str(mana))









