<h1>Charactger generation</h1>
<h2>Names:</h2>
<p>Names are generated using this <a href="https://github.com/Kroket93/Fantasy-Name-Generator-python-script-">name generator</a>, with some tweaks made to the name list, and more tweaks to come.
<p>There is a random chance that a character might receive a silly name, in which case last names will be pulled from a list of silly last names, and first names will be pulled from a list of more common American names, sourced from the Social Security Administration. Silly characters also have class and race chosen without consideration of relevant ability scores. At this point, pronouns are chosen for the character, to be used by Tracery later.
<h2>Stats:</h2>
<p>All data is stored in the Character class, which has functions to set all relevant stats (ability scores, race, class, skills, etc.)
Data for races, classes, weapons and armors are astored as Python classes. 
<p>First, a character's six main ability scores are rolled randomly. Next, the character's class is decided. Based on the character's highest ability score, a different short list of classes is used. For example, a character with high strength could be a Barbarian, Fighter or Paladin. It is at this point that a die is rolled to determine if the character will be "silly," meaning it receives a funnier name, and it's race and class aren't chosen to optimize the character's playability. 
 <p>Next, the character's race (elf, human, dwarf, etc.) is chosen from a weighted list of races that are a good fit for the character's class.
 <p>After all of that, the character's skills, equipment and spells (if applicable) are chosen.
<h2>Flavor text:</h2>
<p>The personality trait, ideal, bond and flaw are generated using <a href="https://github.com/aparrish/pytracery">pytracery</a>, a Python version of Kate Compton's <a href="tracery.io">Tracery</a> language.
<p>Each character class and background have their own unique Tracery elements to create flavor text that is suited to the character, although there are also more generic elements that can be applied to any character. Tracery works like a Madlib, allowing pronouns and other words to be inserted into sentences. In the following example, can extend the possibilities of the flavor text by pulling from lists of places and skills that might be important to our character, all of which can be tailored to fit the character's class, race or background.
  <pre>
    <code>
    'One day, #they# will return to #their# home #place# to show everyone how great of a #trade# #they# #is#.'
    </code>
   </pre>
<h1>Character sheet printing</h1>
Once the relevant stats are generated, Python Image Library (PIL) is used to print the stats onto a .png of a character sheet. Each area of the character sheet is handled by its own function.
<p>Most of these functions take a Character Object as a parameter, so they could used in a program that would allow someone to create a character to their own specifications and print it to a character sheet image.
<h1>Implementation</h1>
<p>The bot's main Python script generates one character, prints it onto a sheet, and then, using <a href="https://python-twitter.readthedocs.io/en/latest/">python-twitter</a> to access the Twitter API, sends a tweet.
<p>The bot is kept on a Raspbery Pi which runs this script once every hour using crontab.
<h1>To do</h1>
<ul>
<li>Create new name lists</li>
<li>Automate cleric domains and other class feature choices</li>
<li>Add unique Tracery lists to races, weapons, and armor</li>
<li>Allow for characters with shield</li>
<li>Allow for characters past level 1</li>
</ul>
