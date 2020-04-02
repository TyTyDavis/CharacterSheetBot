import random
import writer
import fantasy_name_generator
import weapons
import armors
import spells
import backgrounds
import classes

martialWeapons = [weapons.Battleaxe(), weapons.Flail(), weapons.Glaive(), weapons.Greatsword(), weapons.Halberd(), weapons.Lance(), weapons.Longsword(), weapons.Maul(), weapons.Morningstar(), weapons.Pike(), weapons.Rapier(), weapons.Scimitar(), weapons.Shortsword(), weapons.Trident(), weapons.Warpick(), weapons.Warhammer(), weapons.Whip()]
martialRangedWeapons = [weapons.Longbow()] #update!
simpleWeapons = [weapons.Club(), weapons.Dagger(), weapons.Greatclub(), weapons.Handaxe(), weapons.Javelin(), weapons.LightHammer(), weapons.Mace(), weapons.Quarterstaff(), weapons.Sickle(), weapons.Spear()]
simpleRangedWeapons = [weapons.Dart()] #update~
lightArmor = [armors.Padded(), armors.Leather(), armors.StuddedLeather(), ]
mediumArmor = [armors.Hide(), armors.ChainShirt(), armors.ScaleMail(), armors.Breastplate(), armors.HalfPlate()]
heavyArmor = [armors.RingMail(), armors.ChainMail(), armors.Splint(), armors.Plate()]
backgrounds = [		
			backgrounds.Acolyte(), 
			backgrounds.Charlatan(),
			backgrounds.Criminal(),
			backgrounds.Entertainer(),
			backgrounds.FolkHero(),
			backgrounds.GuildArtisan(),
			backgrounds.Hermit(),
			backgrounds.Noble(),
			backgrounds.Outlander(),
			backgrounds.Sage(),
			backgrounds.Sailor(),
			backgrounds.Soldier(),
			backgrounds.Urchin()
]
def randsFromList(list, choices):
	oldList = list
	returnList = []
	count = 0
	while count < choices:
		a = random.choice(oldList)
		returnList.append(a)
		oldList.remove(a)
		count += 1
	return returnList
def maxKey(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]
	 
