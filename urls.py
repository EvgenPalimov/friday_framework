from datetime import date
from views import Index, About


def date_front(request: dict):
    """
    ������� - ���������� ������� ���� � request.

    :param request: dict:  ��������� ������� � ����������� ��� ������,
    :return: dict: �������� ������� � ����������� �����������.
    """

    request['data'] = date.today()


def secret_key_front(request: dict):
    """
    ������� - ���������� ��������� ���� � request.

    :param request: dict:  ��������� ������� � ����������� ��� ������,
    :return: dict: �������� ������� � ����������� �����������.
    """

    request['key'] = 'key'


def admin_front(request: dict):
    """
    ������� - ���������� ������ �������������� � request.

    :param request: dict:  ��������� ������� � ����������� ��� ������,
    :return: dict: �������� ������� � ����������� �����������.
    """

    request['admin'] = {
        'admin_name': 'Djon',
        'password': '12345'
    }


fronts = [date_front, secret_key_front, admin_front]

routes = {
    '/': Index(),
    '/about/': About()
}
