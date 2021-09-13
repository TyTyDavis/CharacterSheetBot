import twitter
import Character
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

api = twitter.Api(consumer_key="xxxxxxxxxx",
                  consumer_secret="xxxxxxxxxxxxxxxx",
                  access_token_key="xxxxxxxxxxx",
                  access_token_secret="xxxxxxxxxxxxxx")
				  

def postSheet(char):
	api.PostUpdate(char.name + ", " +char.race.name + " " + char.characterClass.name, media=os.path.join(ROOT_DIR, "newSheet.png"))
