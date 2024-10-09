import mysql.connector

mydb = mysql.connector.connect(
    user = "Mironshoh",
    password = "02072021Imron!",
    host="localhost",
    database="edfixdatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students")
print(mycursor.fetchone())
for i in mycursor.fetchmany(20):
    print(*i)
