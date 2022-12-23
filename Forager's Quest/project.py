
import project_text
import random
import csv
from tabulate import tabulate
import csv
import pandas
from datetime import date

game_length = 5 #this game cycles in rounds of 3 questions. number of questions in game = (game_length x 3)
purple = '\033[37m'; bold = '\033[1m'; end = '\033[0m' #add colour and style to output

class Player: # Returns a personalised greeting and outro for each player
    def __init__(self, name, forager):
        self.name = name
        self.forager = forager

    def __str__(self):
        if 'y' in self.forager:
            self.forager = "budding forager"
            return f"{self.name}, you are a {self.forager}. Your experience should serve you well..."
        else:
            self.forager = "aspiring forager"
            return f"{self.name}, you are now an {self.forager}! You must tread carefully..."


class Mushroom: # Retrieves items from mushroom.csv

    def __init__(self):
        self.find = find_mushroom()  # returns a list of lists of all mushroom info in csv
        self.random3 = names_only()  # returns a list of names of all mushrooms in csv

    def choice(self):  # returns a random mushroom info list from csv, list of str.s, [name, season, edibility score(0-2), URL]
        selection = random.choice(self.find)
        return selection

    def names3(self):  # creates list of 3 random mushroom from csv [name, name, name]
        picks = [random.choice(self.random3), random.choice(
            self.random3), random.choice(self.random3)]
        return picks

def gatherer(mushroom):#Returns batch of 4 mushrooms*, list of 4 strings from a row of mushroom.csv
                       #and a list of 3 mushroom name strings
                       #the list of 3 is mutually exclusive and contains the chosen one
                       #the chosen one = the mushroom from the info list, the one being questioned about
    while True:

        choice = mushroom.choice()
        rand3 = mushroom.names3()

        if choice[0] in rand3 and rand3[0] != rand3[1] and rand3[1] != rand3[2] and rand3[0] != rand3[2]:
                #non_repetition.append(choice[0])
                return ([choice] + [rand3])
        else:
                continue

def find_mushroom(): #returns contents of csv file
    basket = []
    db = open("mushroom.csv", "r")
    for row in csv.reader(db, delimiter=','):
        basket.append(row)
    return basket


def names_only(): #returns names of all mushrooms from csv file
    names = []
    db = open("mushroom.csv", "r")
    for row in csv.reader(db, delimiter=','):
        names.append(row[0])
    return names


def player_info(name, exp): #validates player information

    if name.isalnum() and str(exp).isalpha():
        return name, exp
    else:
        return "Please enter your name and whether you consider yourself a forager!"

def main():

    name = input("What is your name? ").strip()
    exp = input("Are you a forager? ").strip().lower()
    p1 = Player(name, exp) #returns player name and if/not a 'forager'
    project_text.Quest.title(p1) #begins start title sequence w/ personalised greeting

    spores = 0 #initiates player score
    batch4 = Mushroom() #creates RANDOM batch of 4 mushrooms (list of 1 list + 3 items.)
    #item 1 = list = 1 full line of info from mushroom.csv
    #items 2,3,4 = strs = the names of 3 mushrooms for multiple choice to be used for multiple choice

    spores = game_engine(batch4, spores) #initiates the main game sequence, returns the final score
    project_text.Quest.end_title(p1, spores) #creates personalised end text for the player
    print(end_sequence(spores, p1.name)) #presents score board, itemised by spores

def game_engine(batch4, spores): #main loop for game, calls on project_text.py for question textual content

    no_repeat = []

    while len(no_repeat) < game_length: #len will deterine how many rounds the game will last
        chosen1, batch3 = gatherer(batch4)
        if chosen1[0] not in no_repeat:

            score1, ans1 = project_text.Quest.q1(chosen1,batch3)
            print(ans1)
            spores += score1
            no_repeat.append(chosen1[0])

            score2, ans2 = project_text.Quest.q2(chosen1)
            print(ans2)
            spores += score2

            score3, ans3 = project_text.Quest.q3(chosen1)
            print(ans3)
            spores += score3
            print(f"\n🍄 {bold}{purple}You have {spores} spores in total. 🍄{end}\n")

        else:
            pass

    return spores

def end_sequence(score, name): #uses csv to write new score to highscore.csv. Uses pandas to reorder from highest to lowest score.
    today = date.today() #uses date. to give date score was achieved and finally tabulature for a pprint of high scores.

    with open('highscore.csv', mode='a', newline='') as f:
        record = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        record.writerow([score, name, today])

    dframe = pandas.read_csv('highscore.csv', index_col='Spores', header=0, names=['Spores','Name','Date'])
    dframe = dframe.sort_values(by="Spores", ascending=False)
    dframe.to_csv('highscore.csv')

    fungi = []
    with open('highscore.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            fungi.append(row)

    return tabulate(fungi, headers="firstrow", tablefmt="grid")

if __name__ == "__main__":
    main()