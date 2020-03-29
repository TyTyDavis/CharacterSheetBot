import random
import writer
import fantasy_name_generator
import weapons
import armors
import spells

martialWeapons = [weapons.Battleaxe(), weapons.Flail(), weapons.Glaive(), weapons.Greatsword(), weapons.Halberd(), weapons.Lance(), weapons.Longsword(), weapons.Maul(), weapons.Morningstar(), weapons.Pike(), weapons.Rapier(), weapons.Scimitar(), weapons.Shortsword(), weapons.Trident(), weapons.Warpick(), weapons.Warhammer(), weapons.Whip()]
martialRangedWeapons = [weapons.Longbow()] #update!
simpleWeapons = [weapons.Club(), weapons.Dagger(), weapons.Greatclub(), weapons.Handaxe(), weapons.Javelin(), weapons.LightHammer(), weapons.Mace(), weapons.Quarterstaff(), weapons.Sickle(), weapons.Spear()]
simpleRangedWeapons = [weapons.Dart()] #update~
lightArmor = [armors.Padded(), armors.Leather(), armors.StuddedLeather(), ]
mediumArmor = [armors.Hide(), armors.ChainShirt(), armors.ScaleMail(), armors.Breastplate(), armors.HalfPlate()]
heavyArmor = [armors.RingMail(), armors.ChainMail(), armors.Splint(), armors.Plate()]

