import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="127.0.0.1",  # Since the container is mapped to localhost
    port=3307,         # Port mapped from Docker
    user="root",       # Default MySQL user
    password="strong_password",  # Root password set in Docker
    database="final_mysql"  # Change this to your actual database name
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")
for table in cursor.fetchall():
    print(table)

cursor.close()
conn.close()