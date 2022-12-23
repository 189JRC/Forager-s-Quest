import random
from project import find_mushroom, names_only, player_info, gatherer


def test_find_mushroom():
    assert(type(find_mushroom())) == list
    assert(type(find_mushroom()[0])) == list
    assert(len(find_mushroom())) == 11
    assert(len(find_mushroom()[0])) == 4
    assert(find_mushroom()[0]) != find_mushroom()[1]
    assert(find_mushroom()[0]) != find_mushroom()[2] or find_mushroom()[3] or find_mushroom()[4]
    assert(find_mushroom()[0]) != find_mushroom()[5] or find_mushroom()[6] or find_mushroom()[7]
    assert(find_mushroom()[0]) != find_mushroom()[8] or find_mushroom()[9] or find_mushroom()[10]

def test_names_only():
    assert(type(names_only())) == list
    assert(type(names_only()[0])) == str
    assert(len(names_only())) == 11
    assert(names_only()[0]) != names_only()[1]
    assert(names_only()[0]) != names_only()[2] or names_only()[3] or names_only()[4]
    assert(names_only()[0]) != names_only()[5] or names_only()[6] or names_only()[7]
    assert(names_only()[0]) != names_only()[8] or names_only()[9] or names_only()[10]

def test_player_info():
    assert(type(player_info('Ray Mears', 'Yes'))) == str
    assert(player_info('Bilbo', 'Yes')) == ('Bilbo', 'Yes')
    assert(player_info('Smeagol', 500)) == "Please enter your name and whether you consider yourself a forager!"

########Introduce Mushroom Class in order to test Class method below############################################
class Mushroom:

    def __init__(self):
        self.find = find_mushroom()
        self.random3 = names_only()

    def choice(self):
        selection = random.choice(self.find)
        return selection

    def names3(self):
        picks = [random.choice(self.random3), random.choice(
            self.random3), random.choice(self.random3)]
        return picks
################################################################################################################

def test_gatherer():
    m = Mushroom()
    assert(len(gatherer(m))) == 2
    assert(type(gatherer(m))) == list
    assert(len(gatherer(m)[0])) == 4
    assert(len(gatherer(m)[1])) == 3
    assert(gatherer(m)[1][0] != gatherer(m)[1][1] and gatherer(m)[1][1] != gatherer(m)[1][2])