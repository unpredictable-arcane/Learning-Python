from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "pikachu": 88,
        "Bulbasaur": 74,
        "Charmander": 79,
        "Squirtle": 68,
        "Archaludon": 95,
        "Mew": 99
    }
    return render_template("index.html", marks=marks)

app.run(debug=True)