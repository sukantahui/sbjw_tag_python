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
