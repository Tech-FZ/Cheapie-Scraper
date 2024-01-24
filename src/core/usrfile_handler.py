import platform
import os

def chromeFileDir():
    usrname = os.getlogin()

    if platform.system() == "Windows":
        chromedir = f"C:\\Users\\{usrname}\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"

    elif platform.system() == "macOS":
        chromedir = "Not supported"

    else:
        chromedir = f"/home/{usrname}/.config/google-chrome/Profile 1"

    return chromedir

def chromeExeDir():
    if platform.system() == "Windows":
        chromedir = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    elif platform.system() == "macOS":
        chromedir = "Not supported"

    else:
        chromedir = "/opt/google/chrome/google-chrome"

    return chromedir