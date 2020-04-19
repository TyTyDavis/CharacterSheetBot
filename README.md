<h1>Charactger generation</h1>
<h2>Names:</h2>
<p>Names are generated using this <a href="https://github.com/Kroket93/Fantasy-Name-Generator-python-script-">name generator</a>, with some tweaks made to the name list, and more tweaks to come.
<p>There is a random chance that a character might receive a silly name, in which case last names will be pulled from a list of silly last names, and first names will be pulled from a list of more common American names, sourced from the Social Security Administration. Silly characters also have class and race chosen without consideration of relevant ability scores.
<h2>Stats:</h2>
<p>All data is stored in the Character class, which has functions to set all relevant stats (ability scores, race, class, skills, etc.)
Races, classes, weapons and armors are all defined as classes. 
<h2>Flavor text:</h2>
<p>The personality trait, ideal, bond and flaw are generated using <a href="https://github.com/aparrish/pytracery">pytracery</a>, a Python version of Kate Compton's <a href="tracery.io">Tracery</a> language.
<p>Each character class and background have their own unique Tracery elements to create flavor text that is suited to the character, although there are also more generic elements that can be applied to any character.
<h1>Character sheet printing</h1>
Once all of the relevant stats are generated, Python Image Library (PIL) is used to print the stats onto a .png of a character sheet. Each area of the character sheet is handled by its own function.
<h1>Implementation</h1>
<p>The bot's main Python script generates one character, prints it onto a sheet, and then, using the <a href="https://python-twitter.readthedocs.io/en/latest/">python-twitter</a> to access the Twitter API, sends a tweet.
<p>The bot is kept on a Raspbery Pi which runs this script once every hour using crontab.
<h1>To do</h1>
<ul>
<li>Create new name lists</li>
<li>Automate cleric domains and other class feature choices</li>
<li>Add unique Tracery lists to races, weapons, and armor</li>
<li>Allow for characters with shield</li>
<li>Allow for characters past level 1</li>
</ul>
