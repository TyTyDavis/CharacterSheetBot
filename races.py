import Character
import random

class Race:
	def __init__(self):
		pass
		
	def racialModifiers(self, char):
		for key in self.abilities:
			char.abilities[key] += self.abilities[key]
		
		for x in self.proficiencies:	
			char.proficiencies.append(x)
		for x in self.traits:	
			char.traits.append(x)
		for x in self.languages:	
			char.languages.append(x)
		for x in self.skills:	
			char.skills.append[x] = True
			
		char.hp += self.hp * char.level
		
class Dwarf(Race):
	type = "Dwarf"
	name = "Dwarf"
	speed = 25
	abilities = {
		"Str": 2
	}
	skills = []
	languages = ["Common", "Dwarvish"]
	proficiencies = ["Battleaxe", "Handaxe", "Light hammer", "Warhammer", random.choice(["Smiths tools", "Brewers supplies", "Masons tools"])]
	hp = 0
	traits = [
		"Darkvision: 60 feet", 
		"Dwarven Resilience: Advantage on saving throws against poison, and resistance against poison damage",
		"Stonecunning: Considered proficient on History checks related to stone work, adding double your proficiency bonus"
		]
			
class HillDwarf(Dwarf):
	name = "Hill Dwarf"
	abilities = {
		"Str": 2,
		"Wis": 1
		
	}
	hp = 1
		
class MountainDwarf(Dwarf):
	#to do: add one to HP
	def __init__(self):
		pass
	name = "Mountain Dwarf"
	abilities = {
		"Str": 4
		
	}
	proficiencies = ["Battleaxe", "Handaxe", "Light hammer", "Warhammer", "Light armor", "Medium armor", random.choice(["Smith tool", "Brewers supplies", "Masons tools"])]

class Elf(Race):
	type = "Elf"
	name = "Elf"
	speed = 30
	abilities = {
		"Dex": 2
	}
	languages = ["Common", "Elvish"]
	proficiencies = []
	hp = 0
	skills = ["Perception"]
	traits = [
		"Darkvision: 60 feet", 
		"Fey Ancestry: Advantage on saving throws against beingt charmed, magic cant put you to sleep",
		"Trance: Elves dont need to sleep,  insrtead meditating for 4 hours",
		]
			
class HighElf(Elf):
	name = "High Elf"
	abilities = {
		"Dex": 2,
		"Int": 1
		
	}
	proficiencies = ["Longsword", "Shortsword", "Shortbow", "Longbow"]
	
class WoodElf(Elf):
	name = "Wood Elf"
	abilities = {
		"Dex": 2,
		"Wis": 1
		
	}
	proficiencies = ["Longsword", "Shortsword", "Shortbow", "Longbow"]
	speed = 35
	traits = [
		"Darkvision: 60 feet", 
		"Fey Ancestry: Advantage on saving throws against beingt charmed, magic cant put you to sleep",
		"Trance: Elves dont need to sleep,  insrtead meditating for 4 hours",
		"Mask of the Wild: Can attempt to hide even when only lightly obscured by foliage, heavy rain, snow, mist, etc."
		]
class DarkElf(Elf):
	name = "Dark Elf (Drow)"
	abilities = {
		"Dex": 2,
		"Cha": 1
		
	}
	proficiencies = ["Rapier", "Shortsword", "Hand crossbow"]
	#drow magic needs to be expanded if higher levels are added
	traits = [
		"Darkvision: 120 feet", 
		"Fey Ancestry: Advantage on saving throws against beingt charmed, magic cant put you to sleep",
		"Trance: Elves dont need to sleep,  insrtead meditating for 4 hours",
		"Sunlight Sensitivity:  Disadvantage on attack and Perception rolls when you or your target are in direct sunlight"
		"Drow Magic: You know the Dancing Lights cantrip"
		]
		
class Halfling(Race):
	type = "Halfling"
	name = "Halfling"
	speed = 25
	abilities = {
		"Dex": 2
	}
	languages = ["Common", "Halfling"]
	proficiencies = []
	hp = 0
	skills = []
	traits = [
		"Lucky: If you roll a 1 on a d20, you may reroll and must use the new roll",
		"Brave: Advantage on saving throws against being frightened",
		"Halfling Nimbleness: Can move through the space of any larger creature"
		]
			
class Lightfoot(Halfling):
	name = "Lightfoot Halfling"
	abilities = {
		"Dex": 2,
		"Con": 1
	}
	traits = [
		"Lucky: If you roll a 1 on a d20, you may reroll and must use the new roll",
		"Brave: Advantage on saving throws against being frightened",
		"Halfling Nimbleness: Can move through the space of any larger creature",
		"Naturally Stealthy: Can attempt to hide even when only pbscured by a larger creature"
		]
class Stout(Halfling):
	name = "Lightfoot Stout"
	abilities = {
		"Dex": 2,
		"Con": 1
	}
	traits = [
		"Lucky: If you roll a 1 on a d20, you may reroll and must use the new roll",
		"Brave: Advantage on saving throws against being frightened",
		"Halfling Nimbleness: Can move through the space of any larger creature",
		"Stout Resilience: Advantage on saving throws against poison, and resistance to poison damage"
		]

