import random
import webbrowser
import time


url = 'https://rajparsaniya.000webhostapp.com/'


def main():

    print('\n\n-----------------------------------------------------------------------')
    print('| Options                 | Use                                       |')
    print('-----------------------------------------------------------------------')
    print('| (1) Start New Game      | To start a new game.                      |')
    print('| (2) About Developer     | To see information about the developer    |')
    print('| (3) Game Rule           | To Know rules of the game.                |')
    print('| (4) Exit                | To Quit/Exit the game.                    |')
    print('-----------------------------------------------------------------------\n')

    EnteredChoice = input('Enter your choice : ')

    if EnteredChoice == '1':
        startGame()
        
    elif EnteredChoice == '2':
        about()

    elif EnteredChoice == '3':
        rule()
        
    elif EnteredChoice == '4':
        QuitGame()
        
    else:
        main()


def startGame():
    
    name = input("\nEnter your name : ")
    print("\nAll the best", name)

    words = [
        "website",
        "hangman",
        "abruptly",
        "absurd",
        "abyss",
        "affix",
        "askew",
        "avenue",
        "awkward",
        "axiom",
        "azure",
        "bagpipes",
        "bandwagon",
        "banjo",
        "bayou",
        "beekeeper",
        "blitz",
        "blizzard",
        "boggle",
        "bookworm",
        "boxcar",
        "boxful",
        "buckaroo",
        "buffalo",
        "buffoon",
        "buxom",
        "buzzard",
        "buzzing",
        "buzzwords",
        "caliph",
        "cobweb",
        "cockiness",
        "croquet",
        "crypt",
        "curacao",
        "cycle",
        "daiquiri",
        "dirndl",
        "disavow",
        "dizzying",
        "duplex",
        "dwarves",
        "embezzle",
        "equip",
        "espionage",
        "euouae",
        "exodus",
        "faking",
        "fishhook",
        "fixable",
        "fjord",
        "flapjack",
        "flopping",
        "fluffiness",
        "flyby",
        "foxglove",
        "frazzled",
        "frizzled",
        "fuchsia",
        "funny",
        "gabby",
        "galaxy",
        "galvanize",
        "gazebo",
        "giaour",
        "gizmo",
        "glowworm",
        "glyph",
        "gnarly",
        "gnostic",
        "gossip",
        "grogginess",
        "haiku",
        "haphazard",
        "hyphen",
        "iatrogenic",
        "icebox",
        "injury",
        "ivory",
        "ivy",
        "jackpot",
        "jaundice",
        "jawbreaker",
        "jaywalk",
        "jazziest",
        "jazzy",
        "jelly",
        "jigsaw",
        "jinx",
        "jiujitsu",
        "jockey",
        "jogging",
        "joking",
        "jovial",
        "joyful",
        "juicy",
        "jukebox",
        "jumbo",
        "kayak",
        "kazoo",
        "keyhole",
        "khaki",
        "kilobyte",
        "kiosk",
        "kitsch",
        "kiwifruit",
        "klutz",
        "knapsack",
        "larynx",
        "lengths",
        "lucky",
        "luxury",
        "lymph",
        "marquis",
        "matrix",
        "megahertz",
        "microwave",
        "mnemonic",
        "mystify",
        "naphtha",
        "nightclub",
        "nowadays",
        "numbskull",
        "nymph",
        "onyx",
        "ovary",
        "oxidize",
        "oxygen",
        "pajama",
        "peekaboo",
        "phlegm",
        "pixel",
        "pizazz",
        "pneumonia",
        "polka",
        "pshaw",
        "psyche",
        "puppy",
        "puzzling",
        "quartz",
        "queue",
        "quips",
        "quixotic",
        "quiz",
        "quizzes",
        "quorum",
        "razzmatazz",
        "rhubarb",
        "rhythm",
        "rickshaw",
        "schnapps",
        "scratch",
        "shiv",
        "snazzy",
        "sphinx",
        "spritz",
        "squawk",
        "staff",
        "strength",
        "strengths",
        "stretch",
        "stronghold",
        "stymied",
        "subway",
        "swivel",
        "syndrome",
        "thriftless",
        "thumbscrew",
        "topaz",
        "transcript",
        "transgress",
        "transplant",
        "triphthong",
        "twelfth",
        "twelfths",
        "unknown",
        "unworthy",
        "unzip",
        "uptown",
        "vaporize",
        "vixen",
        "vodka",
        "voodoo",
        "vortex",
        "voyeurism",
        "walkway",
        "waltz",
        "wave",
        "wavy",
        "waxy",
        "wellspring",
        "wheezy",
        "whiskey",
        "whizzing",
        "whomever",
        "wimpy",
        "witchcraft",
        "wizard",
        "woozy",
        "wristwatch",
        "wyvern",
        "xylophone",
        "yachtsman",
        "yippee",
        "yoked",
        "youthful",
        "yummy",
        "zephyr",
        "zigzag",
        "zigzagging",
        "zilch",
        "zipper",
        "zodiac",
        "zombie",    
    ]

    word = random.choice(words)
    print('\n--------------------------')
    print("|  Guess the characters  |")
    print('--------------------------\n')
    guesses = ""

    turns = 6

    while turns > 0:

        failed = 0

        for char in word:
            if char in guesses:
                print(char, end="")
            else:
                print("_", end="")

                failed += 1

        if failed == 0:
            print("\n\n-------------------")
            print("|     You Win     |")
            print("-------------------")
            print("\nThe Word Is : ", word)
            main()
            break

        guess = input("\n\nGuess The Character: ")
        guesses += guess

        if guess not in word:
            turns -= 1
            print("\nWrong")
            print("You Have", +turns, "More Guesses\n")
            if turns == 0:
                print("\n\n--------------------")
                print("|     You Lose     |")
                print("--------------------")
                print("\nThe Word Is : ", word)
                main()


def rule():
    print('\n\n---------------------------')
    print('|        Game Rule        |')
    print('---------------------------\n')
    print('-> The rules of Hangman are fairly simple')
    print('-> It is a traditional two or more player game where one player thinks of a word and the others tries to guess it by trying to find each of the missing letters.')
    print('-> If the puzzle has not been solved after 7 guesses, the player trying to guess the word has lost the game.')
    main()


def about():
    print('\n\n---------------------------------')
    print('|        About Developer        |')
    print('---------------------------------\n')
    print('-> Design By Raj Parsaniya\n')
    
    KeyPress = input('-> Do you want to visit my website (Y/N) : ')

    if KeyPress == 'Y' or KeyPress == 'y':
        webbrowser.open_new_tab(url)
    else:
        main()



def QuitGame():
    print('\n\n\n\t Design By Raj Parsaniya \n\n\n')
    time.sleep(5)
    exit()
    


main()
