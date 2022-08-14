from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder='templates', **kwargs):
    """
    A function that processes site templates.

    :param template_name: template name,
    :param folder: the folder where the templates are located,
    :param kwargs: additional parameters accepted by the function,
    :return: a rendered template with parameters.
    """

    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)
