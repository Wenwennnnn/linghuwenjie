import random
suijishu = []
for i in range(0,6):
	n = random.randint(0,20)
	suijishu.append(n)
character_linghuwenjieList =["strength","dexterity","constitution"," intelligence","wisdom","charisma"]
character_linghuwenjie = {}
character_linghuwenjie = {key: value for key, value in zip(character_linghuwenjieList, suijishu)}
print(character_linghuwenjie)