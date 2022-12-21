"""
__filename__ = "config_cli.py"
___author__ = "Jessie Campbell"
__copyright__ = "Jessie Campbell"
__credits__ = ["Jessie Campbell"]
__license__ = "MIT"
__version__ = "0.1.2"
__maintainer__ = "Jessie Campbell"
__email__ = "jessie.t.campbell@gmail.com"
__status__ = "Alpha"

Module that contains functions to run the configuration update CLI for the english_please.py module.

Uses the following functions:
*menu_print - Function to print the configuration menu.
*config_menu_control - Function to control which case gets called.
*case_1 - Function to update full screen mode.
*case_2 - Function to run case 2 logic to update path targets.
*case_3 - Function to run case 3 logic to update pause times.
*case_4 - Function to change the path 3 and/or path 4 target locations.
*case_5 - Function to update the current screen resolution in the config file.
*case_6 - Function to reset to default configuration settings.

Requires the following imports:
-json
-pyautogui
-ep_exceptions
"""
import json
import pyautogui
import ep_exceptions as errors


def menu_print():
    """Function to print the options menu"""

    print("Welcome to the English Please Configuration Menu\n"
          "Please enter the number for your desired selection, then press enter:\n"
          "\n1) Enable/Disable full screen mode.\n"
          "2) Change your tuning settings.\n"
          "3) Change the pause times.\n"
          "4) Change the path 3 and/or path 4 target locations.\n"
          "5) Update the current screen resolution.\n"
          "6) Reset to default configuration settings.\n"
          "9) Exit the configuration menu"
          " (sets config status to False, manual reset only"
          " in the json file until future revision).")


def config_menu_control(mode):
    """Function to control the Configuration Menu
    :arguments mode (str): desired case from menu_print()
    """
    match mode:
        case "1":  # Enable/Disable full screen mode.
            case_1()
        case "2":  # Change your tuning settings.
            case_2()
        case "3":  # Change the pause times.
            case_3()
        case "4":  # Change the path 3 and/or path 4 target locations.
            case_4()
        case "5":  # Update the current screen resolution in the config file.
            case_5()
        case "6":  # Reset to default configuration settings.
            case_6()
        case "9":  # exit case
            return False
        case _:  # default to catch invalid choices
            print("Invalid Choice, please try again.\n")


def case_1():
    """Function to enable/disable full screen mode."""
    print("Full Screen Mode is not yet supported, this function will now exit\n")


def case_2():
    """Function to run case 2 logic to update path targets"""
    path_sel = None
    try:
        path_sel = int(input("Type the path (1-4) to tune, and press enter.\n"
                             "Enter 5 to return to the menu."))
        # while path_sel not in range(1, 6, 1):
        #     print("you must enter a value 1-4")
        #     path_sel = int(input("Type the path (1-4) to tune, and press enter.\n"))
        #     print(path_sel)
        #     print(type(path_sel))
        #     if path_sel in range(1, 6, 1):
        #         print(path_sel)
        #         break
    except TypeError:
        print("Error, only numbers 1-5 are acceptable inputs")

    try:
        if path_sel == 5:
            print("Ok")
        elif path_sel != 5:
            new_x = int(input(f"Enter the new X pixel path {path_sel}"
                              f" target, then press enter:"))
            new_y = int(input(f"Enter the new Y pixel path {path_sel} "
                              f"target, then press enter:"))
            try:
                with open("./config/config.json", 'r', encoding="utf-8") as file:
                    data = json.load(file)
                    data['path_1_x_tune'] = new_x
                    data['path_1_y_tune'] = new_y
                with open("./config/config.json", 'w', encoding="utf-8") as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError as error:
                errors.EPConfigError(error)
                print("Config file not found, recopy from repo, or contact Author.")
    except TypeError as error:
        print("Error, you must only enter a number 0-9999")
        print(error)


