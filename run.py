from friday_framework.main import Framework
from urls import routes, fronts
from wsgiref.simple_server import make_server

application = Framework(routes, fronts)
ip_address = '127.0.0.1'
port = 8000

with make_server(ip_address, port, application) as httpd:
    print(f'Server is working... \n '
          f'Address server - http://{ip_address}:{port}/.')
    httpd.serve_forever()
