#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
import sys
sys.path.append(
    '/Users/mac/Documents/airBnB_clone_v2-merged/AirBnB_clone_v2/.venv/lib/python3.12/site-packages')

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
