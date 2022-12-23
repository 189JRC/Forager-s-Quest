Video Demo:  https://youtu.be/G-2heJHq9Ns

# Forager's Quest 
A command line game to help players learn to identify wild mushrooms. Players are presented with a series of URL links to anonymous mushrooms, they are then asked 3 questions about each of them. For correct answers players win 'spores'. Total spore-count is presented at the end with the player's name in a ranked score board. Maximimum spores are won for eating gourmet mushrooms, but if the player chooses to eat a mushroom that happens to be poisonous - GAME OVER.

The game consists of 4 files:
* project.py: main structure of game.
* project_text.py: contains text content for the opening/closing sequence and question loop.
* mushroom.csv: contains all data for mushroom identification,; name, season, edibility, and a URL image link
* highscore.csv: contains scores, player names, and date played for all previous players.

I chose to divide the main game into 2 files to allow the main game structure in project.py to be tidier.

The game itself consists of a loop of 3 questions, repeated 5 times;
* Q1 - Identify the mushroom from an image
* Q2 - Identify the season in which it most often appears
* Q3 - Decide whether to eat it

To enhance user experience and make the game replayable; mushrooms are presented in a randomised sequence. At the time of writing
there are 11 different varieties of mushrooms in mushroom.csv. As each game loops for 5 rounds each time the game is different each time it is played. I estimate that there are up to 55,440 variations the game could take*. More mushroom data could be added to mushroom.csv to broaden the scope of the game further.

  As any forager will tell you, mushroom identification is not a straightforward task, and any given mushroom has several
different names, e.g. Amanita Muscaria is also known as Fly Agaric. To enhance playability, I decided that the player will be presented with a multiple choice of 3 names to choose for Q1. Similarly, the answer to Q2 is effectively a multiple choice aswell.

  In developing Forager's Quest I did consider adaptions to allow more flexibility in user input, but as mushroom identification in
the real world requires precision, I thought it best to let the programme be unforgiving of user error. The spore-score for each correct answer reflects the difficulty of the question, with the highest rewards given for choosing to eat a gourmet mushroom. Naturally, the choice to eat a poisonous mushroom leads to the highest penalty of all - game over.

* 5 rounds with no repetition. Sample of 11 mushrooms. 11 x 10 x 9 x 8 x 7 = 55,440.
