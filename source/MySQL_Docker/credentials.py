class DatabaseCredentials:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def get_credentials(self):
        return {
            "host": self.host,
            "port": self.port,
            "user": self.user,
            "password": self.password,
            "database": self.database
        }

# Create an instance of DatabaseCredentials
db_credentials = DatabaseCredentials(
    host="localhost",
    port=3306,
    user="root",
    password="strong_password",
    database="vote_db"
)

