from components.decorators import AppRoute, Debug
from components.models import Engine, Logger, MapperRegistry
from components.notification import EmailNotifier, SmsNotifier, BaseSerializer
from components.test_data import start_add_test_data
from components.unit_of_work import UnitOfWork
from friday_framework.templator import render

site = Engine()
logger = Logger('views')
email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()
UnitOfWork.new_current()
UnitOfWork.get_current().set_mapper_registry(MapperRegistry)
site.courses = MapperRegistry.get_current_mapper('course').all()
site.type_courses = MapperRegistry.get_current_mapper('type_course').all()
routes = {}

# Test data.
start_add_test_data(site)


@AppRoute(routes=routes, url='/')
class Index:
    """Index class - the main page of the site."""

    @Debug(name="Index")
    def __call__(self, request):
        logger.log('Login to the main page.')
        return '200 OK', render('schedule.html')


@AppRoute(routes=routes, url='/about/')
class About:
    """About class - a page about the company."""

    @Debug(name="About")
    def __call__(self, request):
        logger.log('Login to the about company page.')
        return '200 OK', render('about.html')


@AppRoute(routes=routes, url='/feedback/')
class Feedback:
    """Feedback class - a page feedback."""

    @Debug(name="Feedback")
    def __call__(self, request):
        logger.log('Login to the feedback company page.')
        return '200 OK', render('feedback.html')


@AppRoute(routes=routes, url='/type-course-list/')
class TypeCourses:
    """TypeCourses class - CRUD class is type of course."""

    @Debug(name="TypeCoursesList-create-update-delete-detail")
    def __call__(self, request):
        method = request['method'].upper()
        mapper = MapperRegistry.get_current_mapper('type_course')
        if method == 'CREATE':
            logger.log('Creating Training types.')
            data = request['data']
            name = site.decode_value(data['name'])
            mapper.insert(name)
            UnitOfWork.get_current().commit()
            return '200 OK', render('type_courses.html',
                                    objects_list=mapper.all())

        elif method == 'DELETE':
            logger.log('Delete Training types.')
            id = int(request['data']['id'])
            obj = mapper.find_by_id(id)
            mapper.delete(obj)
            UnitOfWork.get_current().commit()
            return '200 OK', render('type_courses.html',
                                    objects_list=mapper.all())

        elif method == 'UPDATE':
            logger.log('Update Training types.')
            id = int(request['data']['id'])
            name = request['data']['name']
            obj = mapper.find_by_id(id)
            obj.name = name
            mapper.update(obj)
            return '200 OK', render('type_courses.html',
                                    objects_list=mapper.all())

        elif method == 'DETAIL':
            logger.log('Detail Training types.')
            id = int(request['data']['id'])
            result = mapper.find_by_id(id)
            return '200 OK', render('include/update_course_type.html',
                                    id=result.id, name=result.name)

        elif method == 'GET':
            logger.log('List of Training types.')
            return '200 OK', render('type_courses.html',
                                    objects_list=mapper.all())


@AppRoute(routes=routes, url='/course-list/')
class Courses:
    """Courses class - CRUD class is course."""

    @Debug(name="CoursesList-create-update-delete-detail")
    def __call__(self, request):
        method = request['method'].upper()
        mapper_courses = MapperRegistry.get_current_mapper('course')
        mapper_type_courses = MapperRegistry.get_current_mapper('type_course')
        if method == 'CREATE':
            logger.log('Creating Training.')
            name = request['data']['name']
            list_type_course = []
            if 'type_course' in request['data']:
                for i in request['data']['type_course']:
                    list_type_course.append(
                        mapper_type_courses.find_by_id(int(i)).id)
            name = site.decode_value(name)
            mapper_courses.insert(name, list_type_course)
            UnitOfWork.get_current().commit()
            # new_course = site.create_course(name, list_type_course)
            # site.courses.append(new_course)
            return '200 OK', render('courses.html', objects_list=mapper_courses.all(
            ), objects_list_type_course=mapper_type_courses.all())

        elif method == 'DETAIL':
            logger.log('Detail Training.')
            id = int(request['data']['id'])
            result = mapper_courses.find_by_id(id)
            return '200 OK', render('include/update_course.html',
                                    id=result.id,
                                    name=result.name,
                                    type=result.type,
                                    objects_list_type_course=mapper_type_courses.all())

        elif method == 'DELETE':
            logger.log('Deleting Training.')
            id = int(request['data']['id'])
            obj = mapper_courses.find_by_id(id)
            mapper_courses.delete(obj)
            UnitOfWork.get_current().commit()
            # result = site.delete_course(id)
            return '200 OK', render('courses.html',
                                    objects_list=mapper_courses.all())

        elif method == 'UPDATE':
            logger.log('Updating Training')
            id = int(request['data']['id'])
            name = request['data']['name']
            type_course = request['data']['type_course']
            list_type_course = []
            for i in type_course:
                list_type_course.append(
                    mapper_type_courses.find_by_id(int(i)).id)
            mapper_courses.update(id, name, list_type_course)
            UnitOfWork.get_current().commit()
            return '200 OK', render('courses.html',
                                    objects_list=mapper_courses.all())

        elif method == 'GET':
            logger.log('List of courses.')
            return '200 OK', render('courses.html', objects_list=mapper_courses.all(
            ), objects_list_type_course=mapper_type_courses.all())


