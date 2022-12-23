import pyshorteners
import sys
import time

red = '\033[31m'; green = '\033[32m'; yellow = '\033[33m'; blue = '\033[34m'; pink = '\033[35m'; cyan = '\033[36m'; purple = '\033[37m'
bold = '\033[1m'; ital = '\033[3m'; end = '\033[0m'

def main():
    ...
    
def death():
    sys.exit(f"\n{red}🤮{bold} This is a poisonous mushroom... you are dead{end} 💀\n")

def short(long): #takes long urls and returns tinyurls, for tidyness and to disguise mushroom name from player!
    url_shrink = pyshorteners.Shortener()
    short = url_shrink.tinyurl.short(long)
    return short

class Quest: #contains text content for Q1, Q2, Q3, and for start and end sequences.

    def __init__(self, spawn1, spawn2):
        self.spawn1 = spawn1 #spawn1 is the 'chosen mushroom' that is queried about in each round.
        self.spawn2 = spawn2 #spawn2 is the multichoice list of 3 mushroom names for player to choose from.

    def q1(spawn1, spawn2):
        surl = spawn1[3].strip()
        short_url = short(surl)

        print(f"{cyan}{short_url}{end} \t> {bold}{green}What is the name of this mushroom?{end}".center(10, "~"))
        print(f"{ital}Pssst. It's one of the following; {spawn2[0]}, {spawn2[1]} or {spawn2[2]}...{end} ".center(10, "~"))
        name = input("> ").strip().lower()

        if name == spawn1[0]:
            return 10, f"\nIndeed this is the {bold}{spawn1[0]}{end} mushroom! You have earned {bold}{pink}10{end} spores"
        else:
            return 0, f"\n{ital}For future reference, this is the {bold}{spawn1[0]}{end} mushroom."

    def q2(spawn1):
        print(f"{green}{bold}\nIn which season might you typically find this mushroom; Spring, Summer, Autumn or Winter?{end}")
        time = input("> ").strip().lower()

        if time == spawn1[1].strip():
            return 5, f"\nCorrect! This mushroom appears in the {spawn1[1].capitalize()}. {bold}{pink}5{end} spores for you!"

        else:
            return 0, f"\n{ital}This mushroom typically appears in the {spawn1[1].capitalize()}{end}."

    def q3(spawn1):
        print(f"{green}{bold}\nWould you eat this mushroom?{end} ")
        scran = input("> ").strip().lower()

        if 'y' not in scran and 'n' not in scran:
                print(f"{ital}\nPlease type either 'yes' or 'no'{end}")

        if scran == 'yes' and spawn1[2].strip() == '0':
            death()

        elif scran == 'yes' and spawn1[2].strip() == '1':
            return 0, f"\n{ital}The {spawn1[0]} is edible, but not all that tasty...{end}"

        elif scran == 'yes' and spawn1[2].strip() == '2':
            return 25, f"{bold}{yellow}\nYou have found a gourmet mushroom!{end} The flavour of the {bold}{spawn1[0]}{end} is simply delicious. {bold}{pink}25{end} spores for you!"

        else:
            return 0, f"\nBest to play it safe... {bold}wild mushrooms can be deadly!{end}"

    def title(p1): #an intro sequence like this will impress even the most ardent forager!

        print("~".center(100, "~")), time.sleep(0.05)
        print(f"{bold}{yellow}Welcome to Forager's Quest!{end}".center(113, "~")), time.sleep(0.05)
        print("Your task is to identify the names of mushrooms from their pictures".center(100, "~")), time.sleep(0.05)
        print("~".center(100, "~")), time.sleep(0.05)
        print("For correct answers you win 'spores'".center(100, "~")), time.sleep(0.05)
        print(f"{bold}The more spores you have: the higher your score!{end}".center(108, "~")), time.sleep(0.05)
        print("High scores will be revealed at the end".center(100, "~")), time.sleep(0.05)
        print(f"{bold}Watch out for the {red}poisonous mushrooms!{end}".center(113, "~")), time.sleep(0.05)
        print("~".center(100, "~")), time.sleep(0.05)
        print("~".center(100, "~")), time.sleep(0.05)
        print("               __.....__                ".center(100, "~")), time.sleep(0.05)
        print('            .`" _  o    "`.             '.center(100, "~")), time.sleep(0.05)
        print("          .' O (_)     () o`.           ".center(100, "~")), time.sleep(0.05)
        print("         .           O       .          ".center(100, "~")), time.sleep(0.05)
        print("         . ()   o__...__    O .         ".center(100, "~")), time.sleep(0.05)
        print('        . _.--"""       """--._.        '.center(100, "~")), time.sleep(0.05)
        print('        :"                    ";        '.center(100, "~")), time.sleep(0.05)
        print("        `-.__    :   :    __.-'         ".center(100, "~")), time.sleep(0.05)
        print('             """-:   :-"""              '.center(100, "~")), time.sleep(0.05)
        print("                J     L                 ".center(100, "~")), time.sleep(0.05)
        print("                :     :                 ".center(100, "~")), time.sleep(0.05)
        print("               J       L                ".center(100, "~")), time.sleep(0.05)
        print("               :       :                ".center(100, "~")), time.sleep(0.05)
        print("               `._____.'                ".center(100, "~")), time.sleep(0.05)
        print("~".center(100, "~")), time.sleep(0.05)
        print("~".center(100, "~")), time.sleep(0.05)
        print(f"{bold}{p1}{end}".center(108, "~")), time.sleep(0.05)
        print("~".center(100, "~")), time.sleep(0.05)
        print("~".center(100, "~")), time.sleep(0.05)
        print("~".center(100, "~")), time.sleep(0.05)

    def end_title(p1, spores): #end of game wrap up
        time.sleep(1)
        print(f"{bold}{yellow}Here marks the end of the Forager's Quest{end}".center(113, "~")),time.sleep(0.2)
        print(f"Congratulations, {bold}{p1.name}{end} You collected {spores} spores in total.".center(108, "~")),time.sleep(0.2)
        print(f"Look for your name in the score board below!".center(100, "~")),time.sleep(0.2)
        print("~"*100, end='\n'),time.sleep(0.2)

if __name__ == "__main__":
    main()