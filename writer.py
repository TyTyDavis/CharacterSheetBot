from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap

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
	draw.text((200, 660), str(abilities["Str"]),(0,0,0), font=font)
	draw.text((200, 960), str(abilities["Dex"]),(0,0,0), font=font)
	draw.text((200, 1260), str(abilities["Con"]),(0,0,0), font=font)
	draw.text((200, 1560), str(abilities["Int"]),(0,0,0), font=font)
	draw.text((200, 1860), str(abilities["Wis"]),(0,0,0), font=font)
	draw.text((200, 2160), str(abilities["Cha"]),(0,0,0), font=font)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
	draw.text((215, 785), writeAbilityBonus(abilities["Str"]),(0,0,0), font=font)
	draw.text((215, 1085), writeAbilityBonus(abilities["Dex"]),(0,0,0), font=font)
	draw.text((215, 1380), writeAbilityBonus(abilities["Con"]),(0,0,0), font=font)
	draw.text((215, 1680), writeAbilityBonus(abilities["Int"]),(0,0,0), font=font)
	draw.text((215, 1980), writeAbilityBonus(abilities["Wis"]),(0,0,0), font=font)
	draw.text((215, 2280), writeAbilityBonus(abilities["Cha"]),(0,0,0), font=font)
	
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
		draw.text((475, 850), "+" + str(abilityBonus(character.abilities["Str"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 850), writeAbilityBonus(character.abilities["Str"]),(0,0,0), font=font)
	if throws["Dexterity"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 920), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 910), "+" + str(abilityBonus(character.abilities["Dex"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 900), writeAbilityBonus(character.abilities["Dex"]),(0,0,0), font=font)
	if throws["Constitution"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 970), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 960), "+" + str(abilityBonus(character.abilities["Con"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 960), writeAbilityBonus(character.abilities["Con"]),(0,0,0), font=font)
	if throws["Intelligence"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1030), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 1020), "+" + str(abilityBonus(character.abilities["Int"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 1020), writeAbilityBonus(character.abilities["Int"]),(0,0,0), font=font)
	if throws["Wisdom"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1085), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 1075), "+" + str(abilityBonus(character.abilities["Wis"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 1075), writeAbilityBonus(character.abilities["Wis"]),(0,0,0), font=font)
	if throws["Charisma"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1140), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 1130), "+" + str(abilityBonus(character.abilities["Cha"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((475, 1130), writeAbilityBonus(character.abilities["Cha"]),(0,0,0), font=font)
		
def writeSkills(image, character):
	img = image
	draw = ImageDraw.Draw(img)
	if character.skills["Acrobatics"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1340), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1330), "+" + str(abilityBonus(character.abilities["Dex"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1330), writeAbilityBonus(character.abilities["Dex"]),(0,0,0), font=font)
	if character.skills["Animal Handling"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1395), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1385), "+" + str(abilityBonus(character.abilities["Wis"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1385), writeAbilityBonus(character.abilities["Wis"]),(0,0,0), font=font)
	if character.skills["Arcana"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1455), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1440), "+" + str(abilityBonus(character.abilities["Int"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1440), writeAbilityBonus(character.abilities["Int"]),(0,0,0), font=font)
	if character.skills["Athletics"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1510), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1500), "+" + str(abilityBonus(character.abilities["Str"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1500), writeAbilityBonus(character.abilities["Str"]),(0,0,0), font=font)
	if character.skills["Deception"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1565), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1555), "+" + str(abilityBonus(character.abilities["Cha"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1555), writeAbilityBonus(character.abilities["Cha"]),(0,0,0), font=font)
	if character.skills["History"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1625), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1610), "+" + str(abilityBonus(character.abilities["Int"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1610), writeAbilityBonus(character.abilities["Int"]),(0,0,0), font=font)
	if character.skills["Insight"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1680), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1665), "+" + str(abilityBonus(character.abilities["Wis"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1665), writeAbilityBonus(character.abilities["Wis"]),(0,0,0), font=font)
	if character.skills["Intimidation"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1735), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1725), "+" + str(abilityBonus(character.abilities["Cha"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1725), writeAbilityBonus(character.abilities["Cha"]),(0,0,0), font=font)
	if character.skills["Investigation"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1790), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1780), "+" + str(abilityBonus(character.abilities["Int"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1780), writeAbilityBonus(character.abilities["Int"]),(0,0,0), font=font)
	if character.skills["Medicine"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1845), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1835), "+" + str(abilityBonus(character.abilities["Wis"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1835), writeAbilityBonus(character.abilities["Wis"]),(0,0,0), font=font)
	if character.skills["Nature"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1905), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1895), "+" + str(abilityBonus(character.abilities["Int"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1895), writeAbilityBonus(character.abilities["Int"]),(0,0,0), font=font)
	if character.skills["Perception"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 1960), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1950), "+" + str(abilityBonus(character.abilities["Wis"]) + 2),(0,0,0), font=font)
		draw.text((150, 2475), str(10 + abilityBonus(character.abilities["Wis"]) + 2),(0,0,0), font=font)
	
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 1950), writeAbilityBonus(character.abilities["Wis"]),(0,0,0), font=font)
		draw.text((150, 2475), str(10 + abilityBonus(character.abilities["Wis"])),(0,0,0), font=font)
	if character.skills["Performance"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 2015), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 2005), "+" + str(abilityBonus(character.abilities["Cha"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 2005), writeAbilityBonus(character.abilities["Cha"]),(0,0,0), font=font)
	if character.skills["Persuasion"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 2070), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 2060), "+" + str(abilityBonus(character.abilities["Cha"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 2060), writeAbilityBonus(character.abilities["Cha"]),(0,0,0), font=font)
	if character.skills["Religion"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 2125), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 2115), "+" + str(abilityBonus(character.abilities["Int"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 2115), writeAbilityBonus(character.abilities["Int"]),(0,0,0), font=font)
	if character.skills["Sleight of Hand"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 2185), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 2175), "+" + str(abilityBonus(character.abilities["Dex"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 2175), writeAbilityBonus(character.abilities["Dex"]),(0,0,0), font=font)
	if character.skills["Stealth"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 2240), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 2230), "+" + str(abilityBonus(character.abilities["Dex"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 2230), writeAbilityBonus(character.abilities["Dex"]),(0,0,0), font=font)
	if character.skills["Survival"] == True:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		draw.text((425, 2295), "X",(0,0,0), font=font)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 2285), "+" + str(abilityBonus(character.abilities["Wis"]) + 2),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
		draw.text((465, 2285), writeAbilityBonus(character.abilities["Wis"]),(0,0,0), font=font)
