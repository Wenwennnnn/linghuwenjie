import random
class player:
	def __init__(self,strength,dexterity,constitution,intelligence,wisdom,charisma):
		self.strength = strength
		self.dexterity = dexterity
		self.constitution = constitution
		self.intelligence = intelligence
		self.wisdom = wisdom
		self.charisma = charisma
#打印球员参数
p1 = player(15,16,17,18,19,20)
print("strength="+str(p1.strength))
print("dexterity="+str(p1.dexterity))
print("constitution="+str(p1.constitution))
print("intelligence"+str(p1.intelligence))
print("wisdom="+str(p1.wisdom))
print("charisma="+str(p1.charisma))

hitpoints=p1.constitution*30+50
print("hitpoints="+str(hitpoints))
attack = random.randint(1,p1.strength)
print("attack="+str(attack))
defense = random.randint(1,20)
print("defense="+str(defense))
if defense>p1.dexterity:
	attack = attack-defense
print("attack="+str(attack))
#这个位置设置治疗值在0-20之间
heal = random.randint(0,20)
print("heal="+str(heal))
hitpoints = hitpoints + heal
print("hitpoints="+str(hitpoints))