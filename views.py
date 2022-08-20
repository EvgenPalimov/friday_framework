from datetime import date

from friday_framework.templator import render
from patterns.patterns import Engine, Logger

site = Engine()
logger = Logger('views')


class Index:
    """Index class - the main page of the site."""

    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=site.categories)


class StudyPrograms:
    """StudyPrograms class - the main page of the site."""

    def __call__(self, request):
        return '200 OK', render('study-programs.html', date=date.today())


class Contacts:
    """Contacts class - the main page of the site."""

    def __call__(self, request):
        return '200 OK', render('contacts.html',
                                data=request.get('data', None))


class CoursesList:
    """CoursesList class - the main page of the site."""

    def __call__(self, request):
        logger.log('List of courses.')
        try:
            category = site.find_category_by_id(
                int(request['request_params']['id']))
            return '200 OK', render('course_list.html',
                                    objects_list=category.courses,
                                    name=category.name,
                                    id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet.'


class About:
    """About class - a page about the company."""

    def __call__(self, request):
        return '200 OK', render('about.html',
                                data=request.get('data', None))


class NotFound404:
    """The Not Found 404 class is an alert if the page is not available."""

    def __call__(self, request):
        return '404 WHAT', '404 Page Not Found'


class CreateCourse:
    """Controller class - creating a course."""

    category_id = -1

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))
                course = site.create_course('record', name, category)
                site.courses.append(course)

            return '200 OK', render('course_list.html',
                                    objects_list=category.courses,
                                    name=category.name,
                                    id=category.id)

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id((int(self.category_id)))

                return '200 OK', render('create_course.html',
                                        name=category.name,
                                        id=category.id)
            except KeyError:
                return '200 OK', 'No categories have been added yet.'


class CreateCategory:
    """Controller class - creating category."""

    def __call__(self, request):
        if request['method'] == 'POST':
            print(request)
            data = request['data']
            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)
            return '200 OK', render('index.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create_category.html',
                                    categories=categories)


class CategoryList:
    """Controller class - list of categories."""

    def __call__(self, request):
        logger.log('List of categories.')
        return '200 OK', render('category_list.html',
                                objects_list=site.categories)


class CopyCourse:
    """Controller class - create new course."""

    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']
            old_course = site.get_course(name)
            if old_course:
                new_name = f'Copy_{name}.'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)

            return '200 OK', render('course_list.html',
                                    objects_list=site.courses)
        except KeyError:
            return '200 OK', 'No courses have been added yet.'
