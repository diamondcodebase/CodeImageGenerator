from flask import Flask

app = Flask(__name__)

# root route
@app.route("/")
def code():
    return "<h1>Hello!</h1>"
