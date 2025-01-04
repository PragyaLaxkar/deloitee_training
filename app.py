from flask import Flask


app = Flask(__name__)



@app.route("/info")
def myapp():
    return "Welcome to Pragya's Page...."


app.run(host='0.0.0.0')
