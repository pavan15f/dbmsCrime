import mysql.connector


mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="123vittal",
    database='project'
)
 
mycurser = mydb.cursor()




mycurser.execute("show tables")
dbs = mycurser

for db in dbs:
    print(db)

