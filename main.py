from libs import mylib
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask"


@app.route("/x")
def x():
    return mylib.do_some_work()


@app.route("/y")
def y():
    return mylib.do_another()


if __name__ == '__main__':
    app.run("0.0.0.0", debug=False, port=12345)
