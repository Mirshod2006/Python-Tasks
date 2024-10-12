import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Mironshoh",
    password="02072021Imron!",
    database = "milliy_taomlar"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS dish (id INT, name VARCHAR(50),ingredient VARCHAR(100))")
# mycursor.executemany("INSERT INTO dish  VALUES (%s,%s,%s)",[
# (1,'Pizza',        'Classic pepperoni pizza with tomato sauce and mozzarella cheese.'),
# (2,'Caesar Salad', 'Crisp romaine lettuce, croutons, Parmesan cheese, and Caesar dressing.'),
# (3,'Cheeseburger', 'Juicy beef patty with cheese, lettuce, tomato, and pickles on a bun.'),
# (4,'Chocolate Brownie', 'Decadent chocolate brownie with vanilla ice cream.')])
# # Commit your changes
# mydb.commit()

mycursor.execute("SELECT * FROM dish WHERE SUBSTRING(name,LENGTH(name),1)='a'")
for row in mycursor.fetchall():
    print(*row)

print("\n")

mycursor.execute("""SELECT * FROM dish WHERE LOCATE("tomato",ingredient)""")
for row in mycursor.fetchall():
    print(*row)

print("\n")

mycursor.execute("""SELECT * FROM dish WHERE ingredient LIKE '%tomato%'""")
for row in mycursor.fetchall():
    print(*row)