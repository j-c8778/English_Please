"""
__filename__ = "english_please.py"
___author__ = "Jessie Campbell"
__copyright__ = "Jessie Campbell"
__credits__ = ["Jessie Campbell"]
__license__ = "MIT"
__version__ = "0.0.5"
__maintainer__ = "Jessie Campbell"
__email__ = "jessie.t.campbell@gmail.com"
__status__ = "Alpha"

Module to move the mouse to a specified location series, and click the left mouse button,
to interact with a known context menu.

Uses the following functions:
***test_interface - Testing interface for manual control via CLI.***
*main - Main loop of the module
*move_to_1 - Moves mouse to location 1, with random delay.
*move_to_2 - Moves mouse to location 2, with random delay.
*move_to_3 - Moves mouse to location 3, with random delay.
*move_to_4 - Moves mouse to location 4, with random delay.
*click - Clicks the mouse on call, with random delay.
*action - Runs the sequence of events.
*find_path - Finds the end point to aim of the specified location.

Requires the following imports:
-pyautogui
-random
-time
-logging

***Also requires the following dependant packages:
-pillow
-pyscreeze
-cv2 (opencv)

Requires the following files to be present in the same directory as the module.
-
"""
import random
from random import randrange
import time
import logging
import pyautogui


def move_to_1():
    """
    Method to  move mouse to position 1.

    Position 1 is lower left hand corner by default, specifically the icon
    that has an 'i' character in a circle.
    :return: None
    """
    # x_cord = 212
    # y_cord = 829
    x_cord = None
    y_cord = None
    obj = "./graphics/p1_target_obj.png"
    now = time.strftime("%a,%d%b%Y_%H_%M_%S", time.localtime())
    error_path = "./error_log" + "_" + now + ".txt"
    try:
        x_cord = (find_path(obj, 0.9)[0])
        y_cord = (find_path(obj, 0.9)[1])
    except TypeError:
        try:
            time.sleep(0.5)
            x_cord = (find_path(obj, 0.9)[0])
            y_cord = (find_path(obj, 0.9)[1])
        except TypeError as error:
            logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
            logging.exception(error)
    # movement time in seconds
    delay_base = 0.25
    # degrade of the base delay, a random floating point number
    delay_degrade = random.uniform(0.01, 0.04)
    delay = delay_base - delay_degrade
    # degrade of the base position, a random int
    pos_degrade = randrange(0, 3)
    x_cord_f = None
    y_cord_f = None
    try:
        x_cord_f = x_cord + 5 - pos_degrade
        y_cord_f = y_cord + 3 - pos_degrade
    except TypeError as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)
    try:
        pyautogui.moveTo(x_cord_f, y_cord_f, delay)
    except UnboundLocalError as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)


def move_to_2():
    """
    Method to  move mouse to position 2.

    Position 2 is near the screen center, specifically the icon that has the
    1 crossing stop sign like icon.
    :return: None
    """
    x_cord = None
    y_cord = None
    obj = "./graphics/p2_target_obj.png"
    now = time.strftime("%a,%d%b%Y_%H_%M_%S", time.localtime())
    error_path = "./error_log" + "_" + now + ".txt"
    try:
        x_cord = find_path(obj, 0.9)[0]
        y_cord = find_path(obj, 0.9)[1]
    except TypeError:
        try:
            time.sleep(0.5)
            x_cord = find_path(obj, 0.9)[0]
            y_cord = find_path(obj, 0.9)[1]
        except TypeError as error:
            logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
            logging.exception(error)
    # movement time in seconds
    delay_base = 0.25
    # degrade of the base delay, a random floating point number
    delay_degrade = random.uniform(0.01, 0.04)
    delay = delay_base - delay_degrade
    # degrade of the base position, a random int
    pos_degrade = randrange(0, 3)
    x_cord_f = None
    y_cord_f = None
    try:
        x_cord_f = x_cord + 10 - pos_degrade
        y_cord_f = y_cord + 15 - pos_degrade
    except TypeError as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)
    try:
        pyautogui.moveTo(x_cord_f, y_cord_f, delay)
    except UnboundLocalError as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)


def move_to_3():
    """
    Method to  move mouse to position 3.

    Position 3 is lower right of center, and is specified by a word, specifically the word
    "continue".
    :return: None
    """
    now = time.strftime("%a,%d%b%Y_%H_%M_%S", time.localtime())
    error_path = "./error_log" + "_" + now + ".txt"
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
    try:
        pyautogui.moveTo(x_cord_f, y_cord_f, delay)
    except pyautogui.PyAutoGUIException as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)


def move_to_4():
    """
    Method to move mouse to position 4.

    Position 4 is the upper right of center, and is specified by an x. This is the final movement
    of the script.
    :return: None
    """
    now = time.strftime("%a,%d%b%Y_%H_%M_%S", time.localtime())
    error_path = "./error_log" + "_" + now + ".txt"
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
    try:
        pyautogui.moveTo(x_cord_f, y_cord_f, delay)
    except pyautogui.PyAutoGUIException as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)


def click_local():
    """
    Method to click the mouse when at the required location.
    :return: None
    """
    now = time.strftime("%a,%d%b%Y_%H_%M_%S", time.localtime())
    error_path = "./error_log" + "_" + now + ".txt"
    # base movement time in seconds, subject to the delay degrade below
    delay_base = 0.05
    # degrade of the base delay, a random floating point number
    delay_degrade = random.uniform(0.0001, 0.0004)
    delay = delay_base - delay_degrade
    time.sleep(delay)
    try:
        pyautogui.click()
    except pyautogui.PyAutoGUIException as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)


def action():
    """
    Method to run the sequence.
    :return: None
    """
    de_pau = 0.025  # default sleep time
    pyautogui.PAUSE = 0.0025
    move_to_1()
    time.sleep(de_pau)
    click_local()
    time.sleep(.55)  # path 2 slower to load, longer wait
    move_to_2()
    time.sleep(de_pau)
    click_local()
    time.sleep(de_pau)
    move_to_3()
    time.sleep(de_pau)
    click_local()
    time.sleep(de_pau)
    move_to_4()
    time.sleep(de_pau)
    click_local()
    time.sleep(de_pau)


def test_interface():
    """
    Testing interface for CLI control.

    This method opens a CLI to request user input to either start the sequence by calling
    the action(), or exits the program.
    :return: None
    """
    print("Lets go")
    running = True
    while running is True:
        var = input("\nHit 1 to start, 9 to exit.\n")
        if var == "1":
            action()
        elif var == "9":
            running = False
        else:
            time.sleep(1)
            print("Waiting")


def find_path(obj, conf):
    """
    This function will locate the coordinates for path 2.

    This function calls the locate function from pyautogui, and returns the location of the
    target x and y coordinates.
    :return: cord (tuple)
    """
    now = time.strftime("%a,%d%b%Y_%H_%M_%S", time.localtime())
    error_path = "./error_log" + "_" + now + ".txt"
    cord = None
    try:
        cord = pyautogui.locateOnScreen(obj, confidence=conf)
    except pyautogui.ImageNotFoundException as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.debug(error)
    except pyautogui.PyAutoGUIException as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)
    return cord


def main():
    """Main Method of the program."""
    action()
    # test_interface()


if __name__ == "__main__":
    main()
