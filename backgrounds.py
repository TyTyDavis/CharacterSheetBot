class Background:
	def __init__(self):
		pass
	def backgroundModifiers(self, char):
		for x in self.tools:	
			char.proficiencies.append(x)
			
class Acolyte(Background):
	name = "Acolyte"
	skills = ["Insight", "Religion"]
	tools = []
	languageChoices = 2
	equipment = ["Holy symbol", "Prayer book", "5 sticks of incense", "Vestments", "common clothes"]
	gp = 15

class Charlatan(Background):
	#to add: con tools of choice
	name = "Charlatan"
	skills = ["Deception", "Sleight of Hand"]
	languageChoices = 0
	tools = ["Disguise kit", "Forgery kit"]
	equipment = ["Fine clothes", "disguise kit", "weighted dice"]
	gp = 15
	
class Criminal(Background):
	#to add: gaming set proficiency
	name = "Criminal"
	skills = ["Deception", "Stealth"]
	languageChoices = 0
	tools = ["Thieves tools"]
	equipment = ["Dark common clothes with hood", "Crowbar"]
	gp = 15
	
class Entertainer(Background):
	#to add: musical instrument choice, favor of admirer
	name = "Entertainer"
	skills = ["Acrobatics", "Performance"]
	languageChoices = 0
	tools = ["Disguise kit", "Lute"]
	equipment = ["Lute", "Lock of hair", "Costume"]
	gp = 15

class FolkHero(Background):
	#to add: specific artisan tools
	name = "Folk Hero"
	skills = ["Animal Handling", "Survival"]
	languageChoices = 0
	tools = ["Artisans tools", "Land vehicles"]
	equipment = ["Artisans tools", "Shovel", "Iron pot", "Common clothes"]
	gp = 10
	
class GuildArtisan(Background):
	#to add: artisans tools
	name = "Guild Artisan"
	skills = ["Insight", "Persuasion"]
	languageChoices = 1
	tools = ["Artisans tools", "Lute"]
	equipment = ["Artisans tools", "Guild letter of introduction", "Travelers clothes"]
	gp = 15
	
class Hermit(Background):
	#to add: 
	name = "Hermit"
	skills = ["Medicine", "Religion"]
	languageChoices = 1
	tools = ["Herbalism kit"]
	equipment = ["Scroll case full of notes", "Winter blanket", "Common clothes", "Herbalism kit"]
	gp = 5

class Noble(Background):
	#to add: gaming set
	name = "Noble"
	skills = ["History", "Persuasion"]
	languageChoices = 1
	tools = ["Playing cards"]
	equipment = ["Playing cards", "Fine clothes", "Signet ring", "Scroll of pedigree"]
	gp = 25
	
class Outlander(Background):
	#to add: musical instrument, animal trophy
	name = "Outlander"
	skills = ["Athletics", "Survival"]
	languageChoices = 1
	tools = ["Flute"]
	equipment = ["Staff", "Hunting trap", "Animal trophy", "Travelers clothes"]
	gp = 10
	
class Sage(Background):
	#to add: artisans tools
	name = "Sage"
	skills = ["Arcana", "History"]
	languageChoices = 2
	tools = ["Artisans tools", "Lute"]
	equipment = ["Black ink", "Quill", "Small knife", "Letter from deceased colleague", "Common clothes"]
	gp = 10
	
class Sailor(Background):
	#to add: trinket
	name = "Sailor"
	skills = ["Athletics", "Perception"]
	languageChoices = 1
	tools = ["Navigators tools", "Water vehicles"]
	equipment = ["Belaying pin", "50 feet of silk rope", "A small stone with a holei in the middle", "Common clothes"]
	gp = 10
	
class Soldier(Background):
	#to add: rank feature, trophy
	name = "Soldier"
	skills = ["Athletics", "Intimidation"]
	languageChoices = 1
	tools = ["Dice"]
	equipment = ["Insignia of rank", "Shard of blade from fallen enemy", "Bone dice", "Common clothes"]
	gp = 10
	
class Urchin(Background):
	#to add: parent token
	name = "Urchin"
	skills = ["Sleight of Hand", "Stealth"]
	languageChoices = 1
	tools = ["Disguise kit", "Thieves tools"]
	equipment = ["Small knife", "Map of city", "Pet mouse", "Locket from parents", "Common clothes"]
	gp = 10
	