@AppRoute(routes=routes, url='/category-list/')
class Category:
    """Courses class - CRUD class is course."""

    @Debug(name="CategoryList-create-update-delete-detail")
    def __call__(self, request):
        method = request['method'].upper()
        mapper_courses = MapperRegistry.get_current_mapper('course')
        if method == 'CREATE':
            logger.log('Creating category.')
            name = request['data']['name']
            list_courses = []
            if 'courses' in request['data']:
                for i in request['data']['courses']:
                    course = site.find_course_by_id(int(i))
                    list_courses.append(course)
            name = site.decode_value(name)
            new_category = site.create_category(name, list_courses)
            site.categories.append(new_category)
            return '200 OK', render('category.html',
                                    objects_list=site.categories)

        elif method == 'DETAIL':
            logger.log('Detail category..')
            id = int(request['data']['id'])
            result = site.category_detail(id)
            return '200 OK', render('include/update_category.html',
                                    id=result.id,
                                    name=result.name,
                                    courses=result.courses,
                                    objects_list_courses=mapper_courses.all())

        elif method == 'DELETE':
            logger.log('Deleting category..')
            id = int(request['data']['id'])
            result = site.category_delete(id)
            return '200 OK', render('category.html',
                                    objects_list=result)

        elif method == 'UPDATE':
            logger.log('Updating category')
            id = int(request['data']['id'])
            name = request['data']['name']
            list_courses = []
            if 'courses' in request['data']:
                for i in request['data']['courses']:
                    list_courses.append(site.find_course_by_id(int(i)))
            else:
                list_courses = site.find_category_by_id(int(id)).courses
            result = site.category_update(id, name, list_courses)
            return '200 OK', render('category.html',
                                    objects_list=result)

        elif method == 'GET':
            logger.log('List of categories.')
            return '200 OK', render('category.html',
                                    objects_list=site.categories,
                                    objects_list_courses=mapper_courses.all())


@AppRoute(routes=routes, url='/students-list/')
class Students:
    """Students class - CRUD class is student."""

    @Debug(name="StudentsList-create-update-delete-detail")
    def __call__(self, request):
        method = request['method'].upper()
        mapper_courses = MapperRegistry.get_current_mapper('course')
        if method == 'CREATE':
            logger.log('Creating student.')
            data = request['data']
            for k, v in data.items():
                if k == 'courses':
                    list_courses = []
                    for i in v:
                        list_courses.append(site.find_course_by_id(int(i)))
                    data[k] = list_courses
                else:
                    data[k] = site.decode_value(v)
            if ('courses' in data.keys()) is not True:
                data['courses'] = list()
            student = site.create_user('student', data)
            student.observers.append(email_notifier)
            site.students.append(student)
            student.add_student(site)
            return '200 OK', render('students.html',
                                    objects_list=site.students,
                                    objects_list_courses=mapper_courses.all())

        elif method == 'DETAIL':
            logger.log('Detail student.')
            id = int(request['data']['id'])
            result = site.student_detail(id)
            return '200 OK', render('include/update_student.html',
                                    id=result.id,
                                    first_name=result.first_name,
                                    last_name=result.last_name,
                                    age=result.age,
                                    email=result.email,
                                    phone=result.phone,
                                    objects_list_courses=mapper_courses())

        elif method == 'DELETE':
            logger.log('Deleting student.')
            id = int(request['data']['id'])
            site.student_delete(id)
            return '200 OK', render('students.html',
                                    objects_list=site.students)

        elif method == 'UPDATE':
            logger.log('Updating student.')
            id = int(request['data']['id'])
            first_name = request['data']['first_name']
            last_name = request['data']['last_name']
            age = request['data']['age']
            email = request['data']['email']
            phone = request['data']['phone']
            list_courses = []
            if 'courses' in request['data']:
                for i in request['data']['courses']:
                    list_courses.append(site.find_course_by_id(int(i)))
            else:
                list_courses = site.find_student_by_id(int(id)).courses
            site.student_update(id, first_name, last_name, age,
                                list_courses, email, phone)
            return '200 OK', render('students.html',
                                    objects_list=site.students)

        elif method == 'GET':
            logger.log('List of students.')
            return '200 OK', render('students.html',
                                    objects_list=site.students,
                                    objects_list_courses=mapper_courses.all())


