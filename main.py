from flask import Flask
import requests
import logging

from settings.ext_api import ext_api_dom, ext_api_port
app = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


@app.route("/")
def hello():
    app.logger.error("root dir")
    req = requests.get(f"http://{ext_api_dom}:{ext_api_port}/")
    res = req.json()
    if res:
        res = res["result"]
    return res


@app.route("/x")
def x():
    app.logger.info("x dir")
    req = requests.get(f"http://{ext_api_dom}:{ext_api_port}/xsup")
    res = req.json()
    if res:
        res = res["result"]
    return res


@app.route("/y")
def y():
    app.logger.error("y dir")
    req = requests.get(f"http://{ext_api_dom}:{ext_api_port}/ysup")
    res = req.json()
    if res:
        res = res["result"]
    return res


@app.route("/z")
def z():
    app.logger.info("z dir")
    req = requests.get(f"http://{ext_api_dom}:{ext_api_port}/zsup")
    res = req.json()
    if res:
        res = res["result"]
    return res


@app.route("/z2")
def z2():
    app.logger.info("z2 dir")
    raise Exception("z2 error in main server")


if __name__ == '__main__':
    app.run("0.0.0.0", debug=False, port=12345)
