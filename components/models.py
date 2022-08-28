import quopri
from components.notification import Subject, ConsoleWriter, FileWriter


class User:
    """Class User - creates a User object."""

    auto_id = 0

    def __init__(self, dict_data):
        self.first_name = dict_data['first_name']
        self.last_name = dict_data['last_name']
        self.phone = dict_data['phone']
        self.id = User.auto_id
        self.observers = []
        self.courses = dict_data['courses']
        self.email = dict_data['email']
        User.auto_id += 1


class Teacher(User, Subject):

    def __init__(self, dict_data):
        super().__init__(dict_data)
        self.students = dict_data['students']

    def add_teacher(self, site):
        self.notify_teacher(site)


class Student(User, Subject):
    """Class Student - creates a Student object."""

    def __init__(self, dict_data):
        super().__init__(dict_data)
        self.age = dict_data['age']

    def add_student(self, site):
        self.notify_student(site)


class UserFactory:
    """The Abstract Factory class is a user factory."""

    types = {
        'student': Student,
        'teacher': Teacher
    }

    @classmethod
    def create(cls, type_, dict_data):
        """The function creates the desired user class."""
        return cls.types[type_](dict_data)


class Course:
    """Class Course - creates a Course object."""

    auto_id = 0

    def __init__(self, name, course_type):
        self.name = name
        self.type = course_type
        self.id = Course.auto_id
        Course.auto_id += 1
        super().__init__()


class CourseType:
    """Class CourseType - creates a CourseType object."""
    auto_id = 0

    def __init__(self, param):
        self.name = param
        self.id = CourseType.auto_id
        CourseType.auto_id += 1


# Abstract classes courses.
class InteractiveCourse(Course):
    pass


class RecordCourse(Course):
    pass


class CourseFactory:
    """The Abstract Factory class is a course factory."""

    types = {
        'interactive': InteractiveCourse,
        'record': RecordCourse
    }

    @classmethod
    def create(cls, type_, name, category):
        """
        The function creates the desired course class.

        :param type_: str: course type - to be created,
        :param name: str: course of category,
        :param category: str: name of category,
        :return: returns an object of the created class.
        """

        return cls.types[type_](name, category)


class Category:
    """Class category - creates a Category object."""

    auto_id = 0

    def __init__(self, name, courses):
        self.name = name
        self.courses = courses
        self.teachers = []
        self.id = Category.auto_id
        Category.auto_id += 1


