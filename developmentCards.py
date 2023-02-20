import random
from constants import *


class DevelopmentCard:

    def genDevelopmentCard(self, values):
        cards = {1: knightCard(), 2: roadBuildCard(), 3: yearOfPlentyCard(), 4: monopolyCard(),
                 5: universityCard(),
                 6: marketCard(), 7: greatHallCard(), 8: chapelCard(), 9: libraryCard()}
        # Above each function is assigned its own number. This number can be randomly selected by the val variable below

        val = random.choice(values)
        for key, value in cards.items():
            if val == key:
                match val:
                    case 1:
                        global KNIGHT
                        KNIGHT -= 1
                        print(knightCard())
                        if KNIGHT == 0:
                            cards.pop(1)
                    case 2:
                        global ROADBUILD
                        ROADBUILD -= 1
                        print(roadBuildCard())
                        if ROADBUILD == 0:
                            del cards[2]
                    case 3:
                        global YEAROFPLENTY
                        YEAROFPLENTY -= 1
                        print(yearOfPlentyCard())
                        if YEAROFPLENTY == 0:
                            del cards[3]
                    case 4:
                        global MONOPOLY
                        MONOPOLY -= 1
                        print(monopolyCard())
                        if MONOPOLY == 0:
                            del cards[4]
                    case 5:
                        global UNIVERSITY
                        UNIVERSITY -= 1
                        print(universityCard())
                        if UNIVERSITY == 0:
                            del cards[5]
                    case 6:
                        global MARKET
                        MARKET -= 1
                        print(marketCard())
                        if MARKET == 0:
                            del cards[6]
                    case 7:
                        global GREATHALL
                        GREATHALL -= 1
                        print(greatHallCard())
                        if GREATHALL == 0:
                            del cards[7]
                    case 8:
                        global CHAPEL
                        CHAPEL -= 1
                        print(chapelCard())
                        if CHAPEL == 0:
                            del cards[8]
                    case 9:
                        global LIBRARY
                        LIBRARY -= 1
                        print(libraryCard())
                        if LIBRARY == 0:
                            del cards[9]

        if key in cards == False:
            print("No more Development Cards for player use!")


def knightCard():
    return "knight card exe", KNIGHT


def roadBuildCard():
    return "road build card exe", ROADBUILD


def yearOfPlentyCard():
    return "year of plenty card exe", YEAROFPLENTY


def monopolyCard():
    return "monopoly card exe", MONOPOLY


def universityCard():
    return " university card exe", UNIVERSITY


def marketCard():
    return " market card exe", MARKET


def greatHallCard():
    return "great hall card exe", GREATHALL


def chapelCard():
    return "chapel card exe", CHAPEL


def libraryCard():
    return "library card exe", LIBRARY
