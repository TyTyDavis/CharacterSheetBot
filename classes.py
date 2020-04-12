import writer
import Character
import random
import spells
import races
import flavorText

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
				
		flavorText.rules['goodPerson'].extend(self.goodPerson)
		flavorText.rules['interest'].extend(self.interest)
		flavorText.rules['externalTrait'].extend(self.externalTrait)
		flavorText.rules['place'].extend(self.place)
		flavorText.rules['trade'].extend(self.trade)
		flavorText.rules['ideal'].extend(self.ideal)
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
		self.goodPerson = ['#their# tribal leader']
		self.interest = ['hunting']
		self.externalTrait = ['scars', 'face paint', 'animal furs', 'face tattoo']
		self.place = ['#their# ancestral territory']
		self.trade = ['barbarian', 'warrior', 'hunter', 'forager', 'arm wrestler', 'mercenary']
		self.ideal = [
			'Freedom: #they.capitalize# believe#s# no man should live in chains.',
			'Independence: No one will tie #them# down, even if it means being alone.',
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
		self.goodPerson = ['#their# favorite songwriter', '#their# favorite poet', 'the main character of #their# unfinished book']
		self.interest = ['poetry', 'obscure songs', 'fairytales', 'sonnets', 'dirty limericks', 'the theatre']
		self.externalTrait = ['costume', 'diction', 'voice']
		self.place = ['bardic college', 'performing troupe', 'theatre', 'stage', 'road']
		self.trade = ['bard', 'musician', 'storyteller', 'juggler', 'performer', 'actor', 'comedian', 'singer', 'dancer', 'poet', 'puppeteer', 'clown']
		self.ideal = [
			'Expression: What the world needs more than anything is a great #performance#.',
			'Inspiration: #their.capitalize# work seeks to make #their# audience just as #emotion# as #they# #is#.'
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
		self.goodPerson = ['#their# high preist', '#their# diety', '#their# high priestess']
		self.interest = ['prayer', 'rituals', '#their# diety']
		self.externalTrait = ['robes', 'holy symbol']
		self.place = ['church', 'monastery']
		self.trade = ['preacher', 'healer', 'cleric']
		self.ideal = [
			'Exaltation: #they.capitalize# seek#s# to spread the message of #their# diety across the land.',
			'Faith: #they.capitalize# want nothing more than to earn the grace of #their# god.'
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
		
		self.goodPerson = ['#their# animal friend']
		self.interest = ['nature', 'animals', 'frolicking']
		self.externalTrait = ['face paint']
		self.place = ['wilderness', 'jungle', 'enchanted woods', 'mysterious forest']
		self.trade = ['tracker', 'forager', 'survivalist', 'climber', 'druid']
		self.ideal = [
			'Conservation: #they.capitalize# will fight to protect the pristine #place# they call home.',
			'Beauty: #they.capitalize# live to see everything the natural world has to offer.'
		]
		
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
		self.goodPerson = ['#their# commander', 'an old war buddy']
		self.interest = ['swords', 'battles']
		self.externalTrait = ['scars', 'war tattoo', 'awesome armor']
		self.place = ['battlefield', 'barracks', 'gladiator arena']
		self.trade = ['wrestler', 'arm wrestler', 'warrior', 'fighter', 'soldier', 'mercenary', 'dragon slayer', 'monster hunter']
		self.ideal = [
			'Protector: #they.capitalize# will fight to protect the #place# #they# call#s# home.',
			'Conquest: #they.capitalize# fight#s# to bring glory to the realm.'
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
		self.goodPerson = ['#their# sensei']
		self.interest = ['meditating', 'proverbs']
		self.externalTrait = ['robes']
		self.place = ['monastery', 'mountains']
		self.trade = ['teacher', 'meditator', 'monk', 'martial artist', 'warrior']
		self.ideal = [
			'Enlightenment: #they.capitalize# seek the one true path through the study of #interest#.',
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
		self.goodPerson = ['#their# priest', '#their# diety']
		self.interest = ['scripture']
		self.externalTrait = ['armor']
		self.place = ['castle', 'keep', 'battlefield']
		self.trade = ['leader', 'knight', 'warrior', 'paladin']
		self.ideal = [
			'Protector: #they.capitalize# will fight to protect the #place# #they# call#s# home.',
			'Conquest: #they.capitalize# fight#s# to bring glory to #their# diety.'
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
		self.goodPerson = ['#their# animal friend', 'an old hermit', 'a mountain man']
		self.interest = ['hunting', 'archery', 'camping', 'climbing']
		self.externalTrait = ['furs', 'long hair']
		self.place = ['wilderness', 'tundra', 'desert', 'mountains', 'enchanted forest', 'campsite']
		self.trade = ['ranger', 'warrior', 'survivalist', 'hunter', 'tracker', 'marksman', 'climber', 'swimmer']
		self.ideal = [
			'Conservation: #they.capitalize# will fight to protect the pristine #place# they call home.',
			'Beauty: #they.capitalize# live to see everything the natural world has to offer.'
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
		self.goodPerson = ['an infamous thief', '#their# gang leader']
		self.interest = ['con artistry', 'breaking the rules', 'breaking the law']
		self.externalTrait = ['hood', 'mask', 'cloak', 'tattoo']
		self.place = ['jail', 'streets', 'back alleys', 'high seas']
		self.trade = ['pickpocket', 'liar', 'actor', 'climber', 'lockpicker', 'thief', 'criminal', 'rogue', 'con artist']
		self.ideal = [
			'Freedom: #they.capitalize# believe#s# no man should live in chains.',
			'Aptitude: #they.capitalize# seek to become the best #trade# the world has ever known.',
			'Infamy: #they.capitalize# believe#s# the only thing better than attracting fans is attracting enemies.'
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
		self.goodPerson = ['#their# arcane mentor']
		self.interest = ['ancient magic', 'long forgotten secrets', 'the multiverse']
		self.externalTrait = ['sense of mystery']
		self.place = ['arcanum']
		self.trade = ['alchemist', 'magician', 'mage', 'sorceror', 'conjurer', 'magic-user', 'evoker']
		self.ideal = [
			'Knowledge: #they.capitalize# are always hungry to learn more about #interest#.',
			'Power: #they.capitalize# seek the arcane means to learn the secrets of #interest#.',
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
		self.goodPerson = ['#their# coven leader']
		self.interest = ['dark secrets', 'ancient terrors', 'forbidden tomes']
		self.externalTrait = ['raven black hair', 'piercing eyes']
		self.place = ['lair', 'Underdark', 'unspeakable place']
		self.trade = ['murderer', 'warlock', 'mage', 'magic-user']
		self.ideal = [
			'Knowledge: #they.capitalize# are always hungry to learn more about #interest#.',
			'Power: #they.capitalize# seek the arcane means to learn the secrets of #interest#.',
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
		self.goodPerson = ['#their# professor', '#their# top student']
		self.interest = ['old dusty books', 'theoretical magic', 'the cosmos']
		self.externalTrait = ['robes', 'spellbook']
		self.place = ['library', 'university', 'tower', 'arcanum']
		self.trade = ['achemist', 'writer', 'philosopher', 'researcher', 'mage', 'magic-user', 'wizard', 'conjurer', 'evoker']
		self.ideal = [
			'Knowledge: #they.capitalize# are always hungry to learn more about #interest#.',
			'Destiny: #they.capitalize# are drawn to the study of #interest# by an unseen force.',
		]
	def classAlignment(self):
		return [random.choice(["C", "L", "N"]), random.choice(["G", "N"])]
	
	def classRace(self):
		return random.choice([random.choice(races.elves), races.HalfElf(), races.Human(), random.choice(races.gnomes)])
		

	
	