from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def writeName(image, name):
#Write character name on sheet
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\Verdana.ttf",50)
	draw.text((200, 270), name,(0,0,0), font=font)