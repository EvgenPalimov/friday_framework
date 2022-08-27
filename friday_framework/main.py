import quopri
from os import path

from components.content_types import CONTENT_TYPES_MAP
from friday_framework.requests import PostRequests, GetRequests
from views import logger


class PageNotFound404:
    """Page Not Found 404 class informs that such a page has not been found."""

    def __call__(self, request):
        return '404 WHAT', '404 Page Not Found'


class Framework:
    """The Framework class is the basis of the framework."""

    def __init__(self, settings, routes_obj):
        self.settings = settings
        self.routes_lst = routes_obj

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            if data.get('method'):
                method_new = data['method']
                if method_new != '':
                    request['method'] = data['method']
                    self.add_logger(method_new, data)
                else:
                    self.add_logger(method, data)
            else:
                self.add_logger(method, data)
            # print(f'We received a post request: {data}.')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            print(f'We received GET parameters: {request_params}.')

        if path in self.routes_lst:
            view = self.routes_lst[path]
            content_type = self.get_content_type(path)
            code, body = view(request)
            body = body.encode('utf-8')

        elif '/api/'.find(path) == 0:
            view = self.routes_lst['/api/']
            request['path'] = path
            content_type = self.get_content_type(path)
            code, body = view(request)
            body = body.encode('utf-8')

        elif path.startswith(self.settings.STATIC_URL):
            # /static/images/logo.jpg/ -> images/logo.jpg
            file_path = path[len(self.settings.STATIC_URL):len(path) - 1]
            content_type = self.get_content_type(file_path)
            code, body = self.get_static(self.settings.STATIC_FILES_DIR,
                                         file_path)
        else:
            view = PageNotFound404()
            content_type = self.get_content_type(path)
            code, body = view(request)
            body = body.encode('utf-8')
        start_response(code, [('Content-Type', content_type)])

        return [body]

    @staticmethod
    def add_logger(method, data):
        logger.log(
            f'He came to us {method}- request: {Framework.decode_value(data)}')

    @staticmethod
    def get_content_type(file_path, content_types_map=CONTENT_TYPES_MAP):
        file_name = path.basename(file_path).lower()
        extension = path.splitext(file_name)[1]
        return content_types_map.get(extension, 'text/html')

    @staticmethod
    def get_static(static_dir, file_path):
        path_to_file = path.join(static_dir, file_path)
        with open(path_to_file, 'rb') as f:
            file_content = f.read()
        status_code = '200 OK'
        return status_code, file_content

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            # Обрабатываем списки пока
            if type(v) == list:
                val = ','.join(v)
            else:
                val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data


class DebugApplication(Framework):
    """
    The logging class - the same as the main one,
    only outputs information for each request
    (request type and parameters) to the console.
    """

    def __init__(self, settings, routes_obj):
        super().__init__(settings, routes_obj)
        self.application = Framework(settings, routes_obj)

    def __call__(self, env, start_response):
        print('Debug mode.')
        print(env)
        return self.application(env, start_response)


class FakeApplication(Framework):
    """
    Fake class - responds to all user requests: 200 OK, Hello from Fake.
    """

    def __init__(self, settings, routes_obj):
        super().__init__(settings, routes_obj)
        self.application = Framework(settings, routes_obj)

    def __call__(self, env, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello from Fake.']
