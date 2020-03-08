from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import writer

img = Image.open(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\blankSheet.jpg")
name = "Baldr Hellhammer"

writer.writeName(img, name)
img.save(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\newSheet.jpg")