from time import time


class AppRoute:
    """Decorator for routing implementation."""

    def __init__(self, routes, url):
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        self.routes[self.url] = cls()


class Debug:
    """Decorator class - measuring the execution time of a function."""

    def __init__(self, name):
        self.name = name

    def __call__(self, cls):

        def timeit(method):

            def timed(*args, **kwargs):
                ts = time()
                result = method(*args, **kwargs)
                te = time()
                delta = te - ts

                print(f'Debug --> {self.name} finished {delta:2.2f} ms')
                return result

            return timed

        return timeit(cls)