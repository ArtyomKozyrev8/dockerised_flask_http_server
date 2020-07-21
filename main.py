from flask import Flask, current_app, jsonify, render_template
import requests
import logging
import click


from settings.ext_api import ext_api_dom, ext_api_port
app = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


@app.cli.command("create-user")
@click.argument("name")
def create_user(name):
    print(f"Created user: {name}")
    with app.app_context():
        current_app.logger.info(f"Created user: {name}")


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


@app.route("/v1/<id>")
def v1(id_):
    app.logger.info(f"v1 got id: {id_}")
    return jsonify(res=f"v1 got id: {id_}")


@app.route("/template")
def template():
    return render_template("some_template.html")


if __name__ == '__main__':
    app.run("0.0.0.0", debug=False, port=12345)
