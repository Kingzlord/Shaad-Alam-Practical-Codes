import mysql.connector

# CONNECT TO MYSQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",              # change if needed
    password="root", # put your MySQL password here
    charset="utf8"            # IMPORTANT: avoids utf8mb4 error
)
cursor = connection.cursor()
print("Connected to MySQL server")
cursor.execute("CREATE DATABASE IF NOT EXISTS college")
print("Database 'college' created")
connection.database="college"
# CREATE TABLE
create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    course VARCHAR(100)
);
"""
cursor.execute(create_table_query)
print("✅ Table 'students' created successfully in MySQL!")
# drop_table="DROP TABLE IF EXISTS students"
# cursor.execute(drop_table)
# print("Table 'students' dropped")
connection.commit()
cursor.close()
connection.close()
print("MySQL connection closed")
