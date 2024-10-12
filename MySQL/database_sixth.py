import mysql.connector

mydb = mysql.connector.connect(
    user = "Mironshoh",
    password = "02072021Imron!",
    host = "127.0.0.1",
    database = 'studentdatabase'
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS student4(id INT,name VARCHAR(50),birth_date VARCHAR(10),score  DOUBLE)")

mycursor.executemany("INSERT INTO student4 (id,name,birth_date,score) VALUES (%s ,%s, %s, %s)",[
    (1,'Miron', '2001-07-14', 90.0),
    (2,'Miron2', '2002-06-02', 45.0),
    (3,'Miron3', '2003-10-04', 97.0),
    (4,'Miron4', '2003-11-01', 40.0),
    (5,'Miron5', '2002-03-09', 85.0),
    (6,'Miron6', '2003-04-01', 61.0),
    (7,'Miron7', '2002-03-30', 95.0),
    (8,'Miron8', '2001-08-22', 53.0),
    (9,'Miron9', '2003-07-12', 75.0),
    (10,'Miron10', '2002-03-21', 60.0),
    (11,'Miron11', '2001-01-01', 79.0),
    (12,'Miron12', '2003-01-11', 85.0),
    (13,'Miron8', '2001-08-22', 55.0),
    (14,'Miron9', '2003-07-12', 74.0),
    (15,'Miron10', '2002-03-21', 100.0),
    (16,'Miron11', '2001-01-01', 93.0),
    (17,'Miron12', '2003-01-11', 80.0)
     ])

mydb.commit()
# FIRST TASK
# mycursor.execute("""
# UPDATE student4 SET id = id + 1 WHERE id % 2=0 
# """)
# mydb.commit()

mycursor.execute("SELECT * FROM student4 WHERE score < 100 AND score >= 90 ORDER BY name ASC")
for i in mycursor.fetchall():
    print(*i)
print("**********************************************")
mycursor.execute("SELECT * FROM student4 WHERE score < 90 AND score >= 70 ORDER BY birth_date DESC")
for i in mycursor.fetchall():
    print(*i)
print("**********************************************")
mycursor.execute("SELECT * FROM student4 WHERE score < 70 AND score >= 60 ORDER BY score ASC")
for i in mycursor.fetchall():
    print(*i)


