import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Mironshoh",
    password="02072021Imron!",
    database = 'BOZOR'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS BOZOR")
mycursor.execute("CREATE TABLE IF NOT EXISTS fruit(id INT, name VARCHAR(50),cost DOUBLE,type VARCHAR(50))")
# mycursor.executemany("INSERT INTO fruit (id, name, cost, type) VALUES (%s,%s,%s,%s)",[
    # (1, 'Apple', 0.75, 'Pome'),
    # (2, 'Banana', 0.50, 'Berry'),
    # (3, 'Orange', 1.00, 'Citrus'),
    # (4, 'Grapes', 2.00, 'Berry'),
    # (5, 'Pineapple', 3.00, 'Tropical'),
    # (6, 'Strawberry', 1.50, 'Berry'),
    # (7, 'Mango', 2.50, 'Tropical'),
    # (8, 'Kiwi', 1.25, 'Berry'),
    # (9, 'Pear', 0.80, 'Pome'),
    # (10, 'Watermelon', 5.00, 'Melon'),
#     (11, 'Strawberry', 1.50, 'Berry'),
#     (12, 'Mango', 2.50, 'Tropical'),
#     (13, 'Kiwi', 1.25, 'Berry'),
#     (14, 'Pear', 0.80, 'Pome'),
#     (15, 'Watermelon', 5.00, 'Melon'),
# ])
# mydb.commit()

mycursor.execute("""
    DELETE f2
    FROM FRUIT f2
    JOIN FRUIT f1
    ON f1.id < f2.id
    AND f1.name = f2.name 
    AND f1.cost = f2.cost
    AND f1.type = f2.type 
""")
mydb.commit()

mycursor.execute("SELECT * FROM FRUIT ORDER BY COST DESC")
for row in mycursor.fetchmany(5):
    print(*row,sep=",")

