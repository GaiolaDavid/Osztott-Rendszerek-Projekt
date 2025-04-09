from flask import Flask, render_template, request, jsonify
from collections import namedtuple
from MySQL_Docker.db import DatabaseConnection
from MySQL_Docker.credentials import db_credentials
from MySQL_Docker.repository import AnswerRepository, UserRepository, VotingSystemRepository

class Field:
    def __init__(self, name, question, type, answer, correct_answer):
        self.name = name
        self.question = question
        self.type = type
        self.answer = answer
        self.correct_answer = correct_answer
    def __str__(self):
        return self.name + " : " + self.answer
    def __dict__(self):
        return {
            "name": self.name,
            "type": self.type,
            "answer": self.answer,
            "correct_answer": self.correct_answer
        }

fields = [
    Field("question1", "Hanyas cipot hord Ruben?", "number", "","valasz"),
    Field("question2", "Mi Ruben masodik neve?", "text", "",""),
    Field("question3", "Milyen magas Tamas? (Tamas szerint, de amugy alacsonyabb)", "number", "", 184),
    ]

app = Flask(__name__)
db_connection = DatabaseConnection(db_credentials)
db_connection.establish_connection()

@app.route("/")
def home_page():
    return render_template('pages/index.html')

@app.route("/answers")
def answer_page():
    voting_system_repository = VotingSystemRepository(db_credentials)
    answers = voting_system_repository.get_all_answers()
    return render_template('pages/answers.html', answers=answers)

@app.route("/form",methods=['GET', 'POST'])
def form_page():

    string = ""
    userdata = {"name": "", "gender": None}
    if request.method == 'POST':
        userdata["name"] = request.form['name']
        userdata["gender"] = request.form['gender']
        for f in fields:
            string += f.name + " : " + request.form[f.name] + "; "
            if f.type == "text" or f.type == "email":
                f.answer = request.form[f.name]
            elif f.type == "number":
                try:
                    f.answer = int(request.form[f.name])
                except:
                    f.answer = None

        return render_template('pages/form_validated.html',f=fields, userdata=userdata)
    else:
        return render_template('pages/form.html',f=fields)

@app.route("/about")
def about_page():
    return render_template('pages/about.html')

if __name__ == '__main__':
    app.run(debug=True)
