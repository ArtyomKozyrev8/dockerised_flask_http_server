from libs import mylib
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info("/2332авыа")
    return "Hello World from Flask"


@app.route("/x")
def x():
    app.logger.info("/x23213213")
    return mylib.do_some_work()


@app.route("/y")
def y():
    app.logger.info("/y2131233")
    return mylib.do_another()


if __name__ == '__main__':
    app.run("0.0.0.0", debug=False, port=12345)
