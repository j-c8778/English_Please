"""
__filename__ = "config_cli.py"
___author__ = "Jessie Campbell"
__copyright__ = "Jessie Campbell"
__credits__ = ["Jessie Campbell"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Jessie Campbell"
__email__ = "jessie.t.campbell@gmail.com"
__status__ = "Alpha"

Module that runs the configuration update CLI for the english_please.py module.

Uses the following functions:
*config_menu_control - Function to control which case gets called.
*case_1 - Function to 1 logic for screen resolution updating
*case_2 - Function to run case 2 logic to update path targets
*case_3 - Function to run case 3 logic to update pause times
*case_4
*case_5
*case_6
*menu_print

Requires the following imports:
-time
-logging
-json

Requires the following files to be present in the same directory as the module.
- config - Folder with the config.json file
- graphics - Folder with the p1_target_obj.png and p2_target_obj.png files
"""

import json
import time


def config_menu_control(mode):
    """Function to control the Configuration Menu
    :arguments mode (str): desired case from menu_print().
    """

    match mode:
        case "1":  # Change your current resolution setting.
            case_1()
        case "2":  # Change your tuning settings.
            case_2()
        case "3":  # Change the pause times.
            case_3()
        case "4":  # Change the path 3 and/or path 4 target locations.
            pass
        case "5":  # Change the current screen resolution.
            pass
        case "6":  # Reset to default configuration settings.
            pass
        case "9":  # exit case
            print("Thank you, goodbye.")
            time.sleep(0.75)
        case _:  # default to catch invalid choices
            print("Invalid Choice, please try again.\n")


def case_1():
    """Function to 1 logic for screen resolution updating"""
    print("Screen resolutions will be updated in two steps.\n")
    new_x = None
    new_y = None
    try:
        new_x = input("Enter the new resolution X value, then press enter:")
        new_y = input("Enter the new resolution y value, then press enter:")
    except TypeError:  # add error handling later
        print("Error, you must only enter a number 0-9999")
    with open("./config/config.json", 'r', encoding="utf-8") as file:
        data = json.load(file)
        data['res_x'] = new_x
        data['res_y'] = new_y


def case_2():
    """Function to run case 2 logic to update path targets"""
    try:
        path_sel = input("Type the path (1-4) to tune, and press enter.\n"
                         "Enter 5 to return to the menu.")
        while int(path_sel) != range(1 - 5):
            print("you must enter a value 1-5")
            path_sel = input("Type the path (1-4) to tune, and press enter.\n")
        try:
            if path_sel == "5":
                pass
            else:
                new_x = input(f"Enter the new X pixel path {path_sel}"
                              f" target, then press enter:")
                new_y = input(f"Enter the new X pixel path {path_sel} "
                              f"target, then press enter:")
                with open("./config/config.json", 'r', encoding="utf-8") as file:
                    data = json.load(file)
                    data['path_1_x_tune'] = new_x
                    data['path_1_y_tune'] = new_y
        except TypeError:  # add error handling later
            print("Error, you must only enter a number 0-9999")
    except TypeError:  # add error handling later
        print("Error, only numbers 1-5 are acceptable inputs")


def case_3():
    """Function to run case 3 logic to update pause times"""
    running = True
    while running:
        try:
            pause_sel = input("Type the path (1-4) to tune, and press enter.\n"
                              "Enter 5 to return to the menu.")
            while int(pause_sel) != range(1 - 5):
                print("you must enter a value 1-5")
                path_sel = input("Type the path (1-4) to tune, and press enter.\n")
                if path_sel == "5":
                    pass
            try:
                print("Note: The limit is 10 Seconds max Pause.\n")
                new_pause = input(f"Enter the new pause time for path {pause_sel},"
                                  f" then press enter:\n")
                try:
                    while float(new_pause) != range(1 - 10):
                        print("you must enter a number value 1-10")
                        new_pause = input(f"Enter the new pause time for path {pause_sel},"
                                          f" then press enter:")
                except TypeError:  # add error handling later
                    print("Invalid Entry.")
                with open("./config/config.json", 'r', encoding="utf-8") as file:
                    out_tar_str = "path_" + pause_sel + "_pause"
                    data = json.load(file)
                    data[out_tar_str] = new_pause
            except TypeError:  # add error handling later
                print("Error, you must only enter a number 0-10")
        except TypeError:  # add error handling later
            print("Error, only numbers 1-5 are acceptable inputs")


def case_4():
    """ -docstring- """


def case_5():
    """ -docstring- """


def case_6():
    """ -docstring- """


def menu_print():
    """Function to print the options menu"""

    print("Welcome to the English Please Configuration Menu\n"
          "Please enter the number for your desired selection, then press enter:\n"
          "\n1) Change your current resolution setting.\n"
          "2) Change your tuning settings.\n"
          "3) Change the pause times.\n"
          "4) Change the path 3 and/or path 4 target locations.\n"
          "5) Change the current screen resolution.\n"
          "6) Reset to default configuration settings.\n"
          "9) Exit the configuration menu.")


menu_print()
