import mysql.connector

mydb = mysql.connector.connect(
    user = "Mironshoh",
    password = "02072021Imron!",
    host = "127.0.0.1",
    database = 'studentdatabase'
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Student2(id INT PRIMARY KEY,name VARCHAR(50),birth_date VARCHAR(10),score  DOUBLE)")

mycursor.executemany("INSERT INTO Student2(id,name,birth_date,score) VALUES (%s ,%s, %s, %s)",[
    (1,'Miron', '2001-07-14', 90.0),
    (2,'Miron2', '2002-06-02', 45.0),
    (3,'Miron3', '2003-10-04', 40.0),
    (4,'Miron4', '2003-11-01', 40.0),
    (5,'Miron5', '2002-03-09', 85.0),
    (6,'Miron6', '2003-04-01', 60.0),
    (7,'Miron7', '2002-03-30', 95.0),
    (8,'Miron8', '2001-08-22', 55.0),
    (9,'Miron9', '2003-07-12', 70.0),
    (10,'Miron10', '2002-03-21', 10.0),
    (11,'Miron11', '2001-01-01', 30.0),
    (12,'Miron12', '2003-01-11', 40.0)
     ])

mydb.commit()
# FIRST TASK
mycursor.execute("SELECT * FROM Student2 WHERE score = 40.0")
sum = 0
for i in mycursor.fetchall():
    print(*i)


# SECOND TASK
mycursor.execute("""
                 SELECT * FROM Student2 
                 WHERE ((SUBSTRING(birth_date, 7, 1) = '1' AND SUBSTRING(birth_date, 6, 1) != '1') 
                 OR SUBSTRING(birth_date, 7, 1) = '2')
                 """)
for i in mycursor.fetchall():
    print(*i)

