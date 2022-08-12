from friday_framework.templator import render


class Index:
    """Index class - the main page of the site."""

    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class Contacts:
    """Contacts class - the main page of the site."""

    def __call__(self, request):
        return '200 OK', render('contacts.html',
                                data=request.get('data', None))


class Product:
    """Product class - a page displaying information about the course."""

    def __call__(self, request):
        return '200 OK', 'Product'


class User:
    """User class - displays information about the user."""

    def __call__(self, request):
        return '200 OK', 'User'


class About:
    """About class - a page about the company."""

    def __call__(self, request):
        return '200 OK', 'About'


class NotFound404:
    """The Not Found 404 class is an alert if the page is not available."""

    def __call__(self, request):
        return '404 WHAT', '404 Page Not Found'
