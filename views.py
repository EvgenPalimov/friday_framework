from friday_fremework.templator import render

class Index:
    """����� Index - ������� �������� �����."""

    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class About:
    """����� About - �������� � ��������."""
    def __call__(self, request):
        return '200 OK', 'About'


class NotFound404:
    """����� NotFound404 - ����������, ���� �������� �� ��������."""

    def __call__(self, request):
        return '404 WHAT', '404 Page Not Found'
