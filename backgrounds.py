import flavorText


class Background:
	def __init__(self):
		pass
	def backgroundModifiers(self, char):
		for x in self.tools:	
			char.proficiencies.append(x)
		for x in self.traits:	
			char.traits.append(x)
		flavorText.rules['flaw'].extend(self.flaw)
		flavorText.rules['bond'].extend(self.bond)
			
class Acolyte(Background):
	name = "Acolyte"
	skills = ["Insight", "Religion"]
	tools = []
	languageChoices = 2
	equipment = ["Holy symbol", "Prayer book", "5 sticks of incense", "Vestments", "common clothes"]
	gp = 15
	traits = ["Shelter of the faithful: As an acolyte, you command the respect of people who share your faith. PHB pg. 127"]
	bond = [
		'#they.capitalize# would die to recover an ancient relic of #their# faith that was lost long ago.'
		'#they.capitalize# work#s# for the good of the common people.',
		'#they.capitalize# seek#s# to preserve an ancient text that #their# enemies consider heretical.'
	]
	flaw= [
		'#they.capitalize# judge#s# others harshly, and #themselves# even more severly.',
		'#their.capitalize# piety sometimes leads #them# to blindly trust those that profess faith in #their# god.',
		'#they.capitalize# #is# inflexible in #their# thinking.'
	]

class Charlatan(Background):
	#to add: con tools of choice
	name = "Charlatan"
	skills = ["Deception", "Sleight of Hand"]
	languageChoices = 0
	tools = ["Disguise kit", "Forgery kit"]
	equipment = ["Fine clothes", "disguise kit", "weighted dice"]
	gp = 15
	traits = ["False Identity: You have created a second identity that includes documentation, acquintances, and disguises. PHB pg. 128"]
	bond = [
		'#they.capitalize# owe#s# everything to #their# mentor, who is currently rotting in jail.',
		'#they.capitalize# fleeced the wrong person, and #they# must now avoid that person for the rest of #their# life.',
		'#they.capitalize# swindled a person who didn\'t deserve it. #they.capitalize# seek#s# to atone for #their# misdeeds.'
	]
	flaw= [
		'#they.capitalize# can\'t resist a pretty face.',
		'#they.capitalize# #is# always in debt.',
		'#they.capitalize# can\'t resist swindling people who are more powerful than #them#.'
	]
	
class Criminal(Background):
	#to add: gaming set proficiency
	name = "Criminal"
	skills = ["Deception", "Stealth"]
	languageChoices = 0
	tools = ["Thieves tools"]
	equipment = ["Dark common clothes with hood", "Crowbar"]
	gp = 15
	traits = ["Criminal Contact: You have a reliable and trustworthy liason to a network of criminals. PHB pg. 129"]
	bond = [
		'#they.capitalize# #is# trying to pay off an old debt.',
		'#their.capitalize# ill-gotten gains go to support #their# family.',
		'#they.capitalize# will become the greatest thief that ever lived.'
	]
	flaw= [
		'When #they# see#s# somethign valuable, #they# can\'t think of anything but how to steal it.',
		'#they.capitalize# #has# a tell that reveals when #they# #is# lying.',
		'An innocent person is in prison for a crime #they# committed, and #they# #is# ok with that.'
	]
	
class Entertainer(Background):
	#to add: musical instrument choice, favor of admirer
	name = "Entertainer"
	skills = ["Acrobatics", "Performance"]
	languageChoices = 0
	tools = ["Disguise kit", "Lute"]
	equipment = ["Lute", "Lock of hair", "Costume"]
	gp = 15
	traits = ["By Popular Demand: You can always find a place to perform. PHB pg. 130"]
	bond = [
		'#they.capitalize# want#s# to be famous, whatever it takes.',
		'#they.capitalize# idealize#s# a hero of the old tales, and measure#s# #their# deed\'s against that person\'s.',
		'#they.capitalize# would do anything to prove #themselves# superior to #their# rival.'
	]
	flaw= [
		'#they# once satirized a noble who still wants #their# head.',
		'#they.capitalize# will do anything for fame and renown.',
		'Scandal seems to follow #them# around.'
	]
	
