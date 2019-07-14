import sqlite3
import sys
from config import Config

def open_database(config=None, database_file=None):
    if database_file is None and config is None:
        raise Exception('Either the config object or the database file must be passed.')
    if database_file is None:
        database_file = config.database_file
    db = sqlite3.connect(database_file)
    script = open('db/database.sql', 'r').read()
    db.cursor().executescript(script)
    db.commit()
    return db
