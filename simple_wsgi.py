def application(environ, start_response):
    """
    :param environ: ������� ������ �� �������
    :param start_response: ������� ��� ������ �������
    """
    # ������� � ������� start_response �������� ��� ������ � ���������
    start_response('200 OK', [('Content-Type', 'text/html')])
    # ���������� ���� ������ � ���� ������ �� bite
    return [b'Hello world from a simple WSGI application!']