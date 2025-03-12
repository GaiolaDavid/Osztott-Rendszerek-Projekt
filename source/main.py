from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('pages/index.html')

@app.route("/form")
def form_page():
    return render_template('pages/form.html')

@app.route("/about")
def about_page():
    return render_template('pages/about.html')

if __name__ == '__main__':
    app.run(debug=True)
