from jinja2 import Template
import os


def render(template_name, folder='templates', **kwargs):
    """
    Функция обрабатывающая шаблоны сайта.

    :param template_name: имя шаблона,
    :param folder: папка в котором находяться шаблоны,
    :param kwargs: дополнительные параметры принимаемые функцией,
    :return: возвращает отрендереный шаблон с параметрами.
    """

    file_path = os.path.join(folder, template_name)

    with open(file_path, encoding='utf-8') as f:
        template = Template(f.read())

    return template.render(**kwargs)
