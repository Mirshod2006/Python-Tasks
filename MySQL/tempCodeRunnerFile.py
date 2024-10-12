mycursor.execute("CREATE TABLE IF NOT EXISTS flights(id INT,plane_type VARCHAR(50),time VARCHAR(20),take_off VARCHAR(50),take_on VARCHAR(50))")
# mycursor.execute("INSERT INTO flights (id,plane_type,time,take_off,take_on) VALUES (%s,%s,%s,%s,%s)",[
#     (1, 'Boeing 737', '2024-12-18 14:30', 'Tashkent International Airport', 'Samarkand International Airport'),
#     (2, 'Airbus A320', '2024-10-13 09:00', 'Samarkand International Airport', 'Bukhara International Airport'),
#     (3, 'Boeing 747', '2024-11-14 18:45', 'Tashkent International Airport', 'Moscow Sheremetyevo Airport')
#     (4, 'Boeing 737', '2024-10-11 16:45', 'Tashkent International Airport', 'Samarkand International Airport'),
#     (5, 'Airbus A320', '2024-12-10 09:00', 'Samarkand International Airport', 'Bukhara International Airport'),
#     (6, 'Boeing 747', '2024-10-15 17:15', 'Tashkent International Airport', 'Moscow Sheremetyevo Airport')
#     (7, 'Boeing 737', '2024-11-11 11:00', 'Tashkent International Airport', 'Samarkand International Airport'),
#     (8, 'Airbus A320', '2024-10-13 09:00', 'Samarkand International Airport', 'Bukhara International Airport'),
#     (9, 'Boeing 747', '2024-12-14 13:15', 'Tashkent International Airport', 'Moscow Sheremetyevo Airport')
#     (10, 'Boeing 737', '2024-10-12 10:30', 'Tashkent International Airport', 'Samarkand International Airport'),
#     (11, 'Airbus A320', '2024-11-03 09:00', 'Samarkand International Airport', 'Bukhara International Airport'),
#     (12, 'Boeing 747', '2024-10-17 14:45', 'Tashkent International Airport', 'Moscow Sheremetyevo Airport')
# ])
# mydb.commit()

# mycursor.execute("DELETE FROM flights")