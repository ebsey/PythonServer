from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Good day, oblate spheroid"

def test_hello():
    assert(True)
