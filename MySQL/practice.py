import mysql.connector

mydb = mysql.connector.connect(
    user = "Mironshoh",
    password = '02072021Imron!',
    host = 'localhost',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute("CREATE TABLE IF NOT EXISTS person (id INT PRIMARY KEY, name VARCHAR(64))")
mycursor.execute("CREATE TABLE IF NOT EXISTS thing (id INT PRIMARY KEY, name VARCHAR(64))")
mycursor.execute("""
                 CREATE TABLE IF NOT EXISTS owns (
                 person INT,
                 thing INT,
                 FOREIGN KEY (person) REFERENCES person(id),
                 FOREIGN KEY (thing) REFERENCES thing(id)
                 );
                 """)
mycursor.execute("SHOW TABLES")

for table in mycursor:
    print(table)

# mycursor.execute("""
#                  INSERT INTO person (id,name) VALUES
#                  (1,'John'),
#                  (2,'Jane'),
#                  (3,'Bob'),
#                  (4,'Alice'),
#                  (5,'Mirshod'),
#                  (6,'Dilshod'),
#                  (7,'Nurmuhammad'),
#                  (8,'Ali');
#                  """)
# mycursor.execute("""
#                  INSERT INTO thing (id,name) VALUES
#                  (1,'book'),
#                  (2,'notebook'),
#                  (3,'phone'),
#                  (4,'bag'),
#                  (5,'adore'),
#                  (6,'armor'),
#                  (7,'wine'),
#                  (8,'fine');
#                  """)
# mycursor.execute("""
#                  INSERT INTO owns (person,thing) VALUES
#                  (2,1),
#                  (2,2),
#                  (2,3),
#                  (4,4),
#                  (1,5),
#                  (1,6),
#                  (3,7),
#                  (3,8);
#                  """)
# mydb.commit()

class Person:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def show_info(self):
        print(f"ID: {self.id}, Name: {self.name}")
    
    def set_from_result(self,row):
        self.id = row[0]
        self.name = row[1]
    
    def insert_to_database(self,cursor):
        cursor.execute(f"INSERT INTO person (id,name) VALUES ({self.id},'{self.name}')")


p2 = Person(9,"Alex")
p2.insert_to_database(mycursor)

mycursor.execute("SELECT * FROM person")
result = mycursor.fetchall()

for row in result:
    person = Person()
    person.set_from_result(row)
    person.show_info()