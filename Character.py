import random

class Character:
	def __init_(self):
		self.abilities = None
		self.name = "Baldr Hellhammer"
		self.characterClass = "Fighter"
		self.race = "Dwarf"
		self.alignment = "LN"
		self.background = "Mercenary"
		self.hp = 12
		self.proficiency = 1
	
	def setAbilities(self):
		self.abilities = [0, 0, 0, 0, 0, 0]
		for x in range(6):
			self.abilities[x] = random.randint(8, 16)
	
