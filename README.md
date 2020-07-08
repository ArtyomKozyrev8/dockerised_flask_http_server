# dockerised_flask_http_server
This is part of dockerised application sandbox. Is used to play around dockerised microservices.

To test locally out of docker container, check is_docker flag in settings/ext_api.py since 
in the tested case we do not create port for support container to communicate with 
outer world. 

How to run:

docker run -d -p 9991:80 --name main_server --network artnet -e GUNICORN_CONF="/usr/src/app/gunicorn_conf.py" main_server