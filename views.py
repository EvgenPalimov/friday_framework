from friday_fremework.templator import render

class Index:
    """Класс Index - главная страница сайта."""

    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class About:
    """Класс About - страница о компании."""
    def __call__(self, request):
        return '200 OK', 'About'


class NotFound404:
    """Класс NotFound404 - оповещение, если страница не доступна."""

    def __call__(self, request):
        return '404 WHAT', '404 Page Not Found'
