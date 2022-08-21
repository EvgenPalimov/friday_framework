from components.settings import PORT, URL_ADDRESS
from friday_framework.main import Framework
from urls import routes
from wsgiref.simple_server import make_server
from components import settings

application = Framework(settings, routes)

with make_server(URL_ADDRESS, PORT, application) as httpd:
    print(f'Server is working... \n '
          f'Address server - http://{URL_ADDRESS}:{PORT}/.')
    httpd.serve_forever()
