from components.settings import PORT, URL_ADDRESS
from friday_framework.main import Framework, DebugApplication, FakeApplication
from wsgiref.simple_server import make_server
from components import settings
from views import routes

# Creating a WSGI application object.
application = Framework(settings, routes)
# application = DebugApplication(settings, routes)
# application = FakeApplication(settings, routes)

with make_server(URL_ADDRESS, PORT, application) as httpd:
    print(f'Server is working... \n '
          f'Address server - http://{URL_ADDRESS}:{PORT}/.')
    httpd.serve_forever()
