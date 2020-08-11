import temp
# working
import mysql.connector
import time
import json
from mysql.connector import Error

try:
    with open('database.json') as f:
        database = json.load(f)

    # load mysql connector        python -m pip install mysql-connector-python
    connection = mysql.connector.connect(host=database['host'],
                                         database=database['database'],
                                         user=database['user'],
                                         password=database['password'])

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
    if e.errno == 1045:
        print("User name or password is incorrect")
    elif e.errno == 1049:
        print("Check the database name")
    elif e.errno == 2003:
        print("Check server name")
    else:
        print("Unknown error")
# finally:
# if (connection.is_connected()):
#     cursor.close()
#     connection.close()
#     print("MySQL connection is closed")
