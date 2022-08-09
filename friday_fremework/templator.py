from jinja2 import Template
import os


def render(template_name, folder='templates', **kwargs):
    """
    A function that processes site templates.

    :param template_name: template name,
    :param folder: the folder where the templates are located,
    :param kwargs: additional parameters accepted by the function,
    :return: returns a rendered template with parameters.
    """

    file_path = os.path.join(folder, template_name)

    with open(file_path, encoding='utf-8') as f:
        template = Template(f.read())

    return template.render(**kwargs)
