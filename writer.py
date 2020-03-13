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

	
	