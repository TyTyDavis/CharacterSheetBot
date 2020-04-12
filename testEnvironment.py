from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import writer
import random
from Character import Character
import races
import classes
import backgrounds
import tracery
from tracery.modifiers import base_english
import flavorText


"""
To do next time:
get SSA name list cleaned up and into silly name list


Tweaks to make:
tweak name lists
"""

#generate character data
char = Character()
img = Image.open(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\blankSheet.png")
char.setAbilities()
char.setClass()
char.silly = True
char.setName()
char.characterClass.classModifiers(char)
char.setRace()
char.race.racialModifiers(char)
char.setBackground()
char.background.backgroundModifiers(char)
char.setHP()
char.setAlignment()
char.setSpeed()
char.setSkills()
char.setEquipment()
char.setSpells()
char.setSilly()
char.setFlavor()

#write data onto character sheet image
writer.writeName(img, char.name)
writer.writeAbilities(img, char.abilities)
writer.writeClass(img, char.characterClass)
writer.writeRace(img, char.race.name)
writer.writeHP(img, char.hp)
writer.writeHitDie(img, char.hitDie)
writer.writeAlignment(img, char.alignment)
writer.writeInitiative(img, char.abilities["Dex"])
writer.writeSpeed(img, char.speed)
writer.writeProficiency(img, 2)
writer.writeSavingThrows(img, char)
writer.writeSkills(img, char)
writer.writeEquipment(img, char)
writer.writeAttacks(img, char)
writer.writeArmor(img, char)
writer.writeSpells(img, char)
writer.writeBackground(img, char)
writer.writeProficiencies(img, char)
writer.writeTraits(img, char)
writer.writeFlavor(img, char)
img.save(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\newSheet.png")

#output a bunch of flavor text in order to test for grammatical errors
File1 = open(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\textTest.txt","w")
File1.writelines(flavorText.testText())
File1.close()

print(char.gender)
print("Silly:" + str(char.silly))
print(char.caster)
print(char.abilities)
print(char.background.name)
print(char.background.skills)