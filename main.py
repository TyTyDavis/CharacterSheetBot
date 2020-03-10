from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import writer
from Character import Character

char = Character()
img = Image.open(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\blankSheet.png")
char.name = "Baldren Hellhammer"
char.setAbilities()
writer.writeName(img, char.name)
writer.writeAbilities(img, char.abilities)
img.save(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\newSheet.png")


print(char.abilities)