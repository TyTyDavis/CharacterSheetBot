from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import writer
from Character import Character

"""
To do next time:
Saving throws based on class
skills
"""
char = Character()
img = Image.open(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\blankSheet.png")
char.name = "Baldren Hellhammer"
char.setAbilities()
char.setClass(char.abilities)
char.setRace(char.characterClass)
char.setHP()
char.setAlignment()
char.setSpeed()
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
img.save(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\newSheet.png")
print(char.silly)