def case_3():
    """Function to run case 3 logic to update pause times"""
    running = True
    while running:
        try:
            pause_sel = int(input("Type the path (1-4) to tune, and press enter.\n"
                                  "Enter 5 to return to the menu."))
            while int(pause_sel) != range(1 - 5):
                print("you must enter a value 1-5")
                path_sel = int(input("Type the path (1-4) to tune, and press enter.\n"))
                if path_sel == "5":
                    pass
            try:
                print("Note: The limit is 10 Seconds max Pause.\n")
                new_pause = float(input(f"Enter the new pause time for path {pause_sel},"
                                        f" then press enter:\n"))
                try:
                    while float(new_pause) != range(1 - 10):
                        print("you must enter a number value 1-10")
                        new_pause = input(f"Enter the new pause time for path {pause_sel},"
                                          f" then press enter:")
                except TypeError:
                    print("Invalid Entry, numbers 1-10 only.")
                try:
                    with open("./config/config.json", 'r', encoding="utf-8") as file:
                        out_tar_str = "path_" + str(pause_sel) + "_pause"
                        data = json.load(file)
                        data[out_tar_str] = new_pause
                    with open("./config/config.json", 'w', encoding="utf-8") as file:
                        json.dump(data, file, indent=4)
                except FileNotFoundError as error:
                    errors.EPConfigError(error)
                    print("Config file not found, recopy from repo, or contact Author.")
            except TypeError:
                print("Error, you must only enter a number 0-10")
        except TypeError:
            print("Error, only numbers 1-5 are acceptable inputs")


def case_4():
    """Function to change the path 3 and/or path 4 target locations."""

    def path_3():
        """Function to update path 3"""
        input("Position your mouse on the path 3 target (using actual tube ad),"
              "then press enter.")
        path_3_x_cord, path_3_y_cord = pyautogui.position()
        print("Your new x and y coordinates are: " + str(path_3_x_cord) +
              ", " + str(path_3_y_cord))
        print("\nRe-preform this function if that is not correct.")
        try:
            with open("./config/config.json", 'r', encoding="utf-8") as file3:
                data = json.load(file3)
                data[path_3_x_cord] = path_3_x_cord
                data[path_3_y_cord] = path_3_y_cord
            with open("./config/config.json", 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError as error:
            errors.EPConfigError(error)
            print("Config file not found, recopy from repo, or contact Author.")

    def path_4():
        """Function to update path 4"""
        input("Position your mouse on the path 4 target (using actual tube ad),"
              "then press enter.")
        path_4_x_cord, path_4_y_cord = pyautogui.position()
        print("Your new x and y coordinates are: " + str(path_4_x_cord) +
              ", " + str(path_4_y_cord))
        print("\nRe-preform this function if that is not correct.")
        try:
            with open("./config/config.json", 'r', encoding="utf-8") as file4:
                data = json.load(file4)
                data[path_4_x_cord] = path_4_x_cord
                data[path_4_y_cord] = path_4_y_cord
            with open("./config/config.json", 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError as error:
            errors.EPConfigError(error)
            print("Config file not found, recopy from repo, or contact Author.")

    try:
        sel = int(input("Type 3 to update path 3, 4 to update path 4, 9 to update both,"
                        " then press Enter."))
        if sel == 3:
            path_3()
        elif sel == 4:
            path_4()
        elif sel == 9:
            input("Press enter to update path 3")
            path_3()
            input("Press enter to update path 4")
            path_4()
    except TypeError:
        print("Invalid Entry, number values for x and y coordinates only.")


def case_5():
    """Function to update the current screen resolution in the config file."""
    res_x, res_y = pyautogui.size()
    print("Your screen resolution is: " + str(res_x) + "x" + str(res_y))
    try:
        sel = input("If this is correct, type Y and hit enter, if not,"
                    " type N and hit enter to set manually.")
        if sel.lower() == "y":
            print("Config File updated.")
        elif sel.lower() == "n":
            res_x = int(input("Type your x axis size and hit enter."))
            res_y = int(input("Type your y axis size and hit enter."))
            try:
                with open("./config/config.json", 'r', encoding="utf-8") as file:
                    data = json.load(file)
                    data[res_x] = res_x
                    data[res_y] = res_y
                with open("./config/config.json", 'w', encoding="utf-8") as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError as error:
                errors.EPConfigError(error)
                print("Config file not found, recopy from repo, or contact Author.")
    except TypeError:
        print("Invalid Entry,, Y or N only.")


def case_6():
    """Function to reset to default configuration settings."""
    input("Warning, you are about to reset the config file to default, press enter to continue.")
    try:
        sel = input("Type Y to reset to default, Type N to exit this function, the press enter.")
        if sel.lower() == "y":
            with open("./config/config_default.json", 'r', encoding="utf-8") as file:
                data = json.load(file)
            with open("./config/config.json", 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        elif sel.lower() == "n":
            print("Returning to main menu.")
        else:
            print("Invalid Entry.")
    except TypeError:
        print("Invalid Entry, Y or N only.")
    except FileNotFoundError as error:
        errors.EPConfigError(error)
        print("Config file not found, recopy from repo, or contact Author.")
