import mysql.connector
from tkinter import *
from tkinter import ttk
from functools import partial
jobList = []
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="sukantahui",
    database='ses_gold'
)
# on change dropdown value
def changeJobChoosen(*args):
    print(jobSelected.get())
def getJobIdList(x):
  print("function calling")
  print(x.get())
  myCursor = mydb.cursor(dictionary=True)
  sql = "select * from job_master where order_id = %s"
  order = ("papai/92/2021",)
  myCursor.execute(sql, order)
  myResult = myCursor.fetchall()
  for x in myResult:
    # print(x['job_id'])
    jobList.append(x['job_id'])
  print("job list")
  print(jobList)
  create_job_drop_down()




window = Tk()
window.geometry("600x250")
mainframe = Frame(window)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)
#order number
orderNumber = StringVar()
Label(mainframe, text="Order Number").grid(row=1, column=1)
orderNumberTextBox = Entry(mainframe,textvariable=orderNumber).grid(row=1, column=2)
getJobListIdsPartial = partial(getJobIdList,orderNumber)
submitOrderNumberBtn = Button(mainframe, text="Submit",command=getJobListIdsPartial, activebackground="pink", activeforeground="blue").grid(row=1, column=4)
Label(mainframe, text="Job ID").grid(row=2, column=1)
jobSelected = StringVar()
jobChoosen = ttk.Combobox(mainframe, width=15, textvariable=jobSelected)
def create_job_drop_down():
  # Adding combobox drop down list
  jobChoosen['values'] = jobList
  jobChoosen.grid(column=2, row=2)
  jobChoosen.current()
  jobSelected.trace('w', changeJobChoosen)
mainloop()
Mon 10:04 AM
import mysql.connector
import time
import json
from mysql.connector import Error
try:
    with open('database.json') as f:
        database = json.load(f)

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

        time.sleep(5)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")