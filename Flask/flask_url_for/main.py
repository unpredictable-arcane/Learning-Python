from flask import Flask, render_template

# app = Flask(__name__, static_url_path="/public") 
#this is how we can change the url path of the static

app = Flask(__name__, static_folder="/assets", static_url_path="/static") #changing the static folder location


@app.route("/")
def hello_world():
    return render_template(("index.html"))

app.run(debug=True)