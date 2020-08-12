import temp
from tkinter import *
from tkinter import ttk
# working
import mysql.connector
import time
import json
import databse
from mysql.connector import Error

gray = ('#AFABAB', '#A29F9F', '#807E7E')
yellow = ('#F9C872', '#FAC66A')
white = ('#FAFAF0', '#FBFBEB')

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
        # time.sleep(5)
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

print("Working area")
root = Tk()
# root.geometry("1350x650")
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(1350, 650))

# create all of the main containers
top_frame = Frame(root, bg=yellow[0], pady=3, padx=50,height=100)
top_frame.grid_propagate(0)
center_frame = Frame(root, bg=gray[0], borderwidth=1)
btm_frame = Frame(root, bg='white', width=1350, height=45, pady=3)
btm_frame2 = Frame(root, bg='green', width=1350, height=60, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center_frame.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
# btm_frame2.grid(row=4, sticky="ew")

# create the widgets for the top frame
model_label = Label(top_frame, text='Model Dimensions')
width_label = Label(top_frame, text='Width:')
length_label = Label(top_frame, text='Length:')
entry_W = Entry(top_frame, background="pink")
entry_L = Entry(top_frame, background="orange")

# layout the widgets in the top frame
model_label.grid(row=0, columnspan=3)
width_label.grid(row=1, column=0)
length_label.grid(row=1, column=2)
entry_W.grid(row=1, column=1)
entry_L.grid(row=1, column=3)

# create the center widgets
center_frame.grid_rowconfigure(0, weight=1)
center_frame.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center_frame, bg=gray[0], width=200)
ctr_mid = Frame(center_frame, bg=white[0], padx=0, pady=0)
# ctr_right = Frame(center_frame, bg='green', width=100, padx=3, pady=3)
ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
# ctr_right.grid(row=0, column=2, sticky="ns")


btn_column = Button(ctr_mid, text="I'm in column 3")
btn_column.grid(column=3)

btn_columnspan = Button(ctr_mid, text="I have a columnspan of 3")
btn_columnspan.grid(columnspan=3)

btn_ipadx = Button(ctr_mid, text="ipadx of 4")
btn_ipadx.grid(ipadx=4)

btn_ipady = Button(ctr_mid, text="ipady of 4")
btn_ipady.grid(ipady=4)

btn_row = Button(ctr_mid, text="I'm in row 2")
btn_row.grid(row=2)

btn_rowspan = Button(ctr_mid, text="Rowspan of 2")
btn_rowspan.grid(rowspan=2)

btn_sticky = Button(ctr_mid, text="I'm stuck to north-east")
btn_sticky.grid(sticky=NE)

mainloop()
