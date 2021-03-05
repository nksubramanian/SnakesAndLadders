# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import SnakeAndLadder

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    first_game = SnakeAndLadder.SnakeAndLadder()
    valid_dicerolls=set(range(1,7))

    while True:
        val = input("Enter the die value: ")
        if int(val) not in valid_dicerolls:
            raise Exception("Invalid Dice value")
        if first_game.play_onemove(int(val)) != 0:
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
