import mysql.connector
from MySQL_Docker.credentials import db_credentials

class DatabaseConnection:
    def __init__(self, credentials):
        self.credentials = credentials
        self.conn = None
        self.cursor = None

    def establish_connection(self):
        self.conn = mysql.connector.connect(**self.credentials.get_credentials())
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

def main():
    db_connection = DatabaseConnection(db_credentials)
    db_connection.establish_connection()
    result = db_connection.execute_query("SHOW TABLES;")
    for table in result:
        print(table)
    db_connection.close_connection()

if __name__ == "__main__":
    main()

