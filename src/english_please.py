"""
__filename__ = "english_please.py"
__author__ = "Jessie Campbell"
__copyright__ = "Jessie Campbell"
__credits__ = ["Jessie Campbell"]
__license__ = "MIT"
__version__ = "0.1.4"
__maintainer__ = "Jessie Campbell"
__email__ = "jessie.t.campbell@gmail.com"
__status__ = "Alpha"

Module to move the mouse to a specified location series, and click the left mouse button,
to interact with a known context menu.

Uses the following Methods:
***test_interface - Testing interface for manual control via CLI.***
*main - Main loop of the module
*move_to_1 - Moves mouse to location 1, with random delay.
*move_to_2 - Moves mouse to location 2, with random delay.
*move_to_3 - Moves mouse to location 3, with random delay.
*move_to_4 - Moves mouse to location 4, with random delay.
*click - Clicks the mouse on call, with random delay.
*action - Runs the sequence of events.
*find_path - Finds the end point to aim of the specified location.
*get_config - Method to locate and serialize config json.
*config_me - Method to run the config option logic.

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
import json
# the following are added to support PyInstaller builds
# noinspection PyUnresolvedReferences
import logging  # pylint: disable=unused-import
# noinspection PyUnresolvedReferences
import PIL  # pylint: disable=unused-import
# noinspection PyUnresolvedReferences
import pyscreeze  # pylint: disable=unused-import
# the following are custom modules related to this project
import pyautogui
import config_cli
import ep_exceptions as errors


def move_to_1(config):
    """
    Method to  move mouse to position 1.

    Position 1 is lower left hand corner by default, specifically the icon
    that has an 'i' character in a circle.

    :param config: (class) **Configuration object build from the config json file.**
    :rtype: **None**
    :return: **None**
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
    conf = config.get_config().get('search_confid')
    try:
        cord = (find_path(obj, conf))
        if cord is None:
            time.sleep(0.5)
            waited = True
            cord = (find_path(obj, conf))
        x_cord = cord[0]
        y_cord = cord[1]
    except TypeError:
        control = 1  # set flag value to 1 to skip cord_f errors
        errors.PathLockError(path_name, waited)
    delay = random.uniform(0.21, 0.29)
    pos_degrade = 0  # randrange(0, 3)
    try:
        if control == 1:
            # path adjusted based on old tune settings
            x_cord = config.get_config().get('p1_x') - pos_degrade + 8  # was 5
            y_cord = config.get_config().get('p1_y') - pos_degrade + 5  # was 3
        else:
            x_cord = x_cord - pos_degrade + 5
            y_cord = y_cord - pos_degrade + 3
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

    :param config: (class) **Configuration object build from the config json file.**
    :rtype: **None**
    :return: **None**
    """
    path_name = "Target 2"  # name of the path, used for execution logging
    x_cord = None
    y_cord = None
    control = 0  # flag variable if exception passed set to 1 before exception logging
    waited = False
    obj = "./graphics/p2_target_obj.png"
    conf = config.get_config().get('search_confid')
    try:
        cord = (find_path(obj, conf))
        if cord is None:
            time.sleep(0.5)
            waited = True
            cord = (find_path(obj, conf))
        x_cord = cord[0]
        y_cord = cord[1]
    except TypeError:
        control = 1  # set flag value to 1 to skip cord_f errors
        errors.PathLockError(path_name, waited)
    # movement time in seconds
    delay = random.uniform(0.21, 0.29)
    pos_degrade = 0  # randrange(0, 3)
    try:
        if control == 1:
            # path adjusted based on old tune settings
            x_cord = config.get_config().get('p2_x') - pos_degrade + 13  # was 10
            y_cord = config.get_config().get('p2_y') - pos_degrade + 18  # was 15
        else:
            x_cord = x_cord - pos_degrade + 10
            y_cord = y_cord - pos_degrade + 15
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

    :param config: (class) **Configuration object build from the config json file.**
    :rtype: **None**
    :return: **None**
    """
    path_name = "Target 3"  # name of the path, used for execution logging
    # movement time in seconds
    delay = random.uniform(0.21, 0.29)
    pos_degrade = randrange(0, 3)
    x_cord = config.get_config().get("p3_x") - pos_degrade
    y_cord = config.get_config().get("p3_y") - pos_degrade
    try:
        pyautogui.moveTo(x_cord, y_cord, delay)
    except pyautogui.PyAutoGUIException as error:
        errors.EPPyAutoGUILogError(path_name, error)


