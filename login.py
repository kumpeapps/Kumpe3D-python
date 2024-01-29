"""Kumpe3D Kiosk Login"""
import setup # pylint: disable=unused-import, wrong-import-order
import os
from dotenv import load_dotenv
from gui import gui
from params import Params

load_dotenv()
userid = os.getenv(key= "USERID", default= "")

def load():
    """Initial Load"""
    if userid == "0":
        Params.Access.set_access_level("basic")
        gui()
    else:
        print("no")


if __name__ == "__main__":
    load()
