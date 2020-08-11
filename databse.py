import json

import mysql.connector
from mysql.connector import Error

with open('database.json') as f:
    database = json.load(f)
connection_config_dict = {
    'user': database['user'],
    'password': database['password'],
    'host': database['host'],
    'database': database['database'],
    'raise_on_warnings': True,
    'use_pure': False,
    'autocommit': True,
    'pool_size': 5
}


def databaseConnection():
    x = mysql.connector.connect(**connection_config_dict)
    return x


def get_connection_error_message(e):
    if e.errno == 1045:
        return "User name or password is incorrect"
    elif e.errno == 1049:
        return "Check the database name"
    elif e.errno == 2003:
        return "Check server name"
    else:
        return "Unknown error"
