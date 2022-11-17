import json

def config_menu_control(mode):
    """Function to control the Configuration Menu
    :arguments mode (str): desired case from menu_print().
    """
   match mode:
    case "1":  # Change your current resoltuion setting.
        print("Screen resolutions will be updated in two steps.\n")
        try:
            new_x = input("Enter the new resolution X value, then press enter:")
            new_y = input("Enter the new resolution y value, then press enter:")
        except TypeError as error:
            print("Error, you must only enter a number 0-9999")
        with open("./config/config.json", 'r', encoding="utf-8") as file:
            file['res_x'] = new_x
            file['res_y'] = new_y
    case "2":  # Change your tuning settings.
        try:
            path_sel = input("Type the path (1-4) to tune, and press enter.\n"
            "Enter 5 to exit")
            while int(path_sel) != range(1-5):
                print("you must enter a value 1-5")
                    path_sel = input("Type the path (1-4) to tune, and press enter.\n"
            if path_sel == "9":
                return
            try:
                new_x = input(f"Enter the new X pixel path {path_sel} target, then press enter:")
                new_y = input(f"Enter the new X pixel path {path_sel} target, then press enter:")
                with open ("./config/config.json", 'r', encoding="utf-8") as file:
                    file['path_1_x_tune'] = new_x
                    file['path_1_y_tune'] = new_y
            except TypeError as error:
                print("Error, you must only enter a number 0-9999")
        except TypeError as error:
            print("Error, only numbers 1-5 are acceptable inputs")
    case "3":  # Change the pause times.
        running = True
        while running:
            try:
                pause_sel = input("Type the path (1-4) to tune, and press enter.\n"
                "Enter 5 to exit")
                while int(path_sel) != range(1-5):
                    print("you must enter a value 1-5")
                        path_sel = input("Type the path (1-4) to tune, and press enter.\n"
                if path_sel == "9":
                    return
                try:
                    print("Note: The limit is 10 Seconds max Pause.\n")
                    new_pause = input(f"Enter the new pause time for path {pause_sel}, then press enter:\n")
                    try:
                        while float(new_pause) != range(1-10):
                            print("you must enter a number value 1-10")
                            new_pause = input(f"Enter the new pause time for path {pause_sel}, then press enter:")
                    except TypeError as error:
                        print("Invalid Entry.")
                    with open ("./config/config.json", 'r', encoding="utf-8") as file:
                        out_tar_str = "path_" + pause_sel + "_pause"
                        file[out_tar_str] = new_pause
                except TypeError as error:
                    print("Error, you must only enter a number 0-10")
            except TypeError as error:
                print("Error, only numbers 1-5 are acceptable inputs")
    case "4":  # Change the path 3 and/or path 4 target locations.
        
    case "5":  # Change the current screen resolution.
        
    case "6":  # Reset to default configuration settings.
        
    case "9":  # exit case
        print("Thank you, goodbye.")
        time.sleep(0.75)
    case _:  # default to catch invalid choices
        print("Invalid Choice, please try again.\n")


def menu_print():
    """Function to print the options menu"""
    
    print("Welcome to the English Please Configuration Menu\n"
    "Please enter the number for your desired selection, then press enter:\n"
    "\n1) Change your current resoltuion setting.\n"
    "2) Change your tuning settings.\n"
    "3) Change the pause times.\n"
    "4) Change the path 3 and/or path 4 target locations.\n"
    "5) Change the current screen resolution.\n"
    "6) Reset to default configuration settings.\n"
    "9) Exit the configuration menu.")

def update_config(mode):
    """Function to update the configuration JSON file"""
    
    pass

menu_print()