@AppRoute(routes=routes, url='/teachers-list/')
class Teachers:
    """Teachers class - CRUD class is student."""

    @Debug(name="TeachersList-create-update-delete-detail")
    def __call__(self, request):
        method = request['method'].upper()
        mapper_courses = MapperRegistry.get_current_mapper('course')
        if method == 'CREATE':
            logger.log('Creating teacher.')
            data = request['data']
            for k, v in data.items():
                list_courses = []
                list_students = []
                if k == 'courses':
                    for i in v:
                        list_courses.append(site.find_course_by_id(int(i)))
                    data[k] = list_courses
                elif k == 'students':
                    for i in v:
                        list_students.append(site.find_student_by_id(int(i)))
                    data[k] = list_students
                else:
                    data[k] = site.decode_value(v)
            if ('courses' in data.keys()) is not True:
                data['courses'] = list()
            if ('students' in data.keys()) is not True:
                data['students'] = list()
            teacher = site.create_user('teacher', data)
            teacher.observers.append(email_notifier)
            site.teachers.append(teacher)
            teacher.add_teacher(site)
            return '200 OK', render('teachers.html',
                                    objects_list=site.teachers,
                                    objects_list_students=site.students,
                                    objects_list_courses=mapper_courses.all())

        elif method == 'DETAIL':
            logger.log('Detail teacher.')
            id = int(request['data']['id'])
            result = site.teacher_detail(id)
            return '200 OK', render('include/update_teacher.html',
                                    id=result.id,
                                    first_name=result.first_name,
                                    last_name=result.last_name,
                                    email=result.email,
                                    phone=result.phone,
                                    objects_list_courses=mapper_courses.all(),
                                    objects_list_students=site.students)

        elif method == 'DELETE':
            logger.log('Deleting teacher.')
            id = int(request['data']['id'])
            site.teacher_delete(id)
            return '200 OK', render('teachers.html',
                                    objects_list=site.teachers)

        elif method == 'UPDATE':
            logger.log('Updating teachers.')
            id = int(request['data']['id'])
            first_name = request['data']['first_name']
            last_name = request['data']['last_name']
            email = request['data']['email']
            phone = request['data']['phone']
            list_courses = []
            if 'courses' in request['data']:
                for i in request['data']['courses']:
                    list_courses.append(site.find_course_by_id(int(i)))
            else:
                list_courses = site.find_teacher_by_id(int(id)).courses
            list_students = []
            if 'students' in request['data']:
                for i in request['data']['students']:
                    list_students.append(site.find_student_by_id(int(i)))
            else:
                list_students = site.find_teacher_by_id(int(id)).students
            site.teacher_update(id, first_name, last_name, list_students,
                                list_courses, email, phone)
            return '200 OK', render('teachers.html',
                                    objects_list=site.teachers,
                                    objects_list_students=site.students)

        elif method == 'GET':
            logger.log('List of teachers.')
            return '200 OK', render('teachers.html',
                                    objects_list=site.teachers,
                                    objects_list_students=site.students,
                                    objects_list_courses=mapper_courses.all())


@AppRoute(routes=routes, url='/api/')
class CourseApi:
    @Debug(name='CourseApi')
    def __call__(self, request):
        path = request.get('path')
        if path:
            try:
                return '200 OK', BaseSerializer(
                    site.__dict__.get(path.split('/')[2])).save()
            except BaseException:
                return '200 OK', BaseSerializer("not").save()
        else:
            return '200 OK', BaseSerializer(site.courses).save()
