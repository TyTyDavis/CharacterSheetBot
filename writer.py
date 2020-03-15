from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def abilityBonus(score):
	if score > 5 and score < 8:
		return -2
	elif score < 10:
		return -1
	elif score < 12:
		return 0
	elif score < 14:
		return 1
	elif score < 16:
		return 2
	elif score < 18:
		return 3
	elif score < 20:
		return 4
	elif score < 22:
		return 5
			
def writeAbilityBonus(score):
	if score > 5 and score < 8:
		return "-2"
	elif score < 10:
		return "-1"
	elif score < 12:
		return "+0"
	elif score < 14:
		return "+1"
	elif score < 16:
		return "+2"
	elif score < 18:
		return "+3"
	elif score < 20:
		return "+4"
	elif score < 22:
		return "+5"
def writeName(image, name):
#Write character name on sheet
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",50)
	draw.text((200, 270), name,(0,0,0), font=font)
	
def writeAbilities(image, abilities):
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",60)
	draw.text((200, 660), str(abilities[0]),(0,0,0), font=font)
	draw.text((200, 960), str(abilities[1]),(0,0,0), font=font)
	draw.text((200, 1260), str(abilities[2]),(0,0,0), font=font)
	draw.text((200, 1560), str(abilities[3]),(0,0,0), font=font)
	draw.text((200, 1860), str(abilities[4]),(0,0,0), font=font)
	draw.text((200, 2160), str(abilities[5]),(0,0,0), font=font)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
	draw.text((215, 785), writeAbilityBonus(abilities[0]),(0,0,0), font=font)
	draw.text((215, 1085), writeAbilityBonus(abilities[1]),(0,0,0), font=font)
	draw.text((215, 1380), writeAbilityBonus(abilities[2]),(0,0,0), font=font)
	draw.text((215, 1680), writeAbilityBonus(abilities[3]),(0,0,0), font=font)
	draw.text((215, 1980), writeAbilityBonus(abilities[4]),(0,0,0), font=font)
	draw.text((215, 2280), writeAbilityBonus(abilities[5]),(0,0,0), font=font)
	
def writeClass(image, characterClass):
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",60)
	draw.text((1130, 200), characterClass,(0,0,0), font=font)
	
def writeRace(image, race):
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",60)
	draw.text((1130, 310), race,(0,0,0), font=font)
	
def writeHP(image, hp):
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
	draw.text((1220, 820), str(hp),(0,0,0), font=font)

def writeAlignment(image, alignment):
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",60)
	draw.text((1600, 310), alignment[0] + alignment[1],(0,0,0), font=font)

def writeInitiative(image, dex):
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",60)
	draw.text((1210, 610), writeAbilityBonus(dex),(0,0,0), font=font)
	
def writeProficiency(image, proficiency):
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",60)
	draw.text((410, 700), "+" + str(proficiency),(0,0,0), font=font)

def writeSpeed(image, speed):
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",60)
	draw.text((1470, 610), str(speed),(0,0,0), font=font)

def writeHitDie(image, hitDie):
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",75)
	draw.text((1000, 1390), "1d" + str(hitDie),(0,0,0), font=font)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
	draw.text((1030, 1320), "1",(0,0,0), font=font)

def writeSavingThrows(image, character):
	img = image
	draw = ImageDraw.Draw(img)
	throws = {
		"Strength": False,
		"Dexterity": False,
		"Constitution": False,
		"Intelligence": False,
		"Wisdom": False,
		"Charisma": False
	}
	
	if character.characterClass == "Barbarian" or character.characterClass == "Fighter" or character.characterClass == "Monk" or character.characterClass == "Ranger":
		throws["Strength"] = True
	if character.characterClass == "Bard" or character.characterClass == "Monk" or character.characterClass == "Ranger" or character.characterClass == "Rogue":
		throws["Dexterity"] = True
	if character.characterClass == "Barbarian" or character.characterClass == "Fighter" or character.characterClass == "Sorceror":
		throws["Constitution"] = True
	if character.characterClass == "Druid" or character.characterClass == "Rogue" or character.characterClass == "Wizard":
		throws["Intelligence"] = True
	if character.characterClass == "Cleric" or character.characterClass == "Druid" or character.characterClass == "Paladin" or character.characterClass == "Warlock" or character.characterClass == "Wizard":
		throws["Wisdom"] = True
	if character.characterClass == "Bard" or character.characterClass == "Cleric" or character.characterClass == "Paladin" or character.characterClass == "Sorceror" or character.characterClass == "Warlock":
		throws["Charisma"] = True
	
	if throws["Strength"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 860), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 850), "+" + str(abilityBonus(character.abilities[0]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 850), writeAbilityBonus(character.abilities[0]),(0,0,0), font=font)
	if throws["Dexterity"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 920), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 910), "+" + str(abilityBonus(character.abilities[1]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 900), writeAbilityBonus(character.abilities[1]),(0,0,0), font=font)
	if throws["Constitution"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 970), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 960), "+" + str(abilityBonus(character.abilities[2]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 960), writeAbilityBonus(character.abilities[2]),(0,0,0), font=font)
	if throws["Intelligence"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1030), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 1020), "+" + str(abilityBonus(character.abilities[3]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 1020), writeAbilityBonus(character.abilities[3]),(0,0,0), font=font)
	if throws["Wisdom"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1085), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 1075), "+" + str(abilityBonus(character.abilities[4]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 1075), writeAbilityBonus(character.abilities[4]),(0,0,0), font=font)
	if throws["Charisma"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1140), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 1130), "+" + str(abilityBonus(character.abilities[5]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 1130), writeAbilityBonus(character.abilities[5]),(0,0,0), font=font)