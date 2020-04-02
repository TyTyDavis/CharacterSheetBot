import writer
import Character
import random
import spells

class CharClass:
	def __init__(self):
		pass
		
class Barbarian(CharClass):
	def __init__(self):
		self.name = "Barbarian"
		self.hitDie = 12
		self.skillNum = 2
		self.skillChoices = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
		self.caster = False
	
	def classAlignment(self):
		return ["C", random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice(["Half-Orc", "Human", "Dragonborn"])
		
class Bard(CharClass):
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
	
	def classAlignment(self):
		return ["C", random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice(["Elf", "Gnome", "Half-Elf", "Halfling", "Human", "Tiefling"])
		
class Cleric(CharClass):
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
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice(["Dwarf", "Elf", "Human", "Dragonborn"])
		
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
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice(["Elf", "Half-Elf", "Human", "Tiefling"])
		
class Fighter(CharClass):
	def __init__(self):
		self.name = "Fighter"
		self.hitDie = 10
		self.skillNum = 2
		self.skillChoices = ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
		self.caster = False
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice(["Dragonborn", "Dwarf", "Half-Orc", "Human"])
		
class Monk(CharClass):
	def __init__(self):
		self.name = "Monk"
		self.hitDie = 8
		self.skillNum = 2
		self.skillChoices = ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]
		self.caster = False
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice(["Elf", "Half-Elf", "Human"])
		
class Paladin(CharClass):
	def __init__(self):
		self.name = "Paladin"
		self.hitDie = 10
		self.skillNum = 2
		self.skillChoices = ["Athletics", "Intimidation", "Insight", "Medicine", "Persuasion", "Religion"]
		self.caster = False
	
	def classAlignment(self):
		return ["L", random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice(["Dragonborn", "Dwarf", "Half-Elf", "Half-Orc", "Human"])
		
class Ranger(CharClass):
	def __init__(self):
		self.name = "Ranger"
		self.hitDie = 10
		self.skillNum = 3
		self.skillChoices = ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]
		self.caster = False
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice(["Elf", "Half-Elf", "Human"])
		
class Rogue(CharClass):
	def __init__(self):
		self.name = "Rogue"
		self.hitDie = 8
		self.skillNum = 4
		self.skillChoices = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand",  "Stealth"]
		self.caster = False
		
	def classAlignment(self):
		return ["C", random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice(["Elf", "Half-Elf", "Gnome", "Halfling", "Human"])
		
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
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice(["Elf", "Half-Elf", "Human", "Gnome", "Halfling", "Tiefling"])
		
class Warlock(CharClass):
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
	
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice(["Tiefling", "Human", "Half-Elf", "Dragonborn"])
		
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
		
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice(["Elf", "Half-Elf", "Human", "Gnome"])
		

	
	