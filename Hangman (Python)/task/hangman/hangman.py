import random


def idk():
    new_result = ""
    for i in range(len(word)):
        if x == word[i]:
            new_result += x
        else:
            new_result += result[i]
    return new_result


def check_input():

    while True:
        global x
        if len(x) != 1:
            print("Please, input a single letter.")
            print()
            print(result)
            x = input("Input a letter: ")
        elif not(x.isalpha() and x.islower()):
            print("Please, enter a lowercase letter from the English alphabet.")
            print()
            print(result)
            x = input("Input a letter: ")
        elif x in inputs:
            print("You've already guessed this letter.")
            print()
            print(result)
            x = input("Input a letter: ")
        else:
            inputs.add(x)
            break


words = ["python", "java", "swift", "javascript"]

won_games = 0
lost_games = 0

while True:

    word = words[random.randint(0, 3)]

    result = ""

    for i in range(len(word)):
        result += "-"

    print('H A N G M A N')
    print()
    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if menu == "exit":
        break
    elif menu == "results":
        print(f"""        You won: {won_games} times.
        You lost: {lost_games} times. """)
    elif menu == "play":

        attempt = 8

        x = ""
        inputs = set()

        while attempt > 0:
            print(result)
            x = input("Input a letter: ")
            check_input()
            if x in word:
                result = idk()
                if result == word:
                    break
            else:
                print("That letter doesn't appear in the word.")
                print()
                attempt -= 1

        if attempt > 0:
            print(f"You guessed the word {word}!")
            print("You survived!")
            won_games += 1
        else:
            print("You lost!")
            lost_games += 1
