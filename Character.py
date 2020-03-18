import random
import writer
import fantasy_name_generator


martialWeapons = ["battleaxe", "Flail", "glaive", "greatsword", "halberd", "lance", "longsword", "maul", "morningstar", "pike", "rapier", "scimitar", "shortsword", "trident", "war pick", "warhammer", "whip"]
simpleWeapons = ["club", "dagger", "greatclub", "handaxe", "javelin", "light hammer", "mace", "quarterstaff", "sickle", "spear"]
mediumArmor = ["hide armor", "chain shirt", "scale mail", "breastplate", "half plate armor"]
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
		firstName = None
		LastName = None
		
		if self.gender == "M":
			firstName = r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\first_name_female.txt" 
		elif self.gender == "F":
			firstName = r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\first_name_female.txt"
		else:
			firstName = self.name = random.choice([r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\first_name_male.txt", r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\first_name_female.txt"])
		
		if self.silly == True:
			lastName = r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\first_name_female.txt", r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\silly_last_names.txt"
		else: 
			
			lastName = r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\first_name_female.txt", r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\last_name.txt"
		self.name = fantasy_name_generator.name_builder(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\first_name_female.txt", r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\last_name.txt")
	def setAbilities(self):
		self.abilities = [0, 0, 0, 0, 0, 0]
		for x in range(6):
			self.abilities[x] = random.randint(8, 16)
	
	def setClass(self, abilities):
		classList = None
		if random.randint(1,10) <= 2:
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
		
		if self.race == "Dwarf":
			self.abilities[2] += 2
		elif self.race == "Elf":
			self.abilities[1] += 2
		elif self.race == "Halfling":
			self.abilities[1] += 2
		elif self.race == "Human":
			for x in range(6):
				self.abilities[x] += 1
		elif self.race == "Dragonborn":
			self.abilities[0] += 2
			self.abilities[5] += 1
		elif self.race == "Gnome":
			self.abilities[3] += 2
		elif self.race == "Half-Elf":
			self.abilities[5] += 2
			self.abilities[random.randint(0, 4)] += 1
			self.abilities[random.randint(0, 4)] += 1
		elif self.race == "Half-Orc":
			self.abilities[0] += 2
			self.abilities[2] += 1
		elif self.race == "Tiefling":
			self.abilities[3] += 1
			self.abilities[5] += 2
	
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
			alignment[1] = "E"
			
		self.alignment = alignment
	
	def setSpeed(self):
	#to do: include armor in calculation
		if self.race == "Gnome" or self.race == "Halfling" or self.race == "Dwarf":
			self.speed = 25
		elif self.race == "Tiefling" or self.race == "Half-Orc" or self.race == "Half-Elf" or self.race == "Dragonborn" or self.race == "Human" or self.race == "Elf":
			self.speed = 30
		else:
			self.speed = 30
	
	def setSkills(self):
		skillChoices = None
		numChoices = 2
		self.skills = {
			"Acrobatics": False,
			"Animal Handling": False,
			"Arcana": False,
			"Athletics": False,
			"Deception": False,
			"History": False,
			"Insight": False,
			"Intimidation": False,
			"Investigation": False,
			"Medicine": False,
			"Nature": False,
			"Perception": False,
			"Performance": False,
			"Persuasion": False,
			"Religion": False,
			"Sleight of Hand": False,
			"Stealth": False,
			"Survival": False
		}
		if self.characterClass == "Barbarian":
			numChoices = 2
			skillChoices = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
		elif self.characterClass == "Bard":
			numChoices = 3
			skillChoices = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
		elif self.characterClass == "Cleric":
			numChoices = 2
			skillChoices = ["History", "Insight", "Medicine", "Persuasion", "Religion"]
		elif self.characterClass == "Druid":
			numChoices = 2
			skillChoices = ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]
		elif self.characterClass == "Fighter":
			numChoices = 2
			skillChoices = ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
		elif self.characterClass == "Monk":
			numChoices = 2
			skillChoices = ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]
		elif self.characterClass == "Paladin":
			numChoices = 2
			skillChoices = ["Athletics", "Intimidation", "Insight", "Medicine", "Persuasion", "Religion"]
		elif self.characterClass == "Ranger":
			numChoices = 3
			skillChoices = ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]
		elif self.characterClass == "Rogue":
			numChoices = 4
			skillChoices = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand",  "Stealth"]
		elif self.characterClass == "Sorceror":
			numChoices = 2
			skillChoices = ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]
		elif self.characterClass == "Warlock":
			numChoices = 2
			skillChoices = ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]
		elif self.characterClass == "Wizard":
			numChoices = 2
			skillChoices = ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
		count = 0
		while count < numChoices:
			chosen = random.choice(skillChoices)
			self.skills[chosen] = True
			skillChoices.remove(chosen)
			count += 1
	
	def testSkills(self):		
		self.skills = {
				"Acrobatics": True,
				"Animal Handling": True,
				"Arcana": True,
				"Athletics": True,
				"Deception": True,
				"History": True,
				"Insight": True,
				"Intimidation": True,
				"Investigation": True,
				"Medicine": True,
				"Nature": True,
				"Perception": True,
				"Performance": True,
				"Persuasion": True,
				"Religion": True,
				"Sleight of Hand": True,
				"Stealth": True,
				"Survival": True
			}
	def setEquipment(self):
		self.weapon1 = None
		self.weapon2 = None
		self.armor = None
		self.shield = None
		self.equipment = []
		equipmentChoices = []
		if self.characterClass == "Barbararian":
			self.weapon1 = random.choice(martialWeapons)
			self.weapon2 = random.choice(simpleWeapons)
			self.armor = random.choice(mediumArmor)
		else:
			self.weapon1 = random.choice(martialWeapons)
			self.weapon2 = random.choice(["handaxe", "dagger"])
			self.armor = random.choice(mediumArmor)
			
		self.equipment.append(self.weapon1)
		self.equipment.append(self.weapon2)
		self.equipment.append(self.armor)
		self.GP = 3
		self.SP = 5
		self.CP = 10
		
	def testEquipment(self):
		self.equipment = ["shortsword", "dagger", "buckler", "pouch", "lucky coin", "ink bottle", "flint and steel", "parchment"]
		self.GP = 3
		self.SP = 5
		self.CP = 10