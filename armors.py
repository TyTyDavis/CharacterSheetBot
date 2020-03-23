class Armor:
	def __init__(self):
		pass
	
#light armor	
class Padded(Armor):
	name = "Padded armor"
	ac = 11
	weight = 8
	stealthDis = True
	
class Leather(Armor):
	name = "Leather armor"
	ac = 11
	weight = 10
	stealthDis = False

class StuddedLeather(Armor):
	name = "Studded leather armor"
	ac = 12
	weight = 13
	stealthDis = False

#medium armor
class Hide(Armor):
	name = "Hide armor"
	ac = 12
	weight = 12
	stealthDis = False
	
class ChainShirt(Armor):
	name = "Chain shirt"
	ac = 13
	weight = 20
	stealthDis = False
	
class ScaleMail(Armor):
	name = "Scale mail"
	ac = 14
	weight = 45
	stealthDis = True
	
class Breastplate(Armor):
	name = "Breastplate"
	ac = 14
	weight = 20
	stealthDis = False
	
class HalfPlate(Armor):
	name = "Half plate armor"
	ac = 15
	weight = 40
	stealthDis = True

#heavy armor
class RingMail(Armor):
	name = "Ring mail armor"
	ac = 14
	weight = 40
	stealthDis = True

class ChainMail(Armor):
	name = "Chain mail armor"
	ac = 16
	weight = 55
	stealthDis = True
	
class Splint(Armor):
	name = "Splint armor"
	ac = 17
	weight = 60
	stealthDis = True
	
class Plate(Armor):
	name = "Plate armor"
	ac = 17
	weight = 60
	stealthDis = True







