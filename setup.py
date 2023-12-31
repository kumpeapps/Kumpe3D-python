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

import_or_install("infisical")
import_or_install("easygui")
import_or_install("beepy")
import_or_install("pymysql")
import_or_install("dotenv", "python-dotenv")
