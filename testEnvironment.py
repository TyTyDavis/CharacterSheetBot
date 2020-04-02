from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import writer
import random
from Character import Character


"""
To do next time:
fill out features and trais from both class and race
correctly calculate starting money
add background feature text blocks
add in tracery to write flavor text
fill out Other Proficiencies


Things to fix:
Silly names not appearing

Tweaks to make:
tweak name lists
"""
char = Character()
img = Image.open(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\blankSheet.png")
char.gender = random.choice(["M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "N"])
char.setAbilities()
char.setClass()
#char.testClass()
char.setRace(char.characterClass)
char.setBackground()
char.setName()
char.setHP()
char.setAlignment()
char.setSpeed()
char.setSkills()
char.setEquipment()
char.setSpells()
writer.writeName(img, char.name)
writer.writeAbilities(img, char.abilities)
writer.writeClass(img, char.characterClass)
writer.writeRace(img, char.race)
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
img.save(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\newSheet.png")
print(char.gender)
print(char.silly)
print(char.caster)
print(char.abilities)
print(char.background.name)
print(char.background.skills)