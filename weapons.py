class Weapon:
	def __init__(self):
		pass
class Club(Weapon):
	name = "Club"
	damage = "1d4"
	damageType = "Bludgeoning"
	weight = 2
	light = True
	finesse = False
	thrown = False
	twoHand = False
	range = None
	
class Dagger(Weapon):
	name = "Dagger"
	damage = "1d4"
	damageType = "piercing"
	weight = 1
	light = True
	finesse = True
	thrown = False
	twoHand = False
	range = "20/60"
	
class Greatclub(Weapon):
	name = "Greatclub"
	damage = "1d8"
	damageType = "Bludgeoning"
	weight = 10
	light = False
	finesse = False
	thrown = False
	twoHand = True
	range = None
	
class Handaxe(Weapon):
	name = "2 Handaxes"
	damage = "1d6"
	damageType = "Slashing"
	weight = 2
	light = True
	finesse = False
	thrown = True
	twoHand = False
	range = "20/60"
	
class Javelin(Weapon):
	name = "Javelin"
	damage = "1d6"
	damageType = "Piercing"
	weight = 2
	light = False
	finesse = False
	thrown = True
	twoHand = False
	range = "30/120"
	
class LightHammer(Weapon):
	name = "Light Hammer"
	damage = "1d4"
	damageType = "Bludgeoning"
	weight = 2
	light = True
	finesse = False
	thrown = True
	twoHand = False
	range = "20/60"

class Mace(Weapon):
	name = "Mace"
	damage = "1d6"
	damageType = "Bludgeoning"
	weight = 4
	light = False
	finesse = False
	thrown = False
	twoHand = False
	range = None

class Quarterstaff(Weapon):
	name = "Quarterstaff"
	damage = "1d6"
	damageType = "Bludgeoning"
	weight = 4
	light = False
	finesse = False
	thrown = False
	twoHand = False
	range = None

class Sickle(Weapon):
	name = "Mace"
	damage = "1d4"
	damageType = "Slashing"
	weight = 2
	light = True
	finesse = False
	thrown = False
	twoHand = False
	range = None

class Spear(Weapon):
	name = "Spear"
	damage = "1d6"
	damageType = "Piercing"
	weight = 3
	light = False
	finesse = False
	thrown = True
	twoHand = False
	range = "20/60"

class LightCrossbow(Weapon):
	name = "Light crossbow"
	damage = "1d8"
	damageType = "Piercing"
	weight = 5
	light = False
	finesse = False
	thrown = True
	twoHand = True
	range = "80/320"

class Dart(Weapon):
	name = "Dart"
	damage = "1d4"
	damageType = "Piercing"
	weight = 0.25
	light = False
	finesse = True
	thrown = True
	twoHand = False
	range = "20/60"

class Shortbow(Weapon):
	name = "Shortbow"
	damage = "1d6"
	damageType = "Piercing"
	weight = 2
	light = False
	finesse = False
	thrown = True
	twoHand = True
	range = "80/320"
	
#martial
class Battleaxe(Weapon):
	name = "Battleaxe"
	damage = "1d8"
	damageType = "Slashing"
	weight = 4
	light = False
	finesse = False
	thrown = False
	twoHand = False
	range = None

class Flail(Weapon):
	name = "Flail"
	damage = "1d8"
	damageType = "Bludgeoning"
	weight = 2
	light = False
	finesse = False
	thrown = False
	twoHand = False
	range = None

class Glaive(Weapon):
	name = "Glaive"
	damage = "1d10"
	damageType = "Slashing"
	weight = 6
	light = False
	heavy = True
	finesse = False
	thrown = False
	twoHand = True
	range = None

class Greataxe(Weapon):
	name = "Greataxe"
	damage = "1d12"
	damageType = "Slashing"
	weight = 7
	light = False
	heavy = True
	finesse = False
	thrown = False
	twoHand = True
	range = None
	
class Greatsword(Weapon):
	name = "Greatsword"
	damage = "2d6"
	damageType = "Slashing"
	weight = 6
	light = False
	heavy = True
	finesse = False
	thrown = False
	twoHand = True
	range = None

