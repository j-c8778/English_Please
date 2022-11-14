"""
__filename__ = "english_please.py"
___author__ = "Jessie Campbell"
__copyright__ = "Jessie Campbell"
__credits__ = ["Jessie Campbell"]
__license__ = "MIT"
__version__ = "0.1.0"
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
-json

***Also requires the following dependant packages:
-pillow
-pyscreeze
-cv2 (opencv-python)

Requires the following files to be present in the same directory as the module.
-
"""
import random
from random import randrange
import time
import logging
import json
import pyautogui
import PIL  # pylint: disable=unused-import
import pyscreeze  # pylint: disable=unused-import


def move_to_1(config):
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
    # testing adds******************************************************************************************************
    pyautogui.moveTo(400, 400)
    pyautogui.click()
    # testing adds******************************************************************************************************
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
    tune_x = config.get_config().get('path_1_x_tune')
    tune_y = config.get_config().get('path_1_y_tune')
    try:
        x_cord_f = x_cord + tune_x - pos_degrade
        y_cord_f = y_cord + tune_y - pos_degrade
    except TypeError as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)
    try:
        pyautogui.moveTo(x_cord_f, y_cord_f, delay)
    except UnboundLocalError as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)


def move_to_2(config):
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
    tune_x = config.get_config().get('path_2_x_tune')
    tune_y = config.get_config().get('path_2_y_tune')
    try:
        x_cord_f = x_cord + tune_x - pos_degrade
        y_cord_f = y_cord + tune_y - pos_degrade
    except TypeError as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)
    try:
        pyautogui.moveTo(x_cord_f, y_cord_f, delay)
    except UnboundLocalError as error:
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)


def move_to_3(config):
    """
    Method to  move mouse to position 3.

    Position 3 is lower right of center, and is specified by a word, specifically the word
    "continue".
    :return: None
    """
    now = time.strftime("%a,%d%b%Y_%H_%M_%S", time.localtime())
    error_path = "./error_log" + "_" + now + ".txt"
    x_cord = config.get_config().get("path_3_x_cord")
    y_cord = config.get_config().get("path_3_y_cord")
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


def move_to_4(config):
    """
    Method to move mouse to position 4.

    Position 4 is the upper right of center, and is specified by an x. This is the final movement
    of the script.
    :return: None
    """
    now = time.strftime("%a,%d%b%Y_%H_%M_%S", time.localtime())
    error_path = "./error_log" + "_" + now + ".txt"
    x_cord = config.get_config().get("path_4_x_cord")
    y_cord = config.get_config().get("path_4_y_cord")
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


def action(config):
    """
    Method to run the sequence.
    :return: None
    """
    de_pau = config.get_config().get("default_pause")
    pyautogui.PAUSE = config.get_config().get("py_a_gui_pause")
    move_to_1(config)
    time.sleep(de_pau)
    click_local()
    time.sleep(config.get_config().get("path_2_pause"))  # path 2 slower to load, longer wait
    move_to_2(config)
    time.sleep(de_pau)
    click_local()
    time.sleep(de_pau)
    move_to_3(config)
    time.sleep(de_pau)
    click_local()
    time.sleep(de_pau)
    move_to_4(config)
    time.sleep(de_pau)
    click_local()
    time.sleep(de_pau)


def test_interface(config):
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
            action(config)
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


def get_config():
    """
    Method to get the configuration settings from a json file.
    :return: config (dict): A dictionary of the overall configuration settings for the program.
    """

    with open("./config/config.json", 'r', encoding="utf-8") as file:
        config = json.load(file)
    return config


class Config:
    """Class to define configuration items in memory."""

    def __init__(self, name, config):
        self.name = name
        self.config = config

    def get_name(self):
        """:return name (str)"""
        return self.name

    def get_config(self):
        """:return config (dict)"""
        return self.config


def main():
    """Main Method of the program."""
    # now = time.strftime("%a,%d%b%Y_%H_%M_%S", time.localtime())
    # error_path = "./error_log" + "_" + now + ".txt"
    try:
        config_obj = Config("config", get_config())  # create the config memory object
        # this whole section needs to be reworked
        try:
            if config_obj.get_config().get("config_required"):
                action(config_obj) #this needs redoing
                # print("starting config\n")
                # print("hover mouse over continue button\n")
                # input("hit enter when over continue button\n")
                # p3 = pyautogui.position()
                # print("hover mouse over x button\n")
                # input("hit enter when ready")
                # p4 = pyautogui.position()
                # print("Path 3 variables: ")
                # print(p3)
                # print("Path 4 variables: ")
                # print(p4)
                # input("hit enter when you have written those down")
            if config_obj.get_config().get("config_required") is False:
                action(config_obj)
        except Exception as error:
            now = time.strftime("%a,%d%b%Y_%H_%M_%S", time.localtime())
            error_path = "./error_log" + "_" + now + ".txt"
            logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
            logging.exception(error)
        # test_interface(config_obj)
    except Exception as error:
        now = time.strftime("%a,%d%b%Y_%H_%M_%S", time.localtime())
        error_path = "./error_log" + "_" + now + ".txt"
        logging.basicConfig(filename=error_path, encoding="utf-8", level=logging.DEBUG)
        logging.exception(error)


if __name__ == "__main__":
    main()
