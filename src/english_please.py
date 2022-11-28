"""
__filename__ = "english_please.py"
___author__ = "Jessie Campbell"
__copyright__ = "Jessie Campbell"
__credits__ = ["Jessie Campbell"]
__license__ = "MIT"
__version__ = "0.1.1"
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
*get_config - Function to locate and serialize config json.
*config_me - Function to run the config option logic.

Defines the following classes:
*Config - In memory storage of active configuration settings.

Requires the following imports:
-pyautogui
-random
-time
-logging
-json
-import config_cli

***Also requires the following dependant packages:
-pillow
-pyscreeze
-cv2 (opencv-python)

Requires the following files to be present in the same directory as the module.
- config - Folder with the config.json file.
- graphics - Folder with the p1_target_obj.png and p2_target_obj.png files.
- logs - Folder to contain logged info
- config_cli.py - Module to run the configuration tool.
- ep_exceptions.py - Module with custom exceptions.
"""
import random
from random import randrange
import time
import logging
import json
import pyautogui
# the following are added to support PyInstaller builds
# noinspection PyUnresolvedReferences
import PIL  # pylint: disable=unused-import
# noinspection PyUnresolvedReferences
import pyscreeze  # pylint: disable=unused-import
# the following are custom modules related to this project
import config_cli
import ep_exceptions as errors


def move_to_1(config):
    """
    Method to  move mouse to position 1.

    Position 1 is lower left hand corner by default, specifically the icon
    that has an 'i' character in a circle.
    :return: None
    """
    path_name = "Target 1"  # name of the path, used for execution logging
    x_cord = None
    y_cord = None
    waited = False
    control = 0  # flag variable if exception passed set to 1 before exception logging
    obj = "./graphics/p1_target_obj.png"
    # testing adds********************************** need to find out if this is always necessary
    # might need to incorporate this in a try block
    pyautogui.moveTo(400, 400)
    pyautogui.click()
    # testing adds******************************** suspect it is due to a loading delay in exe mode
    try:
        cord = (find_path(obj, 0.9))
        if cord is None:
            time.sleep(0.5)
            waited = True
            cord = (find_path(obj, 0.9))
        x_cord = cord[0]
        y_cord = cord[1]
    except TypeError:
        control = 1  # set flag value to 1 to skip cord_f errors
        errors.PathLockError(path_name, waited)
    # movement time in seconds
    delay_base = 0.25
    # degrade of the base delay, a random floating point number
    delay_degrade = random.uniform(0.01, 0.04)
    delay = delay_base - delay_degrade
    # degrade of the base position, a random int
    pos_degrade = randrange(0, 3)
    tune_x = config.get_config().get('path_1_x_tune')
    tune_y = config.get_config().get('path_1_y_tune')
    try:
        if control == 1:
            pass
        else:
            x_cord = x_cord + tune_x - pos_degrade
            y_cord = y_cord + tune_y - pos_degrade
    except TypeError:
        path_name = path_name + " Final"
        errors.PathLockError(path_name, waited)
    try:
        pyautogui.moveTo(x_cord, y_cord, delay)
    except UnboundLocalError:
        errors.EPUnbound(path_name)


def move_to_2(config):
    """
    Method to  move mouse to position 2.

    Position 2 is near the screen center, specifically the icon that has the
    1 crossing stop sign like icon.
    :return: None
    """
    path_name = "Target 2"  # name of the path, used for execution logging
    x_cord = None
    y_cord = None
    control = 0  # flag variable if exception passed set to 1 before exception logging
    waited = False
    obj = "./graphics/p2_target_obj.png"
    try:
        cord = (find_path(obj, 0.9))
        if cord is None:
            time.sleep(0.5)
            waited = True
            cord = (find_path(obj, 0.9))
        x_cord = cord[0]
        y_cord = cord[1]
    except TypeError:
        control = 1  # set flag value to 1 to skip cord_f errors
        errors.PathLockError(path_name, waited)
    # movement time in seconds
    delay_base = 0.25
    # degrade of the base delay, a random floating point number
    delay_degrade = random.uniform(0.01, 0.04)
    delay = delay_base - delay_degrade
    # degrade of the base position, a random int
    pos_degrade = randrange(0, 3)
    tune_x = config.get_config().get('path_2_x_tune')
    tune_y = config.get_config().get('path_2_y_tune')
    try:
        if control == 1:
            pass
        else:
            x_cord = x_cord + tune_x - pos_degrade
            y_cord = y_cord + tune_y - pos_degrade
    except TypeError:
        path_name = path_name + " Final"
        errors.PathLockError(path_name, waited)
    try:
        pyautogui.moveTo(x_cord, y_cord, delay)
    except UnboundLocalError:
        errors.EPUnbound(path_name)


def move_to_3(config):
    """
    Method to  move mouse to position 3.

    Position 3 is lower right of center, and is specified by a word, specifically the word
    "continue".
    :return: None
    """
    path_name = "Target 3"  # name of the path, used for execution logging
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
    path_name = "Target 4"  # name of the path, used for execution logging
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


def config_me():
    """Function to run the config option logic"""
    try:
        config_obj = Config("config", get_config())  # create the config memory object
        if config_obj.get_config().get("config_required"):
            print("Running Initial Configuration.")
            running = True
            while running:
                config_cli.menu_print()
                usr_input = input("Type your selection and press enter.\n")
                config_cli.config_menu_control(usr_input)
                if not config_cli.config_menu_control(usr_input):
                    print("Exiting Config Menu.\n")
                    print("Setting Config Status to not required.")
                    with open("./config/config.json", 'r', encoding="utf-8") as file:
                        data = json.load(file)
                        data["config_required"] = False
                    with open("./config/config.json", 'w', encoding="utf-8") as file:
                        json.dump(data, file, indent=4)
                    time.sleep(3)
                    running = False
    except FileNotFoundError:  # Add error handling later
        print("Config file not found, recopy from repo.")


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
    # config_obj = Config("config", get_config())  # create the config memory object
    # action(config_obj)
    try:
        # config_me()
        config_obj = Config("config", get_config())  # create the config memory object
        action(config_obj)
        # test_interface(config_obj)
    except Exception as error:  # pylint: disable=broad-except  # to do: add custom exception******
        print(error)  # to do - custom logging to catch this situation


if __name__ == "__main__":
    main()
