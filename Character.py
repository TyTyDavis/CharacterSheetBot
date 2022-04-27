import random
import writer
import fantasy_name_generator
import weapons
import armors
import spells
import backgrounds
import classes
import races
import tracery
from tracery.modifiers import base_english
import flavorText
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

martialWeapons = [
	weapons.Battleaxe(), 
	weapons.Flail(), 
	weapons.Glaive(), 
	weapons.Greatsword(), 
	weapons.Halberd(), 
	weapons.Lance(), 
	weapons.Longsword(), 
	weapons.Maul(), 
	weapons.Morningstar(), 
	weapons.Pike(), 
	weapons.Rapier(), 
	weapons.Scimitar(), 
	weapons.Shortsword(), 
	weapons.Trident(), 
	weapons.Warpick(), 
	weapons.Warhammer(), 
	weapons.Whip()
	]
martialRangedWeapons = [weapons.Longbow(), Blowgun(), HandCrossbow(), HeavyCrossbow(), Longbow()]
simpleWeapons = [
	weapons.Club(), 
	weapons.Dagger(), 
	weapons.Greatclub(), weapons.Handaxe(), 
	weapons.Javelin(), weapons.LightHammer(), 
	weapons.Mace(), weapons.Quarterstaff(), 
	weapons.Sickle(), 
	weapons.Spear()]
simpleRangedWeapons = [weapons.Dart(), LightCrossbow(), Shortbow()]
lightArmor = [
	armors.Padded(), 
	armors.Leather(), 
	armors.StuddedLeather() 
	]
mediumArmor = [
	armors.Hide(), 
	armors.ChainShirt(), 
	armors.ScaleMail(), 
	armors.Breastplate(), 
	armors.HalfPlate()
	]
