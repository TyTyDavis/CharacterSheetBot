import random
import writer
import fantasy_name_generator

class Character:
	def __init_(self):
		self.abilities = None
		self.name = None
		self.gender = None
		self.characterClass = "Fighter"
		self.race = "Dwarf"
		self.alignment = "LN"
		self.background = "Mercenary"
		self.hitDie = 8
		self.hp = 12
		self.proficiency = 2
		self.speed = 20
		self.silly = None
	
	def setName(self):
		if self.gender == "M":
			self.name = fantasy_name_generator.name_builder(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\first_name_male.txt", r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\last_name.txt")
		elif self.gender == "F":
			self.name = fantasy_name_generator.name_builder(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\first_name_female.txt", r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\last_name.txt")
		else:
			self.name = fantasy_name_generator.name_builder(random.choice([r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\first_name_male.txt", r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\first_name_female.txt"]), r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\last_name.txt")
	
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
	
	def setHP(self):
		if self.characterClass == "Barbarian":
			self.hitDie = 12
		elif self.characterClass == "Bard":
			self.hitDie = 8
		elif self.characterClass == "Cleric":
			self.hitDie = 8
		elif self.characterClass == "Druid":
			self.hitDie = 8
		elif self.characterClass == "Fighter":
			self.hitDie = 10
		elif self.characterClass == "Monk":
			self.hitDie = 8
		elif self.characterClass == "Paladin":
			self.hitDie = 10
		elif self.characterClass == "Ranger":
			self.hitDie = 10
		elif self.characterClass == "Rogue":
			self.hitDie = 8
		elif self.characterClass == "Sorceror":
			self.hitDie = 6
		elif self.characterClass == "Warlock":
			self.hitDie = 8
		elif self.characterClass == "Wizard":
			self.hitDie = 6
		
		self.hp = self.hitDie + writer.abilityBonus(self.abilities[2])
		
	def setAlignment(self):
		alignment = ["L", "G"]
		if self.characterClass == "Barbarian":
			alignment[0] = "C"
			alignment[1] = random.choice(["G", "N"])
		elif self.characterClass == "Bard":
			alignment[0] = "C"
			alignment[1] = random.choice(["G", "N"])
		elif self.characterClass == "Paladin":
			alignment[0] = "L"
			alignment[1] = random.choice(["G", "N"])
		elif self.characterClass == "Rogue":
			alignment[0] = "C"
			alignment[1] = random.choice(["G", "N"])
		else:	
			alignment[0] = random.choice(["L", "N", "C"])
			alignment[1] = random.choice(["G", "N"])
			
		if random.randint(1, 100) <= 2:
			alignment[2] = "E"
			
		self.alignment = alignment
	
	def setSpeed(self):
	#to do: include armor in calculation
		if self.race == "Gnome" or self.race == "Halfling" or self.race == "Dwarf":
			self.speed = 25
		elif self.race == "Tiefling" or self.race == "Half-Orc" or self.race == "Half-Elf" or self.race == "Dragonborn" or self.race == "Human" or self.race == "Elf":
			self.speed = 30
		else:
			self.speed = 30

			