from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def json():
    marks = {
        "Anuj": 87,
        "Ankit": 82,
        "Tushar": 76,
        "Piyush": 85,
        "Nandani": 79  
    }
    return jsonify(marks)

app.run(debug=True)
