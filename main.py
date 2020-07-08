from flask import Flask
import requests

from settings.ext_api import ext_api_dom, ext_api_port
app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.error("root dir")
    req = requests.get(f"http://{ext_api_dom}:{ext_api_port}/")
    res = req.json()
    return res


@app.route("/x")
def x():
    app.logger.info("x dir")
    req = requests.get(f"http://{ext_api_dom}:{ext_api_port}/xsup")
    res = req.json()
    return res


@app.route("/y")
def y():
    app.logger.error("y dir")
    req = requests.get(f"http://{ext_api_dom}:{ext_api_port}/ysup")
    res = req.json()
    return res


if __name__ == '__main__':
    app.run("0.0.0.0", debug=False, port=12345)
