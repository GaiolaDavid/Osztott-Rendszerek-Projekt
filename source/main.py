from flask import Flask, render_template, request, jsonify
from collections import namedtuple

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
    Field("Name", "", "text", "",""),
    Field("Email", "", "email", "",""),
    Field("question1", "Hanyas cipot hord Ruben?", "number", "","valasz"),
    Field("question2", "Mi Ruben masodik neve?", "text", "",""),
    Field("question3", "Milyen magas Tamas? (Tamas szerint, de amugy alacsonyabb)", "number", "", 184),
    ]

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('pages/index.html')

@app.route("/form",methods=['GET', 'POST'])
def form_page():
    string = ""
    if request.method == 'POST':
        for f in fields:
            string += f.name + " : " + request.form[f.name] + "; "
            if f.type == "text" or f.type == "email":
                f.answer = request.form[f.name]
            elif f.type == "number":
                try:
                    f.answer = int(request.form[f.name])
                except:
                    f.answer = None

        return render_template('pages/form_validated.html',f=fields)
    else:
        return render_template('pages/form.html',f=fields)

@app.route("/about")
def about_page():
    return render_template('pages/about.html')

if __name__ == '__main__':
    app.run(debug=True)
