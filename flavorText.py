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
		'#they.capitalize# look#s# up to #goodPerson#, and constatly refers to that person\'s deeds and example.',
		'#they.capitalize# #is# #tolerant# of other faiths and the worship of other gods.',
		'#they.capitalize# #has# spent so long in the #place# that #they# can\'t understand anything outside of it.',
		'#they.capitalize# #is# a born #trade#, never passing up an opportunity to show off #their# skill.',
		'#they.capitalize# #is# always #emotion#, often — or especially — when the situation doesn\'t call for it.',
		'#they.capitalize# #is# #slow# to trust',
		'#they.capitalize# think#s# #their# #externalTrait# makes #them# seem #virtue#.',
		'#they.capitalize# #is# #proud# of #their# #externalTrait#.',
		'Despite #their# best efforts, #they# get#s# #emotion# very easily.',
		'#they.capitalize# can\'t get along with people who don\'t #love# #interest#.',
		'#they.capitalize# like#s# to talk at length about #interest# to anyone who will listen.',
		'#goodPerson.capitalize# was full of wisdom, and #they# #is# always eager to share that wisdom with others.',
		'Everyone around #them# thinks #they# #is# #virtue#.'
	],
	'ideal': [
		'Loyalty: #they.capitalize# trust#s# that #goodPerson# will guide #them# towards the right actions.',
		'Aspiration: #they.capitalize# seek#s# to prove #themselves# to #goodPerson# through #their# deeds.',
		'Responsibilty: #they.capitalize# will defend the #place#, no matter the cost.',
		'Aspiration: #they.capitalize# will be the best #trade# the world has ever known.',
		'People: #they.capitalize# believe#s# in people, especially #goodPerson#, over things or ideas.',
		'Beauty: #they.capitalize# will share #their# passion for #interest# with the whole world.',
		
	],
	'bond':[
		'The death of #goodPerson# had a huge impact on how #they# form#s# connections with others.',
		'The #place# #they# grew up is the most important place in the whole world.',
		'Everything #they# know#s# about being a #trade#, #they# learned from #goodPerson#.',
		'Everything #they# #is# doing is to try to earn the love of #goodPerson#.',
		'One day, #they# will return to #their# home #place# to show everyone how great of a #trade# #they# #is#.',
		'#they.capitalize# will get revenge on #badPerson# that wronged #them#.',
		'No one is mor important than the other members of #their# #group#.',
		'#they.capitalize# still can\'t seem to trust the other members of #their# #group#.',
		'#they.capitalize# are chasing #badPerson# that killed #goodPerson#.',
		'#they.capitalize# find#s# it hard to care again after losing #goodPerson#.',
		'#they.capitalize# will face any challenge to win the approval of the #group#.',
		'#they.capitalize# will use #their# #group# for as long as it helps #themselves#.',
		'#they.capitalize# will take advantage of #goodPerson# for as long as #they# can.',
		'Even though they may be far away, #they# will always remain loyal to the #group#.',
		'Even though they are far away, #goodPerson# will always be close in #their# heart.',
		'#they.capitalize# work#s# to preserve the dying traditions of the #group#.',
		'#they.capitalize# #love##s# #goodPerson#.',
		'#they.capitalize# #love##s# #badPerson#.',
		'#they.capitalize# #is# so #proud# of #goodPerson#.',
		'People come and go, but #their# #place# will always be there.',
		'#they.capitalize# will always remember the #place#.',
		'#they.capitalize# will get #their# revenge on #badPerson#s. All of them.',
		'The #place# is #their# home, and #they# will fight to defend it.',
		'#they.capitalize# owe#s# a life debt to #goodPerson#.',
	],
	'flaw': [
			'#they.capitalize# put#s# too much trust in the people in charge of the #group#.',
			'#they.capitalize# can often be too #virtue# for #their# own good.',
			'#they.capitalize# #is# obsessed with #interest# to the detriment of everything else.',
			'#they.capitalize# can\'t resist a #virtue# person.',
			'#they.capitalize# spend#s# all of #their# coin on #interest#.',
			
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
		'forest', 
		'woods',
		'swamp',
		'town',
		'village',
		'lake',
		'port',
		'island',
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
		'poem',
		'drama',
		'epic poem',
	],
	'externalTrait': [
		'accent',
		'clothing',
		'style',
		'scowl',
		'hat',
		'tattoo',
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
		'#their# brother',
		'#their# sister',
		'#their# son',
		'#their# daughter',
	],
	'badPerson': [
		'the assassin',
		'the soldier',
		'the wizard',
		'#their# brother',
		'#their# sister',
		'the monster',
		'the dragon',
		'the thief',
		'the warlock',
		'the troll',
		'the ogre',
		'the king',
		
	],
	'group': [
		'guild',
		'adventuring party',
		'army',
		'gang',
		'troupe',
		'tribe',
		'family',
		'rag tag crew',
	],
}

def personalityTrait():
	grammar = tracery.Grammar(rules)
	grammar.add_modifiers(base_english)
	return grammar.flatten("#personality#")
	
def ideal():
	grammar = tracery.Grammar(rules)
	grammar.add_modifiers(base_english)
	return grammar.flatten("#ideal#")
	
def bond():
	grammar = tracery.Grammar(rules)
	grammar.add_modifiers(base_english)
	return grammar.flatten("#bond#")
	
def flaw():
	grammar = tracery.Grammar(rules)
	grammar.add_modifiers(base_english)
	return grammar.flatten("#flaw#")






#'setGender': [{'they': 'they', 'them': 'them', 'their': 'their', 'theirs': 'theirs'}, {'they': 'he', 'them': 'him', 'their': 'his', 'his': 'theirs'}, {'they': 'she', 'them': 'her', 'their': 'her', 'theirs': 'hers'}],
	