class Halberd(Weapon):
	name = "Halberd"
	damage = "1d10"
	damageType = "Slashing"
	weight = 6
	light = False
	heavy = True
	finesse = False
	thrown = False
	twoHand = True
	reach = True
	range = None

class Lance(Weapon):
	name = "Lance"
	damage = "1d12"
	damageType = "Piercing"
	weight = 6
	light = False
	heavy = False
	finesse = False
	thrown = False
	twoHand = False
	reach = True
	range = None

class Longsword(Weapon):
	name = "Longsword"
	damage = "1d8"
	damageType = "Slashing"
	weight = 3
	light = False
	heavy = False
	finesse = False
	thrown = False
	twoHand = False
	range = None
	
class Maul(Weapon):
	name = "Maul"
	damage = "2d6"
	damageType = "Bludgeoning"
	weight = 10
	light = False
	heavy = True
	finesse = False
	thrown = False
	twoHand = True
	range = None
	
class Morningstar(Weapon):
	name = "Morningstar"
	damage = "1d8"
	damageType = "Piercing"
	weight = 4
	light = False
	heavy = False
	finesse = False
	thrown = False
	twoHand = False
	range = None
	
class Pike(Weapon):
	name = "Pike"
	damage = "1d10"
	damageType = "Piercing"
	weight = 18
	light = False
	heavy = True
	finesse = False
	thrown = False
	twoHand = True
	reach = True
	range = None

class Rapier(Weapon):
	name = "Rapier"
	damage = "1d8"
	damageType = "Piercing"
	weight = 2
	light = False
	heavy = False
	finesse = True
	thrown = False
	twoHand = False
	range = None
	
class Scimitar(Weapon):
	name = "Scimitar"
	damage = "1d6"
	damageType = "Slashing"
	weight = 3
	light = True
	heavy = False
	finesse = True
	thrown = False
	twoHand = False
	range = None
	
class Shortsword(Weapon):
	name = "Shortsword"
	damage = "1d6"
	damageType = "Piercing"
	weight = 2
	light = True
	heavy = False
	finesse = True
	thrown = False
	twoHand = False
	range = None

class Trident(Weapon):
	name = "Trident"
	damage = "1d6"
	damageType = "Piercing"
	weight = 4
	light = False
	heavy = False
	finesse = False
	thrown = True
	twoHand = False
	range = "20/60"
	
class Warpick(Weapon):
	name = "War pick"
	damage = "1d8"
	damageType = "Piercing"
	weight = 2
	light = False
	heavy = False
	finesse = False
	thrown = False
	twoHand = False
	range = None

class Warhammer(Weapon):
	name = "Warhammer"
	damage = "1d8"
	damageType = "Bludgeoning"
	weight = 2
	light = False
	heavy = False
	finesse = False
	thrown = False
	twoHand = False
	range = None

class Whip(Weapon):
	name = "Whip"
	damage = "1d4"
	damageType = "Slashing"
	weight = 6
	light = False
	heavy = False
	finesse = True
	thrown = False
	twoHand = False
	reach = True
	range = None
	
class Blowgun(Weapon):
	name = "Blowgun"
	damage = "1"
	damageType = "Piercing"
	weight = 1
	light = False
	heavy = False
	finesse = False
	thrown = True
	twoHand = False
	range = "25/100"

class HandCrossbow(Weapon):
	name = "Hand crossbow"
	damage = "1d6"
	damageType = "Piercing"
	weight = 3
	light = True
	heavy = False
	finesse = False
	thrown = True
	twoHand = False
	range = "30/120"
	
class HeavyCrossbow(Weapon):
	name = "Heavy Crossbow"
	damage = "1d10"
	damageType = "Piercing"
	weight = 18
	light = False
	heavy = True
	finesse = False
	thrown = True
	twoHand = True
	range = "100/400"
	
class Longbow(Weapon):
	name = "Longbow"
	damage = "1d8"
	damageType = "Piercing"
	weight = 2
	light = False
	heavy = True
	finesse = False
	thrown = True
	twoHand = True
	range = "150/600"
	
class MonkHands(Weapon):
	name = "Unarmed"
	damage = "1d4"
	damageType = "Bludgeoning"
	weight = 0
	light = False
	heavy = False
	finesse = False
	thrown = False
	twoHand = True
	range = None
	