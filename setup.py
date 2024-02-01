"""Install missing modules"""
import pip


def import_or_install(module, package = None):
    """install module if unable to import"""
    if package is None:
        package = module
    try:
        __import__(module)
    except ImportError:
        pip.main(['install', package])

import_or_install("infisical", "infisical==1.5.0")
import_or_install("easygui")
import_or_install("beepy")
import_or_install("pymysql")
import_or_install("pyppeteer")
import_or_install("dotenv", "python-dotenv")
import_or_install("flet")
import_or_install("requests")
