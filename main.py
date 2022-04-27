#!/usr/bin/env python
import sys
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
import twitterBot
import schedule
import time
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

print('SheetBot is live!')
#def job():
#function to generate new character and post it
char = Character()
img = Image.open(os.path.join(ROOT_DIR, "static", "blankSheet.png"))
char.setAbilities()
char.setClass()
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
img.save(os.path.join(ROOT_DIR, "static", "newSheet.png"))

#post to twitter
twitterBot.postSheet(char)
print('new character posted!')
img.close()



#schedule tweet every hour at X:30
#schedule.every().hour.at(":30").do(job)

#while True:
 #   schedule.run_pending()
  #  time.sleep(1)