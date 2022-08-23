from datetime import date

from components.decorators import AppRoute
from components.models import Engine, Logger
from components.test_data import add_test_data_type_course, \
    add_test_data_course
from friday_framework.templator import render

site = Engine()
logger = Logger('views')
routes = {}

# Test data.
add_test_data_type_course(site)
add_test_data_course(site)


@AppRoute(routes=routes, url='/')
class Index:
    """Index class - the main page of the site."""

    def __call__(self, request):
        logger.log('Login to the main page.')
        return '200 OK', render('schedule.html')


@AppRoute(routes=routes, url='/about/')
class About:
    """About class - a page about the company."""

    def __call__(self, request):
        logger.log('Login to the about company page.')
        return '200 OK', render('about.html')


@AppRoute(routes=routes, url='/feedback/')
class Feedback:
    """Feedback class - a page feedback."""

    def __call__(self, request):
        Logger.log('Login to the feedback page.')
        return '200 OK', render('feedback.html')


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


@AppRoute(routes=routes, url='/category-list/')
class CategoryList:
    """CategoryList class - list of categories."""

    def __call__(self, request):
        logger.log('List of categories.')
        return '200 OK', render('category.html', objects_list=site.categories)


@AppRoute(routes=routes, url='/teacher-list/')
class TeachersList:
    """TeachersList class - list of teachers."""

    def __call__(self, request):
        logger.log('Getting a list of teachers.')
        return '200 OK', render('teachers.html', objects_list=site.teachers)


@AppRoute(routes=routes, url='/student-list/')
class StudentsList:
    """StudentsList class - list of students."""

    def __call__(self, request):
        logger.log('Getting a list of students.')
        return '200 OK', render('teachers.html', objects_list=site.students)


@AppRoute(routes=routes, url='/type-course-list/')
class TypeCourses:
    """TypeCourses class - CRUD class is type of course."""

    def __call__(self, request):
        method = request['method'].upper()
        if method == 'CREATE':
            logger.log('Creating Training types.')
            data = request['data']
            name = site.decode_value(data['name'])

            new_type = site.type_course_create(name)
            site.type_courses.append(new_type)
            return '200 OK', render('type_courses.html',
                                    objects_list=site.type_courses)

        elif method == 'DELETE':
            logger.log('Delete Training types.')
            id = int(request['data']['id'])
            result = site.type_course_delete(id)
            return '200 OK', render('type_courses.html',
                                    objects_list=result)

        elif method == 'UPDATE':
            logger.log('Update Training types.')
            id = int(request['data']['id'])
            name = request['data']['name']
            print(id, name)
            result = site.type_course_update(id, name)
            return '200 OK', render('type_courses.html',
                                    objects_list=result)

        elif method == 'DETAIL':
            logger.log('Detail Training types.')
            id = int(request['data']['id'])
            result = site.type_course_detail(id)
            return '200 OK', render('include/update_course_type.html',
                                    id=result.id, name=result.name)

        elif method == 'GET':
            logger.log('List of Training types.')
            return '200 OK', render('type_courses.html',
                                    objects_list=site.type_courses)


@AppRoute(routes=routes, url='/course-list/')
class Courses:
    """Courses class - CRUD class is course."""

    def __call__(self, request):
        method = request['method'].upper()
        if method == 'CREATE':
            logger.log('Creating Training.')
            name = request['data']['name']
            type_course = request['data']['type_course']
            list_type_course = []
            for i in type_course:
                list_type_course.append(site.find_type_course_by_id(int(i)))
            name = site.decode_value(name)
            new_course = site.create_course(name, list_type_course)
            site.courses.append(new_course)
            return '200 OK', render('courses.html',
                                    objects_list=site.courses,
                                    objects_list_type_course=site.type_courses)

        elif method == 'DETAIL':
            logger.log('Detail Training.')
            id = int(request['data']['id'])
            result = site.course_detail(id)
            return '200 OK', render('include/update_course.html',
                                    id=result.id,
                                    name=result.name,
                                    type=result.type,
                                    objects_list_type_course=site.type_courses)

        elif method == 'DELETE':
            logger.log('Deleting Training.')
            id = int(request['data']['id'])
            result = site.delete_course(id)
            return '200 OK', render('courses.html',
                                    objects_list=result)

        elif method == 'UPDATE':
            logger.log('Updating Training')
            id = int(request['data']['id'])
            name = request['data']['name']
            type_course = request['data']['type_course']
            list_type_course = []
            for i in type_course:
                list_type_course.append(site.find_type_course_by_id(int(i)))
            result = site.course_update(id, name, list_type_course)
            return '200 OK', render('courses.html',
                                    objects_list=result)

        elif method == 'COPY':
            logger.log('')
            id = int(request['data']['id'])
            new_course = site.copy_course(id)
            site.courses.append(new_course)
            return '200 OK', render('courses.html',
                                    objects_list=site.courses)


        elif method == 'GET':
            logger.log('List of courses.')
            return '200 OK', render('courses.html',
                                    objects_list=site.courses,
                                    objects_list_type_course=site.type_courses)