class Human(Race):
	#todo: Add variant human traits as subrace
	type = "Human"
	name = "Human"
	speed = 30
	abilities = {
		"Str": 0,
			"Dex": 1,
			"Con": 1,
			"Int": 1,
			"Wis": 1,
			"Cha": 1
	}
	languages = ["Common", random.choice(["Elvish", "Dwarvish", "Halfling", "Orc", "Gnomish", "Undercommon", "Draconic", "Infernal"])]
	proficiencies = []
	hp = 0
	skills = []
	traits = []

class Dragonborn(Race):
	#todo: randomize ancestry
	type = "Dragonborn"
	name = "Dragonborn"
	speed = 30
	abilities = {
		"Str": 2,
		"Cha": 1
	}
	languages = ["Common", "Draconic"]
	proficiencies = []
	hp = 0
	skills = []
	traits = [
		"Draconic Ancestry: PHB pg. 34",
		"Breath weapon: PHB pg. 34",
		"Damage Resistance: PHB pg. 34"
		]
			
class Gnome(Race):
	type = "Gnome"
	name = "Gnome"
	speed = 25
	abilities = {
		"Int": 2
	}
	languages = ["Common", "Gnomish"]
	proficiencies = []
	hp = 0
	skills = []
	traits = [
		"Darkvision: 60 feet",
		"Gnome Cunning: Advantage on all Intelligence, Wisdom and Charisma saving throws against magic",
		]

class ForestGnome(Gnome):
	name = "Forest Gnome"
	abilities = {
		"Int": 2,
		"Dex": 1
	}
	traits = [
		"Darkvision: 60 feet",
		"Gnome Cunning: Advantage on all Intelligence, Wisdom and Charisma saving throws against magic",
		"Natural Illusionist: You know the minor illusion cantrip, using Intelligence as your spellcasting ability",
		"Speak with Small Beasts: Through sounds and gestures, you can communicate with Small or smaller beasts"
		]
		
class RockGnome(Gnome):
	name = "Rock Gnome"
	abilities = {
		"Int": 2,
		"Con": 1
	}
	traits = [
		"Darkvision: 60 feet",
		"Gnome Cunning: Advantage on all Intelligence, Wisdom and Charisma saving throws against magic",
		"Artificiers Lore: Add double your proficiency bonius to History checks relating to magi items, alchemical objects or technological devices",
		"Tinker: Proficiency with tinkers tools. Can spend 1 hour and 10 gp to construct a Tiny clockwork device. PHB pg. 37"
		]
		
class HalfElf(Race):
	#todo: randomize skills and ability choices
	type = "Half-Elf"
	name = "Half-Elf"
	speed = 30
	abilities = {
		"Cha": 2,
		"Int": 1,
		"Dex": 1
	}
	languages = ["Common", "Elvish", random.choice(["Dwarvish", "Halfling", "Orc", "Gnomish", "Undercommon", "Draconic", "Infernal"])]
	proficiencies = []
	hp = 0
	skills = ["History", "Animal Handling"]
	traits = [
		"Darkvision: 60 feet",
		"Fey Ancestry: Advantage on saving throws against being charmed, and magic cant put you to sleep"
		]
		
class HalfOrc(Race):
	type = "Half-Orc"
	name = "Half-Orc"
	speed = 30
	abilities = {
		"Str": 2,
		"Con": 1
	}
	languages = ["Common", "Orc"]
	proficiencies = []
	hp = 0
	skills = ["Intimidation"]
	traits = [
		"Darkvision: 60 feet",
		"Relentless Endurance: When reduced to 0 HP, you drop to 1 HP instead",
		"Savage Attacks: When socring a critical melee attack, roll weapons damage die one additional time"
		]

class Tiefling(Race):
	type = "Tiefling"
	name = "Tiefling"
	speed = 30
	abilities = {
		"Int": 2,
		"Cha": 1
	}
	languages = ["Common", "Infernal"]
	proficiencies = []
	hp = 0
	skills = ["Intimidation"]
	traits = [
		"Darkvision: 60 feet",
		"Hellish Resistance: Resistance to fire damage",
		"Infernal Legacy: You know the Thaumaturgy cantrip"
		]
dwarfs = [Dwarf(), HillDwarf(), MountainDwarf()]
elves = [Elf(), HighElf(), WoodElf(), DarkElf()]
halflings = [Halfling(), Lightfoot(), Stout()]
humans = [Human()]
dragonborns = [Dragonborn()]
gnomes = [Gnome(), ForestGnome(), RockGnome()]
halfElves = [HalfElf()]
halfOrcs = [HalfOrc()]
tieflings = [Tiefling()]
allRaces = [Dwarf(), HillDwarf(), MountainDwarf(), Elf(), HighElf(), WoodElf(), DarkElf(), Halfling(), Lightfoot(), Stout(), Halfling(), Lightfoot(), Stout(), Human(), Dragonborn(), Gnome(), ForestGnome(), RockGnome(), HalfElf(), HalfOrc(), Tiefling()]
