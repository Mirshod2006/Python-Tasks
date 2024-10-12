import mysql.connector

mydb = mysql.connector.connect(
    user = "Mironshoh",
    password = "02072021Imron!",
    host = "127.0.0.1",
    database = "computerdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS  computerdatabase")
mycursor.execute("CREATE TABLE IF NOT EXISTS Computer(id INT PRIMARY KEY,model VARCHAR(50),cost  DOUBLE)")
mycursor.execute("""
                 CREATE TABLE IF NOT EXISTS computer_feature
                 (gpu INT ,
                 processor VARCHAR(20),
                 ram INT, 
                 computer_id INT,
                 screen_size  VARCHAR(20), 
                 FOREIGN KEY (computer_id) REFERENCES Computer(id))
                 """)

# mycursor.executemany("INSERT INTO Computer (id, model, cost) VALUES(%s,%s,%s)",
# [(1, 'Dell XPS 13', 1000.0),
#   (2, 'MacBook Pro 16', 2000.0),
#   (3, 'Lenovo ThinkPad X1 Carbon', 1500.0),
#   (4, 'HP Pavilion ', 900.0),
#   (5, 'MacBook Pro M3', 2000.0),
#   (6, 'Lenovo IdeaPad 5 Pro', 800.0),
#   (7, 'Asus Zenbook 14', 700.0),
#   (8, 'MacBook Air M1', 800.0),
#   (9, 'HP Victus', 750.0),]
# )

# mycursor.executemany("INSERT INTO computer_feature (gpu, processor, ram, computer_id, screen_size) VALUES (%s,%s,%s,%s,%s)",
# [
# (4, 'Intel Core i7', 16, 1, '13.3'),
# (8, 'Apple M1 Pro', 32, 2, '16'),
# (0, 'Intel Core i5', 8, 3, '15'),
# (6, 'Intel Core i7', 16, 4, '15.6'),
# (4, 'Apple M1 Pro', 32, 5, '16'),
# (4, 'Intel Core i5', 8, 6, '14'),
# (8, 'Intel Core i7', 16, 7, '13.3'),
# (0, 'Apple M1 Pro', 32, 8, '16'),
# (6, 'Intel Core i5', 8, 9, '14'),]
# )
# mydb.commit()

# FIRST TASK
mycursor.execute("SELECT * FROM computer JOIN computer_feature ON (computer.id = computer_feature.computer_id AND computer_feature.gpu = 0)")
# mycursor.execute("SELECT * FROM computer_feature WHERE gpu=0")
for i in mycursor.fetchall():
    print(i)


# # SECOND TASK
mycursor.execute("""
                 UPDATE computer SET model ='Dell XPS 13'  WHERE (SUBSTRING(model, 1, 1) = 'A' OR SUBSTRING(model, 1, 1) = 'a') OR cost = 800 
                 """)

mycursor.execute("SELECT * FROM computer JOIN computer_feature ON (computer.id = computer_feature.computer_id)")
for i in mycursor.fetchall():
    print(*i)

