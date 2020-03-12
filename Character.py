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
		self.silly = None
	
	def setAbilities(self):
		self.abilities = [0, 0, 0, 0, 0, 0]
		for x in range(6):
			self.abilities[x] = random.randint(8, 16)
	
	def setClass(self, abilities):
		classList = None
		if random.randint(1,10) <= 1:
			classList = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard"]
			self.silly = True
		else:
			self.silly = False
			if abilities.index(max(abilities)) == 0:
				classList = ["Barbarian", "Fighter", "Paladin"]
			elif abilities.index(max(abilities)) == 1:
				classList = ["Monk", "Ranger", "Rogue"]
			elif abilities.index(max(abilities)) == 2:
				classList = ["Fighter", "Barbarian", "Cleric"]
			elif abilities.index(max(abilities)) == 3:
				classList = ["Wizard", "Wizard", "Wizard", "Bard"]
			elif abilities.index(max(abilities)) == 4:
				classList = ["Cleric", "Druid"]
			elif abilities.index(max(abilities)) == 5:
				classList = ["Bard", "Sorceror", "Warlock"]
			else:
				classList = ["Wizard", "Fighter", "Cleric", "Rogue", "Bard"]
		self.characterClass = random.choice(classList)
	
	def setRace(self, characterClass):
		raceList = None
		if self.silly == True:
			raceList = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]
		else:
			if characterClass == "Barbarian":
				raceList = ["Half-Orc", "Human", "Dragonborn"]
			elif characterClass == "Bard":
				raceList = ["Elf", "Gnome", "Half-Elf", "Halfling", "Human", "Tiefling"]
			elif characterClass == "Cleric":
				raceList = ["Dwarf", "Elf", "Human", "Dragonborn"]
			elif characterClass == "Druid":
				raceList = ["Elf", "Half-Elf", "Human", "Tiefling"]
			elif characterClass == "Fighter":
				raceList = ["Dragonborn", "Dwarf", "Half-Orc", "Human"]
			elif characterClass == "Monk":
				raceList = ["Elf", "Half-Elf", "Human"]
			elif characterClass == "Paladin":
				raceList = ["Dragonborn", "Dwarf", "Half-Elf", "Half-Orc", "Human"]
			elif characterClass == "Ranger":
				raceList = ["Elf", "Half-Elf", "Human"]
			elif characterClass == "Rogue":
				raceList = ["Elf", "Half-Elf", "Gnome", "Halfling", "Human"]
			elif characterClass == "Sorceror":
				raceList = ["Elf", "Half-Elf", "Human", "Gnome", "Halfling", "Tiefling"]
			elif characterClass == "Warlock":
				raceList = ["Tiefling", "Human", "Half-Elf", "Dragonborn"]
			elif characterClass == "Wizard":
				raceList = ["Elf", "Half-Elf", "Human", "Gnome"]
			else:
				raceList = ["Human"]
		self.race = random.choice(raceList)
		
			