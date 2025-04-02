from flask import Flask
import emoji

app = Flask(__name__)

# root route
@app.route("/")
def code():
    return "<h1></h1>"