def move_to_4(config):
    """
    Method to move mouse to position 4.

    Position 4 is the upper right of center, and is specified by an x. This is the final movement
    of the script.

    :param config: (class) **Configuration object build from the config json file.**
    :rtype: **None**
    :return: **None**
    """
    path_name = "Target 4"  # name of the path, used for execution logging
    delay = random.uniform(0.21, 0.29)
    pos_degrade = randrange(0, 3)
    x_cord = config.get_config().get("p4_x") - pos_degrade
    y_cord = config.get_config().get("p4_y") - pos_degrade
    try:
        pyautogui.moveTo(x_cord, y_cord, delay)
    except pyautogui.PyAutoGUIException as error:
        errors.EPPyAutoGUILogError(path_name, error)


def click_local():
    """
    Method to click the mouse when at the required location using delays.

    :return: **None**
    """
    path_name = "local_click_function"
    delay = random.uniform(0.045, 0.065)
    time.sleep(delay)
    try:
        pyautogui.click()
    except pyautogui.PyAutoGUIException as error:
        errors.EPPyAutoGUILogError(path_name, error)


def action(config):
    """
    Method to run the sequence.

    :param config: (class) **Configuration object build from the config json file.**
    :return: **None**
    """
    de_pau = config.get_config().get("default_pause")
    pyautogui.PAUSE = config.get_config().get("py_a_gui_pause")
    move_to_1(config)
    time.sleep(de_pau)
    click_local()
    # path 2 slower to load, longer wait
    time.sleep(.55)
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

    :param config: (class) **Configuration object build from the config json file.**
    :return: **None**
    """
    print("Lets go")
    running = True
    while running is True:
        var = input("\nHit 1 to start, 5 to run config, 9 to exit.\n")
        if var == "1":
            action(config)
        elif var == "9":
            running = False
        elif var == "5":
            config_me("cmd")
        else:
            time.sleep(1)
            print("Waiting")


def find_path(obj, conf):
    """
    This Method will locate the coordinates for path 2.

    This Method calls the locate method from pyautogui, and returns the location of the
    target x and y coordinates.

    :param obj: (str) **String of the file path to the target object.**
    :param conf: (float) **Float of the percentage to use as confidence level to use.**
    :rtype: **tuple**
    :return: **cord**: The tuple of the x and y cord of the target object
    """
    path_name = "local_find_function"
    cord = None
    try:
        cord = pyautogui.locateOnScreen(obj, confidence=conf)
    except (pyautogui.ImageNotFoundException, pyautogui.PyAutoGUIException) as error:
        errors.EPPyAutoGUILogError(path_name, error)
    return cord


def get_config():
    """
    Method to get the configuration settings from a json file.

    :rtype: **dict**
    :return: **config**: A dictionary of the overall configuration settings for the program
    """
    try:
        with open("./config/config.json", 'r', encoding="utf-8") as file:
            config = json.load(file)
            return config
    except FileNotFoundError as error:
        errors.EnglishPleaseException(error)
        return None


def config_me(status):
    """
    Method to run the config option logic

    :return: **None**
    """
    try:
        config_obj = Config("config", get_config())  # create the config memory object
        if config_obj.get_config().get("config_required") or status == "cmd":
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
    except (FileNotFoundError, AttributeError) as error:
        errors.EnglishPleaseException(error)


class Config:
    """
    Class to define configuration items in memory.

    :return: **None**
    """

    def __init__(self, name, config):
        self.name = name
        self.config = config

    def get_name(self):
        """:return name (str): the name of the class"""
        return self.name

    def get_config(self):
        """:return config (dict): the config json dict of the class"""
        return self.config


def main():
    """Main Method of the program."""
    # config_obj = Config("config", get_config())  # create the config memory object
    # action(config_obj)
    try:
        # config_me("initial")
        config_obj = Config("config", get_config())  # create the config memory object
        # action(config_obj)
        test_interface(config_obj)
    except errors.EnglishPleaseException as error:
        errors.EnglishPleaseException(error)


if __name__ == "__main__":
    main()
