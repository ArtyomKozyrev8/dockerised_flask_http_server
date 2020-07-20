is_docker = True
import os


IS_DOCKER = os.getenv("IS_DOCKER", "True")

if IS_DOCKER in {"1", "TRUE", "True", "true"}:
    IS_DOCKER = True
elif IS_DOCKER in {"0", "False", "FALSE", "false"}:
    IS_DOCKER = False
else:
    IS_DOCKER = True

if not IS_DOCKER:
    ext_api_dom = "localhost"
    ext_api_port = "11155"
else:
    ext_api_dom = "sup_serv"
    ext_api_port = "80"