def maxKey(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]
	 
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
		self.AC = 10
		self.silly = None
		self.caster = False
	
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
		self.abilities = {
			"Str": 0,
			"Dex": 0,
			"Con": 0,
			"Int": 0,
			"Wis": 0,
			"Cha": 0
			}
		for x in self.abilities:
			self.abilities[x] = random.randint(8, 16)
	
	def setClass(self, abilities):
		classList = None
		if random.randint(1,10) <= 2:
			classList = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard"]
			self.silly = True
		else:
			self.silly = False
			if maxKey(self.abilities) == "Str":
				classList = ["Barbarian", "Fighter", "Paladin"]
			elif maxKey(self.abilities) == "Dex":
				classList = ["Monk", "Ranger", "Rogue"]
			elif maxKey(self.abilities) == "Con":
				classList = ["Fighter", "Barbarian", "Cleric"]
			elif maxKey(self.abilities) == "Int":
				classList = ["Wizard", "Wizard", "Wizard", "Bard"]
			elif maxKey(self.abilities) == "Wis":
				classList = ["Cleric", "Druid"]
			elif maxKey(self.abilities) == "Cha":
				classList = ["Bard", "Sorceror", "Warlock"]
			else:
				classList = ["Wizard", "Fighter", "Cleric", "Rogue", "Bard"]
		self.characterClass = random.choice(classList)
		if self.characterClass == "Wizard" or self.characterClass == "Sorceror" or self.characterClass == "Warlock" or self.characterClass == "Druid" or self.characterClass == "Bard" or self.characterClass == "Cleric":
			self.caster = True
		else:
			self.caster = False
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
			self.abilities["Con"] += 2
		elif self.race == "Elf":
			self.abilities["Dex"] += 2
		elif self.race == "Halfling":
			self.abilities["Dex"] += 2
		elif self.race == "Human":
			for x in self.abilities:
				self.abilities[x] += 1
		elif self.race == "Dragonborn":
			self.abilities["Str"] += 2
			self.abilities["Cha"] += 1
		elif self.race == "Gnome":
			self.abilities["Int"] += 2
		elif self.race == "Half-Elf":
			self.abilities["Cha"] += 2
			ab = ["Str", "Dex", "Con", "Int", "Wis"]
			a = random.choice(ab)
			self.abilities[a] += 1
			ab.remove(a)
			self.abilities[random.choice(ab)] += 1
		elif self.race == "Half-Orc":
			self.abilities["Str"] += 2
			self.abilities["Con"] += 1
		elif self.race == "Tiefling":
			self.abilities["Int"] += 1
			self.abilities["Cha"] += 2
	
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
		
		self.hp = self.hitDie + writer.abilityBonus(self.abilities["Con"])
		
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
		equipmentChoices = ["Caltrops", "Candle", "Crowbar", "Lamp", "Lock", "Manacles", "Rope", "Tent", "Tinderbox", "Torch"]
		equipmentCount = 2
		if self.characterClass == "Barbararian":
			self.weapon1 = random.choice(martialWeapons)
			self.weapon2 = random.choice(simpleWeapons)
			self.armor = random.choice(mediumArmor)
		elif self.characterClass == "Bard":
			self.weapon1 = random.choice([weapons.Rapier(), weapons.Longsword(), weapons.Shortword(), weapons.Club(), weapons.Dagger(), weapons.GreatClub(), weapons.Handaxe(), weapons.Javelin(), weapons.Lighthammer(), weapons.Mace(), weapons.Quarterstaff(), weapons.Sickle(), weapons.Spear()])
			self.weapon2 = random.choice([weapons.Dagger(), weapons.Shortbow(), weapons.LightCrossbow()])
			self.armor = random.choice(lightArmor)
		elif self.characterClass == "Cleric":
			self.weapon1 = random.choice([weapons.Mace(), weapons.Warhammer(), weapons.Sickle(), weapons.Greatclub()])
			self.weapon2 = random.choice(simpleRangedWeapons)
			self.armor = random.choice(mediumArmor)
		elif self.characterClass == "Druid":
			self.weapon1 = random.choice([weapons.Club(), weapons.Dagger(), weapons.Mace(), weapons.Quarterstaff(), weapons.Scimitar(), weapons.Sickle(), weapons.Spear()])
			self.weapon2 = random.choice([weapons.Dagger(), weapons.Dart()])
			self.armor = random.choice([armors.Padded(), armors.Leather(), armors.Hide()])
		elif self.characterClass == "Fighter":
			self.weapon1 = random.choice(martialWeapons)
			self.weapon2 = random.choice(simpleWeapons)
			self.armor = random.choice(heavyArmor)
		elif self.characterClass == "Barbararian":
			self.weapon1 = random.choice(martialWeapons)
			self.weapon2 = random.choice(simpleWeapons)
			self.armor = random.choice(mediumArmor)
		elif self.characterClass == "Monk":
			self.weapon1 = weapons.MonkHands()
			self.weapon2 = random.choice(simpleWeapons)
			self.armor = None
		elif self.characterClass == "Paladin":
			self.weapon1 = random.choice(martialWeapons)
			self.weapon2 = random.choice(simpleWeapons)
			self.armor = random.choice(heavyArmor)
		elif self.characterClass == "Ranger":
			self.weapon1 = random.choice(simpleWeapons)
			self.weapon2 = weapons.Longbow()
			self.armor = random.choice(lightArmor)
		elif self.characterClass == "Rogue":
			self.weapon1 = random.choice(simpleWeapons)
			self.weapon2 = random.choice(simpleRangedWeapons)
			self.armor = random.choice(lightArmor)
		elif self.characterClass == "Sorceror":
			self.weapon1 = random.choice([weapons.Dagger(), weapons.Dart(), weapons.LightCrossbow()])
			self.weapon2 = None
			self.armor = None
		elif self.characterClass == "Warlock":
			self.weapon1 = random.choice(simpleWeapons)
			self.weapon2 = None
			self.armor = random.choice(lightArmor)
		elif self.characterClass == "Wizard":
			self.weapon1 = random.choice([weapons.Dagger(), weapons.Dart(), weapons.LightCrossbow()])
			self.weapon2 = None
			self.armor = None
		
		
		if self.armor != None: 
			self.ac = self.armor.ac + writer.abilityBonus(self.abilities["dex"])
		else:
			self.ac = 10 + writer.abilityBonus(self.abilities["Dex"])
		if self.weapon1 != None and self.weapon1.name != "Unarmed": self.equipment.append(self.weapon1.name)
		if self.weapon2 != None: self.equipment.append(self.weapon2.name)
		if self.armor != None: self.equipment.append(self.armor.name)
		count = 0
		while count < equipmentCount:
			chosen = random.choice(equipmentChoices)
			self.equipment.append(chosen)
			equipmentChoices.remove(chosen)
			count += 1
		self.GP = 3
		self.SP = 5
		self.CP = 10
		
	def testEquipment(self):
		self.equipment = ["shortsword", "dagger", "buckler", "pouch", "lucky coin", "ink bottle", "flint and steel", "parchment"]
		self.GP = 3
		self.SP = 5
		self.CP = 10