class FolkHero(Background):
	#to add: specific artisan tools
	name = "Folk Hero"
	skills = ["Animal Handling", "Survival"]
	languageChoices = 0
	tools = ["Artisans tools", "Land vehicles"]
	equipment = ["Artisans tools", "Shovel", "Iron pot", "Common clothes"]
	gp = 10
	traits =  ["Rustic Hospitality: You fit in among the common folks with ease. PHB pg. 131"]
	bond = [
		'#they.capitalize# worked the land, #they# love#s# the land, #they# will protect the land.',
		'#they.capitalize# protect those who cannot protect themselves.',
		'#they.capitalize# #has# a family, but #they# #has# no idea where they are.'
	]
	flaw= [
		'The tyrant who rules #their# land will stop at nothing to see #them# killed.',
		'The people who knew #them# as a child know #their# shameful secret, so #they# can never return home.',
		'Secretly, #they# believe#s# that things would be better if #they# ruled over the land.'
	]
	
class GuildArtisan(Background):
	#to add: artisans tools
	name = "Guild Artisan"
	skills = ["Insight", "Persuasion"]
	languageChoices = 1
	tools = ["Artisans tools", "Lute"]
	equipment = ["Artisans tools", "Guild letter of introduction", "Travelers clothes"]
	gp = 15
	traits =  ["Guild Membership: You can rely on certain benefits that membership provides. PHB pg. 133"]
	bond = [
		'#they.capitalize# created a great work, but have yet to find someone worthy to receive it.',
		'One day #they# will return to #their# guild to prove that #they# are the greatest artisan.',
		'#they.capitalize# pursue wealth to win someone\'s love.'
	]
	flaw= [
		'#they.capitalize# will do anything to get #their# hands on something rare or priceless.',
		'No one must ever know that #they# stole money from the guild coffers.',
		'#they.capitalize# are jealous of anyone who can outshine #their# handiwork.'
	]
	
class Hermit(Background):
	#to add: 
	name = "Hermit"
	skills = ["Medicine", "Religion"]
	languageChoices = 1
	tools = ["Herbalism kit"]
	equipment = ["Scroll case full of notes", "Winter blanket", "Common clothes", "Herbalism kit"]
	gp = 5
	traits =  ["Discovery: Your seclusion gave you access to a unique and powerful discovery. PHB pg. 134"]
	bond = [
		'#they.capitalize# entered seclusion to hide from the people that hunt #them#.',
		'#they.capitalize# entereed seclusion because #they# loved someone that did not love #them# back.',
		'their.capitalize# isolation brought #them# knowledge of an evil that only #they# can destroy.'
	]
	flaw= [
		'Now that #they# #has# returned to the world, #they# enjoy#s# its comforts a bit too much.',
		'#they.capitalize# #is# dogmatic in his thoughts and philosophy.',
		'#they.capitalize# like#s# keeping secrets and won\'t share them with anyone else.'
	]
	
class Noble(Background):
	#to add: gaming set
	name = "Noble"
	skills = ["History", "Persuasion"]
	languageChoices = 1
	tools = ["Playing cards"]
	equipment = ["Playing cards", "Fine clothes", "Signet ring", "Scroll of pedigree"]
	gp = 25
	traits = ["Position of Privilege: Due to your noble birth, people are inclined to think the best of you. PHB pg. 135"]
	bond = [
		'#they.capitalize# will face any challenge to win the approval of #their# family.',
		'#they.capitalize# want#s# the common people to see #them# as a hero.',
		'Nothing is more important to #them# than the members of #their# family.'
	]
	flaw= [
		'#they.capitalize# believe#s# that everyone is beneath #them#.',
		'#they.capitalize# hide#s# a shameful secret that could ruin #their# family forever.',
		'By #their# words and actions, #they# often bring#s# shame to #their# family.'
	]
	
class Outlander(Background):
	#to add: musical instrument, animal trophy
	name = "Outlander"
	skills = ["Athletics", "Survival"]
	languageChoices = 1
	tools = ["Flute"]
	equipment = ["Staff", "Hunting trap", "Animal trophy", "Travelers clothes"]
	gp = 10
	traits = ["Wanderer: You have and excellent memory for maps and geography. PHB pg. 136"]
	bond = [
		'An injury to the unspoiled wilderness that is #their# home is an injury to #them#.',
		'#they.capitalize# suffer#s# awful visions of impending disaster that #they# must prevent.',
		'#they.capitalize# will bring terrible wrath on the evildoers who destroyed #their# homeland.'
	]
	flaw= [
		'#they.capitalize# live#s# life to the fullest, throwing caution to the wind.',
		'Violence is #their# answer to almost any question.',
		'#they.capitalize# won\'t help those who can\'t help themselves. Its nature\'s way that the strong survive.'
	]
	
