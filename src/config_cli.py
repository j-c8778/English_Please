"""
__filename__ = "config_cli.py"
___author__ = "Jessie Campbell"
__copyright__ = "Jessie Campbell"
__credits__ = ["Jessie Campbell"]
__license__ = "MIT"
__version__ = "0.1.4"
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
          "2) Change the path 3 and/or path 4 target locations.\n"
          "3) Update the current screen resolution.\n"
          "4) Reset to default configuration settings.\n"
          "9) Exit the configuration menu")


def config_menu_control(mode):
    """Function to control the Configuration Menu
    :arguments mode (str): desired case from menu_print()
    """
    match mode:
        case "1":  # Enable/Disable full screen mode.
            case_1()
        case "2":  # Change the path 3 and/or path 4 target locations.
            case_2()
        case "3":  # Update the current screen resolution in the config file.
            case_3()
        case "4":  # Reset to default configuration settings.
            case_4()
        case "9":  # exit case
            return False
        case _:  # default to catch invalid choices
            print("Invalid Choice, please try again.\n")


def case_1():
    """Function to enable/disable full screen mode."""
    print("Full Screen Mode is not yet supported, this function will now exit\n")


def case_2():
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


def case_3():
    """Function to update the current screen resolution in the config file."""
    try:
        with open("./config/config.json", 'r', encoding="utf-8") as file:
            data = json.load(file)
            c_res = data.get("active_res")
            print("Current Resolution is set at: " + c_res)
            choice = input("To change this, type Y or"
                           " to keep this setting type N,"
                           " then hit enter.")
            if choice.lower() == "y":
                choice2 = data.get("res_1")
                choice3 = data.get("res_2")
                choice4 = input(f"Type the resolution you want, {choice2} or {choice3}")
                if choice4 == choice2:
                    data["active_res"] = choice2
                    data["p1_x"] = data["p1_1920x1080_x"]
                    data["p1_y"] = data["p1_1920x1080_y"]
                    data["p2_x"] = data["p2_1920x1080_x"]
                    data["p2_y"] = data["p2_1920x1080_y"]
                    data["p3_x"] = data["p3_1920x1080_x"]
                    data["p3_y"] = data["p3_1920x1080_y"]
                    data["p4_x"] = data["p4_1920x1080_x"]
                    data["p4_y"] = data["p4_1920x1080_y"]
                elif choice4 == choice3:
                    data["active_res"] = choice3
                    data["p1_x"] = data["p1_1680x1050_x"]
                    data["p1_y"] = data["p1_1680x1050_y"]
                    data["p2_x"] = data["p2_1680x1050_x"]
                    data["p2_y"] = data["p2_1680x1050_y"]
                    data["p3_x"] = data["p3_1680x1050_x"]
                    data["p3_y"] = data["p3_1680x1050_y"]
                    data["p4_x"] = data["p4_1680x1050_x"]
                    data["p4_y"] = data["p4_1680x1050_y"]
                else:
                    print(f"You did not type in a valid resolution,"
                          f" only {choice2} or {choice3} are supported currently.")
            else:
                print("Retaining active resolution.")
        with open("./config/config.json", 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError as error:
        errors.EPConfigError(error)
        print("Config file not found, recopy from repo, or contact Author.")
    except TypeError:
        print("Invalid entry type.")


def case_4():
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
