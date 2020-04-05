import writer
import Character
import random
import spells
import races

class CharClass:
	def __init__(self):
		pass
		
	def classModifiers(self, char):
		
		for x in self.proficiencies:	
			char.proficiencies.append(x)
		for x in self.traits:	
			char.traits.append(x)
		if self.name == "Druid":
			for x in self.languages:	
				char.languages.append(x)
		
class Barbarian(CharClass):
	def __init__(self):
		self.name = "Barbarian"
		self.hitDie = 12
		self.skillNum = 2
		self.skillChoices = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
		self.caster = False
		self.proficiencies = ["Light armor", "Medium armor", "Shield", "Simple weapons", "Martial weapons"]
		self.traits = [
			"Rage: PHB pg. 48",
			"Unarmored Defense: While not wearing armor, AC is 10 + Dexterity modifier + Constitution modifier"
		]
	def classAlignment(self):
		return ["C", random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([races.HalfOrc(), races.Human(), races.Dragonborn()])
		
class Bard(CharClass):
	#todo: randomize musical instrument
	def __init__(self):
		self.name = "Bard"
		self.hitDie = 8
		self.skillNum = 3
		self.skillChoices = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
		self.caster = True
		self.cantrips = spells.bardCantrips
		self.spells1 = spells.bardSpells1
		self.cantripCount = 2
		self.spells1Count = 4
		self.proficiencies = ["Light armor", "Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords", "Lute"]
		self.traits = [
			"Bardic Inspiration: PHB pg. 53"
		]
		
	def classAlignment(self):
		return ["C", random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([random.choice(races.elves), random.choice(races.gnomes), races.HalfElf(), random.choice(races.halflings), races.Human(), races.Tiefling()])
		
class Cleric(CharClass):
	#todo: add domain
	def __init__(self):
		self.name = "Cleric"
		self.hitDie = 8
		self.skillNum = 2
		self.skillChoices = ["History", "Insight", "Medicine", "Persuasion", "Religion"]
		self.caster = True
		self.cantrips = spells.clericCantrips
		self.spells1 = spells.clericSpells1
		self.cantripCount = 3
		self.spells1Count = 2
		self.proficiencies = ["Light armor", "Medium armor", "Shield", "Simple weapons"]
		self.traits = [
			"Divine Domain: PHB pg. 58"
		]
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([random.choice(races.dwarfs), random.choice(races.elves), races.Human(), races.Dragonborn()])
		
class Druid(CharClass):
	def __init__(self):
		self.name = "Druid"
		self.hitDie = 8
		self.skillNum = 2
		self.skillChoices = ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]
		self.caster = True
		self.cantrips = spells.druidCantrips
		self.spells1 = spells.druidSpells1
		self.cantripCount = 2
		self.spells1Count = 2
		self.proficiencies = ["Light armor", "Medium armor", "Shield", "Clubs", "Daggers", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears", "Herbalism kit"]
		self.traits = []
		self.languages = ["Druidic"]
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([random.choice(races.elves), races.HalfElf(), races.Human(), races.Tiefling()])
		
class Fighter(CharClass):
	def __init__(self):
		self.name = "Fighter"
		self.hitDie = 10
		self.skillNum = 2
		self.skillChoices = ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
		self.caster = False
		self.proficiencies = ["All armor", "Shields", "Simple weapons", "Martial weapons"]
		self.traits = [
			random.choice([
				"Archery: +2 attack bonus with ranged weapons", "Defense: Gain +1 bonus to AC while wearing armor","Dueling: While wielding a melee weapon in one hand and no other weapons, gain +2 to damge rolls","Great Weapon Fighting: When you roll a 1 or 2 on damage die while wielding a two-handed melee weapon, you may reroll and you must use the new roll","Protection: When a creature you see attacks a targer within 5 feet of you, use reaction to impose disadavantage. Must be wielding shield","Two weapon fighting: Add ability modifier to second attack when wielding two weapons"]),
			"Second Wind: Once per day, regain 1d10 + level HP"
		]
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([races.Dragonborn(), random.choice(races.dwarfs), races.HalfOrc(), races.Human()])
		
class Monk(CharClass):
#todo: randomize tools or instrument
	def __init__(self):
		self.name = "Monk"
		self.hitDie = 8
		self.skillNum = 2
		self.skillChoices = ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]
		self.caster = False
		self.proficiencies = ["Simple weapons", "Shortswords", "Artisans tools or musical instrument"]
		self.traits = [
			"Unarmored Defense: While not wearing armor, AC is 10 + Dexterity modifier + Wisdom modifier",
			"Martial arts: PHB pg. 78"
		]
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([random.choice(races.elves), races.HalfElf(), races.Human()])
		
class Paladin(CharClass):
	def __init__(self):
		self.name = "Paladin"
		self.hitDie = 10
		self.skillNum = 2
		self.skillChoices = ["Athletics", "Intimidation", "Insight", "Medicine", "Persuasion", "Religion"]
		self.caster = False
		self.proficiencies = ["All armor", "Shields", "Simple weapons", "Martial weapons"]
		self.traits = [
			"Divine Sense: PHB pg. 84",
			"Lay on Hands: PHB pg. 84"
		]
		
	def classAlignment(self):
		return ["L", random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([races.Dragonborn(), random.choice(races.dwarfs), races.HalfElf(), races.HalfOrc(), races.Human()])
		
class Ranger(CharClass):
	def __init__(self):
		self.name = "Ranger"
		self.hitDie = 10
		self.skillNum = 3
		self.skillChoices = ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]
		self.caster = False
		self.proficiencies = ["Light armor", "Medium armor", "Shields", "Simple weapons", "Martial weapons"]
		self.traits = [
			"Favored Enemy: " + random.choice(["Aberrations", " Beasts", "Celestials", "Constructs", "Dragons", "Elementals", "Fey", "Fiends", "Giants", "Monstrosities", "Oozes", "Plants", "Undead"]) + ", PHB pg. 91",
			"Natural Explorer: PHB pg. 91"
		]
	
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([random.choice(races.elves), races.HalfElf(), races.Human()])
		
class Rogue(CharClass):
	#todo: randomise expertise
	def __init__(self):
		self.name = "Rogue"
		self.hitDie = 8
		self.skillNum = 4
		self.skillChoices = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand",  "Stealth"]
		self.caster = False
		self.proficiencies = ["Light armor", "Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Longswords", "Thieves tools"]
		self.traits = [
			"Expertise: PHB pg. 96",
			"Sneak Attack: Extra 1d6 damage if you have advantage on attack, using finesse or ranged weapon",
			"Thieves Cant: Communicatge with other thieves using secret dialect, jargon and code"
		]
		
	def classAlignment(self):
		return ["C", random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([random.choice(races.elves), races.HalfElf(), random.choice(races.gnomes), random.choice(races.halflings), races.Human()])
		
class Sorceror(CharClass):
	def __init__(self):
		self.name = "Sorceror"
		self.hitDie = 6
		self.skillNum = 2
		self.skillChoices = ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]
		self.caster = True
		self.cantrips = spells.sorcerorCantrips
		self.spells1 = spells.sorcerorSpells1
		self.cantripCount = 4
		self.spells1Count = 2
		self.proficiencies = ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"]
		self.traits = [
			random.choice(["Draconic Bloodline: PHB pg. 102", "Wild Magic: PHB pg. 103"])
		]
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([random.choice(races.elves), races.HalfElf(), races.Human(), random.choice(races.gnomes), random.choice(races.halflings), races.Tiefling()])
		
class Warlock(CharClass):
	#todo: expand on Pact Magic
	def __init__(self):
		self.name = "Warlock"
		self.hitDie = 8
		self.skillNum = 2
		self.skillChoices = ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]
		self.caster = True
		self.cantrips = spells.warlockCantrips
		self.spells1 = spells.warlockSpells1
		self.cantripCount = 2
		self.spells1Count = 2
		self.proficiencies = ["Light armor", "Simple weapons"]
		self.traits = [
				"Otherwordly Pact: " + random.choice(["The Archfey", "The Fiend", "The Great Old One"]) + ", PHB pg. 108",
				"Pact Magic: PHB pg. 107"
		]
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([races.Tiefling(), races.Human(), races.HalfElf(), races.Dragonborn()])
		
class Wizard(CharClass):
	def __init__(self):
		self.name = "Wizard"
		self.hitDie = 6
		self.skillNum = 2
		self.skillChoices = ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
		self.caster = True
		self.cantrips = spells.wizardCantrips
		self.spells1 = spells.wizardSpells1
		self.cantripCount = 3
		self.spells1Count = 6
		self.proficiencies = ["Daggers", "Darts", "Slings", "Quarterstaff", "Light crossbows"]
		self.traits = [
			"Arcane Recovery: PHB pg. 115"
		]
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([random.choice(races.elves), races.HalfElf(), races.Human(), random.choice(races.gnomes)])
		

	
	