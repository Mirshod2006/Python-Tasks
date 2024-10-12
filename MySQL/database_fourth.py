import mysql.connector

mydb = mysql.connector.connect(
    user = "Mironshoh",
    password = "02072021Imron!",
    host = "127.0.0.1",
    database = 'studentdatabase'
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Student2(id INT PRIMARY KEY,name VARCHAR(50),birth_date VARCHAR(10),score  DOUBLE)")

# mycursor.executemany("INSERT INTO Student2(id,name,birth_date,score) VALUES (%s ,%s, %s, %s)",[
#     (1,'Miron', '2001-07-14', 90.0),
#     (2,'Miron2', '2002-06-02', 45.0),
#     (3,'Miron3', '2003-10-04', 40.0),
#     (4,'Miron4', '2003-11-01', 40.0),
#     (5,'Miron5', '2002-03-09', 85.0),
#     (6,'Miron6', '2003-04-01', 60.0),
#     (7,'Miron7', '2002-03-30', 95.0),
#     (8,'Miron8', '2001-08-22', 55.0),
#     (9,'Miron9', '2003-07-12', 70.0),
#     (10,'Miron10', '2002-03-21', 10.0),
#     (11,'Miron11', '2001-01-01', 30.0),
#     (12,'Miron12', '2003-01-11', 40.0)
#      ])

# mydb.commit()
# FIRST TASK
mycursor.execute("""
SELECT s.*
FROM Student2 s
JOIN (
    SELECT name
    FROM Student2
    GROUP BY name
    HAVING COUNT(name) > 1
) duplicates ON s.name = duplicates.name;

""")
sum = 0
for i in mycursor.fetchall():
    print(*i)

print("\n")
print("##################################################################################")
print("\n")
# SECOND TASK
mycursor.execute("""
                 SELECT * FROM student2 
                 WHERE MONTH(BIRTH_DATE)=2 AND score > 80
                 """)
for i in mycursor.fetchall():
    print(*i)

