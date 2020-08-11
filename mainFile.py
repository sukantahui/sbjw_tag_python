import temp
# working
import mysql.connector
import time
import json
import databse
from mysql.connector import Error

try:

    # load mysql connector        python -m pip install mysql-connector-python
    connection = databse.databaseConnection()
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        person = '{"name": "Bob", "languages": ["English", "Fench"]}'
        person_dict = json.loads(person)
        print(person_dict)

        program = 'TOUSB.exe'
        arguments = 'database.json'
        # subprocess.call([program, arguments])
        f = open("guru99.txt", "w+")
        for i in range(10):
            f.write("This is line %d\r\n" % (i + 1))
        f.close()
        temp.print_world()
        time.sleep(5)
except Error as e:
    # print("Error while connecting to MySQL",e)
    msg = 'Failure in connecting to database. Error: {0}'.format(e)
    print(msg)
    # print(e.errno)
    print(databse.get_connection_error_message(e))
# finally:
# if (connection.is_connected()):
#     cursor.close()
#     connection.close()
#     print("MySQL connection is closed")