def writeEquipment(image, character):
#1110 x 2460 500 wide
	line = 0
	img = image
	draw = ImageDraw.Draw(img)
	equipmentString = str(character.equipment).strip('[]')
	toPrint = textwrap.wrap(equipmentString, 30)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
	for x in range(len(toPrint)):
		draw.text((1110, 2470 + line), str(toPrint[x]).replace("'",""),(0,0,0), font=font)
		line += 47
	
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",40)
	draw.text((975, 2505), str(character.CP),(0,0,0), font=font)
	draw.text((975, 2615), str(character.SP),(0,0,0), font=font)
	draw.text((975, 2830), str(character.GP),(0,0,0), font=font)
	
def writeAttacks(image, character):
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
	if character.weapon1 != None:
		draw.text((950, 1650), character.weapon1.name,(0,0,0), font=font)
		draw.text((1230, 1650), "+" + str(abilityBonus(character.abilities["Str"]) + 2),(0,0,0), font=font)
		draw.text((1380, 1650), character.weapon1.damage + " " + character.weapon1.damageType,(0,0,0), font=font)
	
	if character.weapon2!= None:
		draw.text((950, 1730), character.weapon2.name,(0,0,0), font=font)
		draw.text((1230, 1730), "+" + str(abilityBonus(character.abilities["Str"]) + 2),(0,0,0), font=font)
		draw.text((1380, 1730), character.weapon2.damage + " " + character.weapon2.damageType,(0,0,0), font=font)

def writeArmor(image, character):
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",60)
	draw.text((990, 610), str(character.ac),(0,0,0), font=font)
	
def writeSpells(image, character):
	if character.caster == False:
		pass
	else:
		line = 0
		img = image
		draw = ImageDraw.Draw(img)
		cantripString = "Cantrips: " + str(character.cantrips).strip('[]')
		spells1String = "Level 1: " + str(character.spells1).strip('[]')
		
		toPrint = textwrap.wrap(cantripString, 50)
		font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",30)
		for x in range(len(toPrint)):
			draw.text((925, 1880 + line), str(toPrint[x]).replace("'",""),(0,0,0), font=font)
			line += 45
		
		line += 45
		toPrint = textwrap.wrap(spells1String, 50)
		for x in range(len(toPrint)):
			draw.text((925, 1880 + line), str(toPrint[x]).replace("'",""),(0,0,0), font=font)
			line += 45
		
		