from datetime import date
from views import Index, About


def date_front(request: dict):
    """
    Функция - передающая текущую дату в request.

    :param request: dict:  принимаем словарь с параметрами или пустой,
    :return: dict: возвщаем словарь с обновлеными параметрами.
    """

    request['data'] = date.today()


def secret_key_front(request: dict):
    """
    Функция - передающая секретный ключ в request.

    :param request: dict:  принимаем словарь с параметрами или пустой,
    :return: dict: возвщаем словарь с обновлеными параметрами.
    """

    request['key'] = 'key'


def admin_front(request: dict):
    """
    Функция - передающая данные администратора в request.

    :param request: dict:  принимаем словарь с параметрами или пустой,
    :return: dict: возвщаем словарь с обновлеными параметрами.
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
