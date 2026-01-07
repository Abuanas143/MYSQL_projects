import mysql.connector
import psycopg2

mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anas,.1122",
    database="test_db"
)

mysql_cursor = mysql_conn.cursor()
mysql_cursor.execute("SELECT full_name FROM clark")
rows = mysql_cursor.fetchall()

pg_conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="Anas,.1122",
    database="Anas Ali",
    port="7416"
)

pg_cursor = pg_conn.cursor()

for row in rows:
    full_name = row[0]             
    parts = full_name.split(" ")   

    first = parts[0]             
    last = " ".join(parts[1:])     

    pg_cursor.execute(
        "INSERT INTO python_pg (first_name, last_name) VALUES (%s, %s)",
        (first, last)
    )

pg_conn.commit()

print("Data transferred successfully.")