class Engine:
    """A class containing the main interface of the project."""

    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []
        self.type_courses = []

    @staticmethod
    def type_course(param):
        """
        Function for getting the course type.

        :param param: str: type name,
        :return: returns a course type object.
        """

        return CourseType(param)

    def type_course_delete(self, id):
        """
        Deletes the course type.

        :param id: id of type course,
        :return: returns an updated list of course types.
        """

        for item in self.type_courses:
            if item.id == id:
                self.type_courses.pop(id)
                return self.type_courses
        raise Exception(f'There is no course type with id = {id}.')

    def type_course_detail(self, id):
        """
        Detailing the course type.

        :param id: id of type course,
        :return: returns the course object.
        """

        for item in self.type_courses:
            if item.id == id:
                return item
        raise Exception(f'There is no course type with id = {id}.')

    def type_course_update(self, id, name):
        """
        Updating course type data.

        :param id: id of type course,
        :param name: str: new name of type course,
        :return: returns an updated list of course types.
        """

        for item in self.type_courses:
            if item.id == id:
                item.name = name
                return self.type_courses
        raise Exception(f'There is no course type with id = {id}.')

    def find_type_course_by_id(self, id):
        """
        Search for a certain type of course by id.

        :param id: id of type course,
        :return: returns the course object.
        """

        for item in self.type_courses:
            if item.id == id:
                return item
        raise Exception(f'There is no course type with id = {id}.')

    def type_course_create(self, name):
        """A function that starts the creation of a type course.

        :param name: str: name of type course.
        """

        return CourseType(name)

    def create_course(self, name, type_):
        """
        A function that starts the creation of a course.

        :param name: str: name of course,
        :param type_: str: type of course.
        """

        return Course(name, type_)

    def copy_course(self, id):
        """
        The function of copy a course by id.

        :param id: id of course,
        """

        for item in self.courses:
            if item.id == id:
                new_name = f'Copy_{item.name}.'
                new_type = item.type
                return Course(new_name, new_type)
        raise Exception(f'There is no course with id = {id}.')

    def course_detail(self, id):
        """
        Detailing the course.

        :param id: id course,
        :return: returns the course object.
        """

        for item in self.courses:
            if item.id == id:
                return item
        raise Exception(f'There is no course with id = {id}.')

    def course_update(self, id, name, type_):
        """
        Updating course data.

        :param id: id of type course,
        :param name: str: new name of type course,
        :param type_: list: new type of course,
        :return: returns an updated list of course types.
        """

        for item in self.courses:
            if item.id == id:
                item.name = name
                item.type = type_
                return self.courses
        raise Exception(f'There is no course with id = {id}.')

    def delete_course(self, id):
        """
        The function of deleting a course by id.

        :param id: id of course,
        :return: returns list of courses.
        """

        for item in self.courses:
            if item.id == id:
                self.courses.pop(id)
                return self.courses
        raise Exception(f'There is no course with id = {id}.')

    def get_course(self, name):
        """
        Getting a course by name.

        :param name: name of course,
        :return: returns object of course or None.
        """

        for item in self.courses:
            if item.name == name:
                return item
        return None

    def find_course_by_id(self, id):
        """
        Search for a certain course by id.

        :param id: id course,
        :return: returns the course object.
        """

        for item in self.courses:
            if item.id == id:
                return item
        raise Exception(f'There is no course type with id = {id}.')

    @staticmethod
    def create_user(type_, dict_data):
        """
        A function that triggers the creation of a user.

        :param type_: str: user type - to be created.
        :param dict_data: dict: data of created to user.
        """

        return UserFactory.create(type_, dict_data)

    def student_delete(self, id):
        """
        The function of deleting a student by id.

        :param id: id student,
        :return: returns list of students.
        """

        for item in self.students:
            if item.id == id:
                self.students.pop(id)
                return self.students
        raise Exception(f'There is no student with id = {id}.')

    def student_detail(self, id):
        """
        Detailing the student.

        :param id: id student,
        :return: returns the student object.
        """

        for item in self.students:
            if item.id == id:
                return item
        raise Exception(f'There is no student with id = {id}.')

    def student_update(self, id, first_name, last_name, age, courses, email,
                       phone):
        """
        Updating data of the student.

        :param id: id student,
        :param first_name: first_name of student,
        :param last_name: last_name of student,
        :param age: age of student,
        :param courses: the course in which the student studies,
        :param email: email of student,
        :param phone:phone number of student,
        :return: returns list of students.
        """

        for item in self.students:
            if item.id == id:
                item.first_name = first_name
                item.last_name = last_name
                item.age = age
                item.courses = courses
                item.email = email
                item.phone = phone
                return self.students
        raise Exception(f'There is no student with id = {id}.')

    def find_student_by_id(self, id):
        """
        Search for a certain student by id.

        :param id: id student,
        :return: returns the student object.
        """

        for item in self.students:
            if item.id == id:
                return item
        raise Exception(f'There is no student type with id = {id}.')

    def teacher_delete(self, id):
        """
        The function of deleting a teacher by id.

        :param id: id teacher,
        :return: returns list of teachers.
        """

        for item in self.teachers:
            if item.id == id:
                self.teachers.pop(id)
                return self.teachers
        raise Exception(f'There is no teacher with id = {id}.')

    def teacher_detail(self, id):
        """
        Detailing the teacher.

        :param id: id teacher,
        :return: returns the teacher object.
        """

        for item in self.teachers:
            if item.id == id:
                return item
        raise Exception(f'There is no teacher with id = {id}.')

    def teacher_update(self, id, first_name, last_name, students, courses,
                       email,
                       phone):
        """
        Updating data of the teacher.

        :param id: id teacher,
        :param first_name: first_name of teacher,
        :param last_name: last_name of teacher,
        :param students: the students in which the teacher studies,
        :param courses: list of students who study with a teacher,
        :param email: email of teacher,
        :param phone:phone number of teacher,
        :return: returns list of teacher.
        """

        for item in self.teachers:
            if item.id == id:
                item.first_name = first_name
                item.last_name = last_name
                item.students = students
                item.courses = courses
                item.email = email
                item.phone = phone
                return self.teachers
        raise Exception(f'There is no teacher with id = {id}.')

    def find_teacher_by_id(self, id):
        """
        Search for a certain teacher by id.

        :param id: id teacher,
        :return: returns the teacher object.
        """

        for item in self.teachers:
            if item.id == id:
                return item
        raise Exception(f'There is no teacher type with id = {id}.')

    @staticmethod
    def create_category(name, courses=None):
        """A function that starts the creation of a category."""

        return Category(name, courses)

    def category_detail(self, id):
        """
        Detailing the category.

        :param id: id course,
        :return: returns the category object.
        """

        for item in self.categories:
            if item.id == id:
                return item
        raise Exception(f'There is no category with id = {id}.')

    def category_update(self, id, name, courses):
        """
        Updating category data.

        :param id: id category,
        :param name: str: new name category,
        :param courses: list: new list of courses,
        :return: returns an updated list of courses.
        """

        for item in self.categories:
            if item.id == id:
                item.name = name
                item.courses = courses
                return self.categories
        raise Exception(f'There is no category with id = {id}.')

    def category_delete(self, id):
        """
        The function of deleting a category by id.

        :param id: id category,
        :return: returns list of categories.
        """

        for item in self.categories:
            if item.id == id:
                self.categories.pop(id)
                return self.categories
        raise Exception(f'There is no category with id = {id}.')

    def find_category_by_id(self, id):
        """
        The function of searching for the desired category by id.

        :param id: int: id category,
        :return: returns the desired category or error.
        """

        for item in self.categories:
            # print('item', item.id)
            if item.id == id:
                return item
        raise Exception(f'There is no category with this id: {id}')

    @staticmethod
    def decode_value(val):
        """
        A function that performs value decoding.

        :param val: str: string with value,
        :return: returns string of value.
        """

        val_b = bytes(val.replace('%', '=').replace('+', ' '), 'UTF-8')
        val_decode_str = quopri.decodestring(val_b)
        return val_decode_str.decode('UTF-8')


class SingletonByName(type):
    """
    Singleton class - checking for the presence of the desired class.

    If the required class is found, it returns it.
    Otherwise creates a new class.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']

        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class Logger(metaclass=SingletonByName):

    def __init__(self, name, writer=ConsoleWriter(),
                 writer_file=FileWriter('logs.txt')):
        self.name = name
        self.writer = writer
        self.writer_file = writer_file

    def log(self, text):
        self.writer.write(text)
        self.writer_file.write(text)
