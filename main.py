from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import writer
import random
from Character import Character


"""
To do next time:
skills
equipment
attacks
spells

Tweaks to make:
make a "silly" last name list
tweak name lists
"""
char = Character()
img = Image.open(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\blankSheet.png")
char.gender = random.choice(["M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "N"])
char.setAbilities()
char.setClass(char.abilities)
char.setRace(char.characterClass)
char.setName()
char.setHP()
char.setAlignment()
char.setSpeed()
char.setSkills()
writer.writeName(img, char.name)
writer.writeAbilities(img, char.abilities)
writer.writeClass(img, char.characterClass)
writer.writeRace(img, char.race)
writer.writeHP(img, char.hp)
writer.writeHitDie(img, char.hitDie)
writer.writeAlignment(img, char.alignment)
writer.writeInitiative(img, char.abilities[1])
writer.writeSpeed(img, char.speed)
writer.writeProficiency(img, 2)
writer.writeSavingThrows(img, char)
writer.writeSkills(img, char)
img.save(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\newSheet.png")
print(char.gender)