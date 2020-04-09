import tracery
from tracery.modifiers import base_english

rules = {
	'they': 'they',
	'them': 'them',
	'their': 'their',
	'theirs': 'theirs',
	'themselves': 'themselves',
	'is': 'are',
	'has': 'has',
	's': 's',
	'personality': [
		'#they.capitalize# look#s# ip to #goodPerson#, and constatly refers to that person\'s deeds and example.',
		'#they.capitalize# #is# #tolerant of other faiths and the worship of other gods.',
		'#they.capitalize# #has# spent so long in the #place# that #they# have little understanding of anything outside of it.',
		'#they.capitalize# #is# a born #trade#, never passing up an opportunity to show off #their# skill.',
		'#they.capitalize# #is# always #emotion#, often — or especially — when the situation doesn\'t call for it.',
		'#they.capitalize# #is# #slow# to trust',
		'#they.capitalize# think#s# #their# #externalTrait# make#s# #them# seem #virtue#.',
		'#they.capitalize# #is# #proud# of #their# #externalTrait#.',
		'Despite #their# best efforts, #they# get#s# #emotion# very easily.',
		'#they.capitalize# can\'t get along with people who don\'t #love# #interest#.',
		'#they.capitalize# like#s# to talk at length about #interest# to anyone who will listen.',
		'#goodPerson.capitalize# was full of wisdom, and #they# #is# always eager to share that wisdom with others.',
		'Everyone around #them# thinks #they# are #virtue#.'
	],
	'tolerant': ['tolerant', 'intolerant'],
	'slow': ['slow', 'fast'],
	'proud': ['proud', 'ashamed'],
	'love': ['love', 'hate'],
	'trade': [
		'gambler',
		'drinker',
		'pick up artist',
		'orator',
	],
	'place': [
		'temple', 
		'city', 
		'university', 
		'gladiator arena', 
		'forest', 
		'woods',
		'swamp',
		'jail'
	],
	'emotion': [
		'calm',
		'angry',
		'happy',
		'sad',
		'jovial',
		'friendly',
		'cheery',
		'mad',
		'anxious',
		'impatient',
		'patient',
		'loving',
		'bored',
		'tired'
	],
	'virtue': [
		'intelligent',
		'distinguished',
		'brave',
		'courageous',
		'sexy',
		'smart',
		'funny',
		'cool',
		'hip'
	],
	'performance': [
		'joke',
		'story',
		'song',
	],
	'externalTrait': [
		'accent',
		'clothes',
		'style',
		'scowl',
		'hat',
		'tattoos',
		'smile'
	],
	'interest': [
		'books',
		'fine art',
		'music',
		'storytelling',
		'wine',
		'food',
		'nature',
		'booze'
	],
	'goodPerson': [
		'#their# mom',
		'#their# dad',
		'#their# mentor',
		'#their# best friend',
		'#their# favorite folk tale character',
		'#their# crush',
	],
		
}

def personalityTrait():
	grammar = tracery.Grammar(rules)
	grammar.add_modifiers(base_english)
	return grammar.flatten("#personality#")






#'setGender': [{'they': 'they', 'them': 'them', 'their': 'their', 'theirs': 'theirs'}, {'they': 'he', 'them': 'him', 'their': 'his', 'his': 'theirs'}, {'they': 'she', 'them': 'her', 'their': 'her', 'theirs': 'hers'}],
	