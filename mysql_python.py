import mysql.connector
import time
myDB= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="Python"
    )

print(myDB)

#Creating Database..
myCursor=myDB.cursor()
print("Tables present in Python Database :")
myCursor.execute("Show tables")

results = myCursor.fetchall()

print(results)

#ask if user wants to delete any existing table.....
ask=input("Do you want to drop any table : ")
if ask=="y" or ask=="Y":
    ask1=input("Name of the table :")
    myCursor.execute("Drop table "+ask1)
    
#ask user to create a new table...
create=input("Do you want to create a new table : ")
if create=="y" or create=="Y":
    tablename=input("Enter the name for new table:")

    results_lists = [item[0] for item in results]
    if tablename in results_lists:
        print(tablename," already exists")
    else:
        myCursor.execute("Create table "+ tablename+"(Name varchar(10),age integer);")
        print("\nTable Created")

    time.sleep(1)

    myCursor.execute("Show tables")
    print("Tables in python database:")
    results = myCursor.fetchall()
    for x in results:
        print(x)

else:
    print("\n\t\tThank You!")
time.sleep(1)



