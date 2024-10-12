import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Mironshoh",
    password="02072021Imron!",
    database="university"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS student (id INT, name VARCHAR(50),course INT,scholarship DOUBLE)")
# mycursor.executemany("""
#      INSERT INTO student VALUES (%s,%s,%s,%s)
#  """,[(1, 'Miron', 2, 1213),
# (2, 'Miron2', 4, 4569),
# (3, 'Miron3', 3, 4182), 
# (4, 'Miron4', 3, 2063), 
# (5, 'Miron5', 3, 1884), 
# (6, 'Miron6', 4, 3966), 
# (7, 'Miron7', 2, 1886), 
# (8, 'Miron8', 4, 4174), 
# (9, 'Miron9', 3, 1776), 
# (10, 'Miron10', 3, 1464), 
# (11, 'Miron11', 1, 2961), 
# (12, 'Miron12', 1, 2966), 
# (13, 'Vladimir', 4, 1062), 
# (14, 'Miron', 3, 4836), 
# (15, 'Miron2', 4, 4015), 
# (16, 'Vladimir', 2, 1656),])
# mydb.commit()
# mycursor.execute("DELETE FROM student WHERE course = 4")
# mycursor.execute("UPDATE student SET course = course+1 WHERE course<4")
mycursor.execute("SELECT * FROM student")
for row in mycursor.fetchall():
    print(*row)

print('\n')
mycursor.execute("SELECT * FROM student WHERE course=2")
for row in mycursor.fetchall():
    print(*row)
print('\n')
mycursor.execute("SELECT * FROM student WHERE course=3")
for row in mycursor.fetchall():
    print(*row)
print('\n')
mycursor.execute("SELECT * FROM student WHERE course=4")
for row in mycursor.fetchall():
    print(*row)