class Sage(Background):
	#to add: artisans tools
	name = "Sage"
	skills = ["Arcana", "History"]
	languageChoices = 2
	tools = ["Artisans tools", "Lute"]
	equipment = ["Black ink", "Quill", "Small knife", "Letter from deceased colleague", "Common clothes"]
	gp = 10
	traits = ["Researcher: You often know where to find information you do not know. PHB pg. 138"]
	bond = [
		'#they.capitalize# #has# an ancient text full of terrible secrets that must not fall into the wrong hands.',
		'#they.capitalize# #has# been searching #their# whole life for the answer to a certain question.',
		'#they.capitalize# sold #their# soul for knowledge.'
	]
	flaw= [
		'#they.capitalize# speak#s# without thinking, often insulting others in the process.',
		'#they.capitalize# can\'t keep #their# secrets, or anyone elses.',
		'#they.capitalize# #is# easily distracted by the promise of information.'
	]
	
class Sailor(Background):
	#to add: trinket
	name = "Sailor"
	skills = ["Athletics", "Perception"]
	languageChoices = 1
	tools = ["Navigators tools", "Water vehicles"]
	equipment = ["Belaying pin", "50 feet of silk rope", "A small stone with a holei in the middle", "Common clothes"]
	gp = 10
	traits = ["Ship\'s Passage: When you need to, you can secure free passage on a sailing ship. PHB pg. 139"]
	bond = [
		'#they.capitalize# will always remember #their# first ship.',
		'#they.capitalize# got cheated out of #their# fair share of the profits, and #they# want#s# #their# due.',
		'Pirates killed #their# captain and crew. #they.capitalize# will have #their# revenge.'
	]
	flaw= [
		'#they.capitalize# follow#s# orders, even if #they# think#s# they are wrong.',
		'#they.capitalize# will say anything to avoid extra work.',
		'Once #they# start#s# drinking, it\'s hard for #them# to stop.',
	]
	
class Soldier(Background):
	#to add: rank feature, trophy
	name = "Soldier"
	skills = ["Athletics", "Intimidation"]
	languageChoices = 1
	tools = ["Dice"]
	equipment = ["Insignia of rank", "Shard of blade from fallen enemy", "Bone dice", "Common clothes"]
	gp = 10
	traits = ["Military Rank: You have a military rank from you career as a soldier. PHB pg. 140"]
	bond = [
		'#they.capitalize# would do still lay down #their# life for the people #they# served with.',
		'#their.capitalize# honor is #their# life.',
		'#they.capitalize# fight for those who cannot fight for themselves.'
	]
	flaw= [
		'The enemy #they# faced in battle still leaves #them# quivering in fear.',
		'#they.capitalize# #has# little respect for anyone who isn\'t a proven warrior.',
		'#they.capitalize# obey#s# the law, even if the law causes misery.'
	]
	
class Urchin(Background):
	#to add: parent token
	name = "Urchin"
	skills = ["Sleight of Hand", "Stealth"]
	languageChoices = 1
	tools = ["Disguise kit", "Thieves tools"]
	equipment = ["Small knife", "Map of city", "Pet mouse", "Locket from parents", "Common clothes"]
	gp = 10
	traits = ["City Secrets: You know the secret patterns and flow to cities. PHB pg. 141"]
	bond = [
		'#they.capitalize# owe#s# #their# life to #goodPerson#, who taught #them# to survive on the streets.',
		'#they.capitalize# fought #their# way out of poverty by robbing #badPerson#, and #they# #is# wanted for it.',
		'#they.capitalize# give#s# to the poor to prevent others from going through what #they endured.'
	]
	flaw= [
		'#they.capitalize# would rather kill someone in their sleep than in a fair fight.',
		'If #they# #is# outnumbered, #they# will run away from a fight.',
		'#they.capitalize# will never fully trust anyone but #themselves#.'
	]
	