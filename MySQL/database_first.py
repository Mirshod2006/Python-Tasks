import mysql.connector

mydb = mysql.connector.connect(
    user = "Mironshoh",
    password = "02072021Imron!",
    host = "127.0.0.1",
    database = 'studentdatabase'
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Student(id INT PRIMARY KEY,name VARCHAR(50),scholarship DOUBLE,course INT)")
# mycursor.executemany("INSERT INTO  Student(id ,name ,scholarship ,course ) VALUES (%s, %s, %s, %s)",[
#     ('1','Mironshoh','3000','4'),
#     ('2','Shohruh','2000','1'),
#     ('3','Dmitry','2000','2'),
#     ('4','Dilshod','2500','3'),
#     ('5','Mirshod','2000','2'),
#     ('6','Ali','2500','3'),
#     ('7','Mercury','3000','4'),
#     ('8','Thor','2500','3'),
#     ('9','Lyk','2000','2'),
#     ('10','Mark','3000','4'),
# ])
# mydb.commit()


# FIRST TASK
mycursor.execute("SELECT * FROM Student WHERE course=2")
sum = 0
for i in mycursor.fetchall():
    sum += i[2]
    print(i[2])
print(f"Sum Scholarship of Second Course Students: {sum}")


# SECOND TASK
mycursor.execute("SELECT * FROM Student WHERE  LENGTH(name) < 5 ORDER BY course DESC")
for i in mycursor.fetchall():
    print(*i)