heavyArmor = [
	armors.RingMail(), 
	armors.ChainMail(), 
	armors.Splint(), 
	armors.Plate()
	]
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
		self.level = 1
		self.abilities = None
		self.name = None
		self.gender = random.choice(["M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "N"])
		self.characterClass = "Fighter"
		self.race = "Dwarf"
		self.alignment = ["L","G"]
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
		self.proficiencies = []
		self.languages = []
		self.traits = []
		self.personality = "Blank"
		self.ideal = "blank"
		self.bond = "blank"
		self.flaw = "blank"
	def setName(self):
		firstName = None
		LastName = None
		maleNames = os.path.join(ROOT_DIR, "static", "first_name_male.txt")
		sillyMaleNames = os.path.join(ROOT_DIR, "static", "silly_name_male.txt")
		femaleNames = os.path.join(ROOT_DIR, "Static", "first_name_female.txt")
		sillyFemaleNames = os.path.join(ROOT_DIR, "static", "silly_name_female.txt")
		lastNames = os.path.join(ROOT_DIR, "static", "last_name.txt")
		sillyLastNames = os.path.join(ROOT_DIR, "static", "silly_last_names.txt")
		if self.gender == "M":
			firstName = maleNames
			flavorText.rules['they'] = "he"
			flavorText.rules['them'] = "him"
			flavorText.rules['their'] = "his"
			flavorText.rules['theirs'] = "his"
			flavorText.rules['is'] = "is"
			flavorText.rules['themselves'] = "himself"
			flavorText.rules['has'] = "has"
			flavorText.rules['s'] = "s"
		elif self.gender == "F":
			firstName = femaleNames
			flavorText.rules['they'] = "she"
			flavorText.rules['them'] = "her"
			flavorText.rules['their'] = "her"
			flavorText.rules['theirs'] = "hers"
			flavorText.rules['is'] = "is"
			flavorText.rules['themselves'] = "herself"
			flavorText.rules['has'] = "has"
			flavorText.rules['s'] = "s"
		else:
			firstName = random.choice([maleNames, femaleNames])
			flavorText.rules['they'] = "they"
			flavorText.rules['them'] = "them"
			flavorText.rules['their'] = "their"
			flavorText.rules['theirs'] = "theirs"
			flavorText.rules['is'] = "are"
			flavorText.rules['themselves'] = "themselves"
			flavorText.rules['has'] = "have"
			flavorText.rules['s'] = ""
		
		if self.silly == True:
			lastName = sillyLastNames
			if self.gender == "M":
				firstName = sillyMaleNames
			if self.gender == "F":
				firstName = sillyFemaleNames
			else:
				firstName = random.choice([sillyMaleNames, sillyFemaleNames])
				
		else: 
			lastName = lastNames
		self.name = fantasy_name_generator.name_builder(firstName, lastName)
		
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
				self.characterClass = random.choice([classes.Cleric(), classes.Druid()])
			elif maxKey(self.abilities) == "Cha":
				self.characterClass = random.choice([classes.Bard(), classes.Sorceror(), classes.Warlock()])
			else:
				self.characterClass = random.choice([classes.Wizard(), classes.Fighter(), classes.Fighter(), classes.Rogue(), classes.Bard()])
		self.caster = self.characterClass.caster
		
	def setRace(self):
		self.race = self.characterClass.classRace()
		if self.silly == True:
			self.race = random.choice(races.allRaces)
		self.race = self.characterClass.classRace()
		
	
	def setHP(self):
		self.hitDie = self.characterClass.hitDie
		self.hp = self.hitDie + writer.abilityBonus(self.abilities["Con"])
		
	def setAlignment(self):
		self.alignment = self.characterClass.classAlignment()
		if random.randint(1, 100) <= 2:
			self.alignment[1] = "E"
			
	def setSpeed(self):
	#to do: include armor in calculation
		self.speed = self.race.speed
	
	def setSkills(self):
		for x in self.background.skills:
			self.skills[x] = True
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
		if self.caster == True:
			self.cantrips = randsFromList(self.characterClass.cantrips, self.characterClass.cantripCount)
			self.spells1 = randsFromList(self.characterClass.spells1, self.characterClass.spells1Count)
	
	def setBackground(self):
		self.background = random.choice(backgrounds)
	
	def setSilly(self):
		if self.silly == False:
			pass
		else:
			sillyTrade = [
				'dude',
				'D&D character',
				'pretend wizard',
				'friend',
				'knitter',
				'bro',
				'boy'
			]
			sillyExternalTrait = [
				'mustache',
				'sweet shoes',
				'rad hairdo',
				'big pants',
				'puffy shirt',
				'butt',
				'weird chin',
				'small hands',
				'big hands',
				'beard',
				'chest',
				'many rings',
				'oversized hat'
			]
			sillyVirtue = [
				'cool as hell',
				'rowdy',
				'big',
				'thicc',
				'silly',
				
			]
			
			sillyInterest = [
				'dragon stuff',
				'dungeon stuff',
				'fantasy things',
				'wizarding',
				'fireballs',
				'owlbears',
				'tacos',
				'craft beer',
			]
			
			flavorText.rules['trade'].extend(sillyTrade)
			flavorText.rules['externalTrait'].extend(sillyExternalTrait)
			flavorText.rules['virtue'].extend(sillyVirtue)
			flavorText.rules['interest'].extend(sillyInterest)
			
	def testEquipment(self):
		self.equipment = ["shortsword", "dagger", "buckler", "pouch", "lucky coin", "ink bottle", "flint and steel", "parchment"]
		self.GP = 3
		self.SP = 5
		self.CP = 10
		
	def testClass(self):
		self.characterClass = classes.Monk()
		self.caster = self.characterClass.caster
		
	def testRace(self):
		self.race = races.HillDwarf()
		
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
			
	def setFlavor(self):
		self.personality = flavorText.personalityTrait()
		self.ideal = flavorText.ideal()
		self.bond = flavorText.bond()
		self.flaw = flavorText.flaw()