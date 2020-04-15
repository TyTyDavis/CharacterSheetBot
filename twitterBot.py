import twitter
import Character


api = twitter.Api(consumer_key="cSJeAfgqlrapOZmxwuXh7QWxf",
                  consumer_secret="IuTEJKzpjrRVCXS59jZSIdjXovU6iIuyJeIwoiGw6aBL3r5WbE",
                  access_token_key="1237052091929178122-Xl6B9gnoV4c8z0ZGPBhtPO6yQKzX7c",
                  access_token_secret="hPjYQ0L0e08QfPdm6MgPgwSVEziGpmOSgIevzMlD8Cr24")
				  

def postSheet(char):
	api.PostUpdate(char.name + ", " +char.race.name + " " + char.characterClass.name, media=r"C:\Users\wiggi\OneDrive\Documents\CharacterSheetBot\newSheet.png")