class Character:
	def __init__(self):
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
		self.abilities = {
			"Str": 0,
			"Dex": 0,
			"Con": 0,
			"Int": 0,
			"Wis": 0,
			"Cha": 0
			}
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
		for x in self.abilities:
			self.abilities[x] = random.randint(8, 16)
	
	def setClass(self):
		if random.randint(1,10) <= 2:
			self.characterClass = random.choice([classes.Barbarian(), classes.Bard(), classes.Cleric(), classes.Druid(), classes.Fighter(), classes.Monk(), classes.Paladin(), classes.Ranger(), classes.Rogue(), classes.Sorceror(), classes.Warlock(), classes.Wizard()])
			self.silly = True
		else:
			self.silly = False
			if maxKey(self.abilities) == "Str":
				self.characterClass = random.choice([classes.Barbarian(), classes.Fighter(), classes.Paladin()])
			elif maxKey(self.abilities) == "Dex":
				self.characterClass = random.choice([classes.Monk(), classes.Ranger(), classes.Rogue()])
			elif maxKey(self.abilities) == "Con":
				self.characterClass = random.choice([classes.Fighter(), classes.Barbarian(), classes.Cleric()])
			elif maxKey(self.abilities) == "Int":
				self.characterClass = random.choice([classes.Wizard(), classes.Wizard(), classes.Wizard(), classes.Bard()])
			elif maxKey(self.abilities) == "Wis":
				self.characterClass = random.choice([classes.Cleric(), self.Druid()])
			elif maxKey(self.abilities) == "Cha":
				self.characterClass = random.choice([classes.Bard(), classes.Sorceror(), classes.Warlock()])
			else:
				self.characterClass = random.choice([classes.Wizard(), classes.Fighter(), classes.Fighter(), classes.Rogue(), classes.Bard()])
		self.caster = self.characterClass.caster
		
	def setRace(self, characterClass):
		self.race = self.characterClass.classRace()
		if self.silly == True:
			self.race = random.choice(["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"])
		self.race = self.characterClass.classRace()
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
		self.hitDie = self.characterClass.hitDie
		self.hp = self.hitDie + writer.abilityBonus(self.abilities["Con"])
		
	def setAlignment(self):
		if random.randint(1, 100) <= 2:
			alignment[1] = "E"
		
		self.alignment = self.characterClass.classAlignment()
		if random.randint(1, 100) <= 2:
			alignment[1] = "E"
			
	def setSpeed(self):
	#to do: include armor in calculation
		if self.race == "Gnome" or self.race == "Halfling" or self.race == "Dwarf":
			self.speed = 25
		elif self.race == "Tiefling" or self.race == "Half-Orc" or self.race == "Half-Elf" or self.race == "Dragonborn" or self.race == "Human" or self.race == "Elf":
			self.speed = 30
		else:
			self.speed = 30
	
	def setSkills(self):
		for x in self.background.skills:
			self.skills[x] = True
		skillChoices = []
		numChoices = 2
		numChoices = self.characterClass.skillNum
		skillChoices = self.characterClass.skillChoices
		count = 0
		failSwitch = 0
		while count < numChoices and failSwitch < 10:
			chosen = random.choice(skillChoices)
			if self.skills[chosen] == False:
				self.skills[chosen] = True
				skillChoices.remove(chosen)
				count += 1
			else:
				failSwitch += 1
	
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
		if self.characterClass.name == "Barbarian":
			self.weapon1 = random.choice(martialWeapons)
			self.weapon2 = random.choice(simpleWeapons)
			self.armor = random.choice(mediumArmor)
		elif self.characterClass.name == "Bard":
			self.weapon1 = random.choice([weapons.Rapier(), weapons.Longsword(), weapons.Shortsword(), weapons.Club(), weapons.Dagger(), weapons.Greatclub(), weapons.Handaxe(), weapons.Javelin(), weapons.LightHammer(), weapons.Mace(), weapons.Quarterstaff(), weapons.Sickle(), weapons.Spear()])
			self.weapon2 = random.choice([weapons.Dagger(), weapons.Shortbow(), weapons.LightCrossbow()])
			self.armor = random.choice(lightArmor)
		elif self.characterClass.name == "Cleric":
			self.weapon1 = random.choice([weapons.Mace(), weapons.Warhammer(), weapons.Sickle(), weapons.Greatclub()])
			self.weapon2 = random.choice(simpleRangedWeapons)
			self.armor = random.choice(mediumArmor)
		elif self.characterClass.name == "Druid":
			self.weapon1 = random.choice([weapons.Club(), weapons.Dagger(), weapons.Mace(), weapons.Quarterstaff(), weapons.Scimitar(), weapons.Sickle(), weapons.Spear()])
			self.weapon2 = random.choice([weapons.Dagger(), weapons.Dart()])
			self.armor = random.choice([armors.Padded(), armors.Leather(), armors.Hide()])
		elif self.characterClass.name == "Fighter":
			self.weapon1 = random.choice(martialWeapons)
			self.weapon2 = random.choice(simpleWeapons)
			self.armor = random.choice(heavyArmor)
		elif self.characterClass.name == "Barbararian":
			self.weapon1 = random.choice(martialWeapons)
			self.weapon2 = random.choice(simpleWeapons)
			self.armor = random.choice(mediumArmor)
		elif self.characterClass.name == "Monk":
			self.weapon1 = weapons.MonkHands()
			self.weapon2 = random.choice(simpleWeapons)
			self.armor = None
		elif self.characterClass.name == "Paladin":
			self.weapon1 = random.choice(martialWeapons)
			self.weapon2 = random.choice(simpleWeapons)
			self.armor = random.choice(heavyArmor)
		elif self.characterClass.name == "Ranger":
			self.weapon1 = random.choice(simpleWeapons)
			self.weapon2 = weapons.Longbow()
			self.armor = random.choice(lightArmor)
		elif self.characterClass.name == "Rogue":
			self.weapon1 = random.choice(simpleWeapons)
			self.weapon2 = random.choice(simpleRangedWeapons)
			self.armor = random.choice(lightArmor)
		elif self.characterClass.name == "Sorceror":
			self.weapon1 = random.choice([weapons.Dagger(), weapons.Dart(), weapons.LightCrossbow()])
			self.weapon2 = None
			self.armor = None
		elif self.characterClass.name == "Warlock":
			self.weapon1 = random.choice(simpleWeapons)
			self.weapon2 = None
			self.armor = random.choice(lightArmor)
		elif self.characterClass.name == "Wizard":
			self.weapon1 = random.choice([weapons.Dagger(), weapons.Dart(), weapons.LightCrossbow()])
			self.weapon2 = None
			self.armor = None
		
		
		if self.armor != None: 
			self.ac = self.armor.ac + writer.abilityBonus(self.abilities["Dex"])
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
		self.GP = self.background.gp
		self.SP = 0
		self.CP = 0
		self.equipment = self.equipment + self.background.equipment
		
	def setSpells(self):
		self.cantrips = randsFromList(self.characterClass.cantrips, self.characterClass.cantripCount)
		self.spells1 = randsFromList(self.characterClass.spells1, self.characterClass.spells1Count)
	
	def setBackground(self):
		self.background = random.choice(backgrounds)
	
	def testEquipment(self):
		self.equipment = ["shortsword", "dagger", "buckler", "pouch", "lucky coin", "ink bottle", "flint and steel", "parchment"]
		self.GP = 3
		self.SP = 5
		self.CP = 10
		
	def testClass(self):
		self.characterClass = classes.Sorceror()
		self.caster = self.characterClass.caster