import mysql.connector

from MySQL_Docker import credentials

class UserRepository:
    def __init__(self, db_credentials):
        self.db_credentials = db_credentials
        self.conn = None
        self.cursor = None

    def establish_connection(self):
        self.conn = mysql.connector.connect(**self.db_credentials.get_credentials())
        self.cursor = self.conn.cursor()

    def get_all_users(self):
        query = "SELECT * FROM User"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM User WHERE UserID = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        return

    def get_user_by_name(self, user_name):
        query = "SELECT * FROM User WHERE UserName = %s"
        self.cursor.execute(query, (user_name,))
        return self.cursor.fetchone()

    def create_user(self, user_name, gender):
        query = "INSERT INTO User (UserName, Gender) VALUES (%s, %s)"
        self.cursor.execute(query, (user_name, gender))
        self.conn.commit()
        return

class AnswerRepository:
    def __init__(self, db_credentials):
        self.db_credentials = db_credentials
        self.conn = None
        self.cursor = None

    def establish_connection(self):
        self.conn = mysql.connector.connect(**self.db_credentials.get_credentials())
        self.cursor = self.conn.cursor()

    def get_all_answers(self):
        query = "SELECT * FROM Answer"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_answers_by_user_id(self, user_id):
        query = "SELECT * FROM Answer WHERE UserID = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

class VotingSystemRepository:
    def __init__(self, db_credentials):
        self.user_repository = UserRepository(db_credentials)
        self.answer_repository = AnswerRepository(db_credentials)

    def get_all_users(self):
        self.user_repository.establish_connection()
        users = self.user_repository.get_all_users()
        self.user_repository.close_connection()
        return users

    def get_user_by_id(self, user_id):
        self.user_repository.establish_connection()
        user = self.user_repository.get_user_by_id(user_id)
        self.user_repository.close_connection()
        return user

    def get_all_answers(self):
        self.answer_repository.establish_connection()
        answers = self.answer_repository.get_all_answers()
        self.answer_repository.close_connection()
        return answers

    def get_answers_by_user_id(self, user_id):
        self.answer_repository.establish_connection()
        answers = self.answer_repository.get_answers_by_user_id(user_id)
        self.answer_repository.close_connection()
        return answers

    def get_user_by_name(self, user_name):
        self.user_repository.establish_connection()
        user = self.user_repository.get_user_by_name(user_name)
        self.user_repository.close_connection()
        return user

def main():
    db_credentials = credentials.db_credentials
    voting_system_repository = VotingSystemRepository(db_credentials)

    # Example usage:
    users = voting_system_repository.get_all_users()
    for user in users:
        print(user)

    user_id = 1
    user = voting_system_repository.get_user_by_id(user_id)
    print(user)

    user_name = 'Alice'
    user = voting_system_repository.get_user_by_name(user_name)
    print(user)

    user_name = 'Alice1'
    user = voting_system_repository.get_user_by_name(user_name)
    print(user)

    answers = voting_system_repository.get_all_answers()
    for answer in answers:
        print(answer)

    answers = voting_system_repository.get_answers_by_user_id(user_id)
    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()

