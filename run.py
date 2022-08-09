from friday_framework.main import Framework
from urls import routes, fronts
from wsgiref.simple_server import make_server

application = Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print('Server is working... \n Address server - 127.0.0.1:8080.')
    httpd.serve_forever()
