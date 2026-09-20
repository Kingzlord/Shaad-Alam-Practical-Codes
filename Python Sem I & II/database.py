import mysql.connector as mysql
connection = mysql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    charset = "utf8"
    )
print("MySQL connected successfully")

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS college;")

connection.database = "college"

table = """
CREATE TABLE IF NOT EXISTS students(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    NAME VARCHAR(50),
    AGE INT,
    COURSE VARCHAR(50)
);
"""


##disconneting sql
cursor.execute(table)
connection.commit()
cursor.close()
connection.close()
