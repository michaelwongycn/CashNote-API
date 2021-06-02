import sqlite3
import base64
from sqlite3.dbapi2 import Error

database_path = 'App_Data/Database/database.db'


def get_connection():
    try:
        connection = sqlite3.connect(database_path)
    except Error:
        connection = None
        print(Error)
    return connection


def encode(string):
    message_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def decode(string):
    base64_bytes = string.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message
