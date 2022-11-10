"""
__filename__ = "english_please.py"
___author__ = "Jessie Campbell"
__copyright__ = "None"
__credits__ = ["Jessie Campbell"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Jessie Campbell"
__email__ = "jessie.t.campbell@gmail.com"
__status__ = "Test"

Module to move the mouse to a specified location series, and click the left mouse button,
to interact with a known context menu.


Uses the following functions:
*main - Main loop of the module
*move_to_1 - Moves mouse to location 1.
*move_to_2 - Moves mouse to location 1.
*move_to_3 - Moves mouse to location 1.
*move_to_4 - Moves mouse to location 1.
*click - Clicks the mouse on call.

Requires the following imports:
-pyautogui
-random

Requires the following files to be present in the same directory as the module.
-
"""
import pyautogui
import random
import time
from random import randrange


def move_to_1():
    """
    Method to  move mouse to position 1.

    Position 1 is lower left hand corner by default, specifically the icon
    that has an 'i' character in a circle.
    :return: None
    """
    x_cord = 212
    y_cord = 829
    # movement time in seconds
    delay_base = 0.25
    # degrade of the base delay, a random floating point number
    delay_degrade = random.uniform(0.01, 0.04)
    delay = delay_base - delay_degrade
    # degrade of the base position, a random int
    pos_degrade = randrange(0, 3)
    x_cord_f = x_cord - pos_degrade
    y_cord_f = y_cord - pos_degrade
    pyautogui.moveTo(x_cord_f, y_cord_f, delay)


def move_to_2():
    """
    Method to  move mouse to position 2.

    Position 2 is near the screen center, specifically the icon that has the
    1 crossing stop sign like icon.
    :return: None
    """
    x_cord = 641
    y_cord = 479
    # movement time in seconds
    delay_base = 0.25
    # degrade of the base delay, a random floating point number
    delay_degrade = random.uniform(0.01, 0.04)
    delay = delay_base - delay_degrade
    # degrade of the base position, a random int
    pos_degrade = randrange(0, 3)
    x_cord_f = x_cord - pos_degrade
    y_cord_f = y_cord - pos_degrade
    pyautogui.moveTo(x_cord_f, y_cord_f, delay)


def move_to_3():
    """
    Method to  move mouse to position 3.

    Position 3 is lower right of center, and is specified by a word, specifically the word
    "continue".
    :return: None
    """
    x_cord = 1181
    y_cord = 628
    # movement time in seconds
    delay_base = 0.25
    # degrade of the base delay, a random floating point number
    delay_degrade = random.uniform(0.01, 0.04)
    delay = delay_base - delay_degrade
    # degrade of the base position, a random int
    pos_degrade = randrange(0, 3)
    x_cord_f = x_cord - pos_degrade
    y_cord_f = y_cord - pos_degrade
    pyautogui.moveTo(x_cord_f, y_cord_f, delay)


def move_to_4():
    """
    Method to move mouse to position 4.

    Position 4 is the upper right of center, and is specified by an x. This is the final movement
    of the script.
    :return: None
    """
    x_cord = 1261
    y_cord = 193
    # base movement time in seconds, subject to the delay degrade below
    delay_base = 0.25
    # degrade of the base delay, a random floating point number
    delay_degrade = random.uniform(0.01, 0.04)
    delay = delay_base - delay_degrade
    # degrade of the base position, a random int
    pos_degrade = randrange(0, 3)
    x_cord_f = x_cord - pos_degrade
    y_cord_f = y_cord - pos_degrade
    pyautogui.moveTo(x_cord_f, y_cord_f, delay)


def click_local():
    """
    Method to click the mouse when at the required location.
    :return:
    """
    # base movement time in seconds, subject to the delay degrade below
    delay_base = 0.05
    # degrade of the base delay, a random floating point number
    delay_degrade = random.uniform(0.001, 0.004)
    delay = delay_base - delay_degrade

    pyautogui.click()


def action():
    move_to_1()
    time.sleep(0.075)
    click_local()
    time.sleep(0.075)
    move_to_2()
    time.sleep(0.075)
    click_local()
    time.sleep(0.075)
    move_to_3()
    time.sleep(0.075)
    click_local()
    time.sleep(0.075)
    move_to_4()
    time.sleep(0.075)
    click_local()
    time.sleep(0.075)


def main():
    action()
    #test_interface()


def test_interface():
    print("Lets go")
    running = True
    var = "0"
    while running is True:
        var = input("\nHit 1 to start, 9 to exit.\n")
        if var == "1":
            action()
        elif var == "9":
            running = False
        else:
            time.sleep(1)
            print("Waiting")


if __name__ == "__main__":
    main()
