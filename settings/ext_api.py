is_docker = True

if not is_docker:
    ext_api_dom = "localhost"
    ext_api_port = "11155"
else:
    ext_api_dom = "sup_serv"
    ext_api_port = "80"
