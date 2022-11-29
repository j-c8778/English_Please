"""
__filename__ = "ep_exceptions.py"
___author__ = "Jessie Campbell"
__copyright__ = "Jessie Campbell"
__credits__ = ["Jessie Campbell"]
__license__ = "MIT"
__version__ = "0.1.1"
__maintainer__ = "Jessie Campbell"
__email__ = "jessie.t.campbell@gmail.com"
__status__ = "Alpha"

Module with custom exception handlers and logging support for English_Please.

Uses the following functions:


Defines the following classes:
-EnglishPleaseException - Custom exception to catch and log errors.
-EPTypeError - Custom Error Handler for path lock failure.
-EPUnbound - Custom UnboundLocalError Handler
-EPPyAutoGUILogError - Custom method to produce logs for PyAutoGuiExceptions

Requires the following imports:
-time
-logging

***Also requires the following dependant packages:
-

Requires the following files to be present in the same directory as the module.
- logs - Folder to contain the logged information.
"""
import time
import logging
import pyautogui


class EnglishPleaseException(Exception):
    """
    Custom exception to catch and log errors.

    :argument error (obj): the error that occurred
    """
    now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())

    def __init__(self, error, e_time=now):
        self.error = error
        self.e_time = e_time
        self.print_error()

    def error_output(self):
        """method to construct the output string"""
        return f'{self.error} at {self.e_time}.'

    def print_error(self):
        """method to print the error to the output txt file"""
        error_path = "./logs/english_please_error_log.txt"
        logging.basicConfig(filename=error_path, filemode="a",
                            encoding="utf-8", level=logging.DEBUG, force=True)
        logging.log(logging.INFO, self.error_output(), stack_info=False)


class PathLockError(Exception):
    """
    Custom Error Handler for path lock failure.

    :argument path (str): the path that is being executed by the function
    :argument waited (bool): true if waited occurred, false otherwise
    """
    now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())

    def __init__(self, path, waited, e_time=now):
        self.e_time = e_time
        self.path = path
        self.waited = waited
        self.print_error()

    def error_output(self):
        """method to construct the output string"""
        return f'Did not find {self.path} on {self.e_time}, waited status was {self.waited}.'

    def print_error(self):
        """method to print the error to the output txt file"""
        error_path = "./logs/path_error_log.txt"
        logging.basicConfig(filename=error_path, filemode="a",
                            encoding="utf-8", level=logging.DEBUG, force=True)
        logging.log(logging.INFO, self.error_output(), stack_info=False)


class EPUnbound(Exception):
    """
    Custom UnboundLocalError Handler

    :argument path (str): the path the unbound error occurred on
    """
    now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())

    def __init__(self, path, e_time=now):
        self.e_time = e_time
        self.path = path
        self.print_error()

    def error_output(self):
        """method to construct the output string"""
        return f'UnboundLocalError while running {self.path} on {self.e_time}'

    def print_error(self):
        """method to print the error to the output txt file"""
        error_path = "./logs/path_error_log.txt"
        logging.basicConfig(filename=error_path, filemode="a",
                            encoding="utf-8", level=logging.DEBUG, force=True)
        logging.log(logging.INFO, self.error_output(), stack_info=False)


class EPPyAutoGUILogError(pyautogui.PyAutoGUIException):
    """
    Custom method to produce logs for PyAutoGuiExceptions.

    :argument path (str): the path the error occurred on
    :argument message (obj): the message of the error
    """
    now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())

    def __init__(self, path, message, e_time=now):
        self.path = path
        self.e_time = e_time
        self.message = message
        self.print_error()

    def error_output(self):
        """ Method to construct the output message for the log."""
        return f'{self.message} while running {self.path} on {self.e_time}'

    def print_error(self):
        """ Method to print the error to the output txt file"""
        error_path = "./logs/py_auto_gui_logs.txt"
        logging.basicConfig(filename=error_path, filemode="a",
                            encoding="utf-8", level=logging.DEBUG, force=True)
        logging.log(logging.INFO, self.error_output(), stack_info=False)
