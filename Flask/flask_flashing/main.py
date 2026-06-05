from flask import Flask, flash, render_template, redirect

app = Flask(__name__)

app.secret_key = "98ry34kjyf8oy4gbfwdgpqde"

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("You have been logged out", "success")
    return render_template("index.html")


app.run(debug=True)
