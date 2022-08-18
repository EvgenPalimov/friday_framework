from datetime import date
from views import Index, About, Contacts, StudyPrograms, CoursesList, \
    CreateCourse, CreateCategory, CategoryList, CopyCourse


def date_front(request: dict):
    """
    Function - passing the current date to the request.

    :param request: dict: accepts a dictionary with parameters or an empty one,
    :return: dict: returns a dictionary with updated parameters.
    """

    request['date'] = date.today()


def secret_key_front(request: dict):
    """
    The function that passes the secret key to the request.

    :param request: dict: accepts a dictionary with parameters or an empty one,
    :return: dict: returns a dictionary with updated parameters.
    """

    request['key'] = 'key'


def admin_front(request: dict):
    """
    Function - transmitting administrator data to request.

    :param request: dict: accepts a dictionary with parameters or an empty one,
    :return: dict: returns a dictionary with updated parameters.
    """

    request['admin'] = {
        'admin_name': 'Djon',
        'password': '12345'
    }


fronts = [date_front, secret_key_front, admin_front]

routes = {
    '/': Index(),
    '/about/': About(),
    '/study_programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse(),
    '/contacts/': Contacts()
}
