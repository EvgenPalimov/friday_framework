import quopri
import sqlite3

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


class CourseType:
    """Class CourseType - creates a CourseType object."""

    def __init__(self, id, param):
        self.id = id
        self.name = param


class Course:
    """Class Course - creates a Course object."""

    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type


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

    # @staticmethod
    # def type_course(param):
    #     """
    #     Function for getting the course type.
    #
    #     :param param: str: type name,
    #     :return: returns a course type object.
    #     """
    #
    #     return CourseType(param)
    #
    # def type_course_delete(self, id):
    #     """
    #     Deletes the course type.
    #
    #     :param id: id of type course,
    #     :return: returns an updated list of course types.
    #     """
    #
    #     for item in self.type_courses:
    #         if item.id == id:
    #             self.type_courses.pop(id)
    #             return self.type_courses
    #     raise Exception(f'There is no course type with id = {id}.')
    #
    # def type_course_detail(self, id):
    #     """
    #     Detailing the course type.
    #
    #     :param id: id of type course,
    #     :return: returns the course object.
    #     """
    #
    #     for item in self.type_courses:
    #         if item.id == id:
    #             return item
    #     raise Exception(f'There is no course type with id = {id}.')
    #
    # def type_course_update(self, id, name):
    #     """
    #     Updating course type data.
    #
    #     :param id: id of type course,
    #     :param name: str: new name of type course,
    #     :return: returns an updated list of course types.
    #     """
    #
    #     for item in self.type_courses:
    #         if item.id == id:
    #             item.name = name
    #             return self.type_courses
    #     raise Exception(f'There is no course type with id = {id}.')
    #
    # def find_type_course_by_id(self, id):
    #     """
    #     Search for a certain type of course by id.
    #
    #     :param id: id of type course,
    #     :return: returns the course object.
    #     """
    #
    #     for item in self.type_courses:
    #         if item.id == id:
    #             return item
    #     raise Exception(f'There is no course type with id = {id}.')
    #
    # def type_course_create(self, name):
    #     """A function that starts the creation of a type course.
    #
    #     :param name: str: name of type course.
    #     """
    #
    #     return CourseType(name)
    #
    # def create_course(self, name, type_):
    #     """
    #     A function that starts the creation of a course.
    #
    #     :param name: str: name of course,
    #     :param type_: str: type of course.
    #     """
    #
    #     return Course(name, type_)
    #
    # def copy_course(self, id):
    #     """
    #     The function of copy a course by id.
    #
    #     :param id: id of course,
    #     """
    #
    #     for item in self.courses:
    #         if item.id == id:
    #             new_name = f'Copy_{item.name}.'
    #             new_type = item.type
    #             return Course(new_name, new_type)
    #     raise Exception(f'There is no course with id = {id}.')
    #
    # def course_detail(self, id):
    #     """
    #     Detailing the course.
    #
    #     :param id: id course,
    #     :return: returns the course object.
    #     """
    #
    #     for item in self.courses:
    #         if item.id == id:
    #             return item
    #     raise Exception(f'There is no course with id = {id}.')
    #
    # def course_update(self, id, name, type_):
    #     """
    #     Updating course data.
    #
    #     :param id: id of type course,
    #     :param name: str: new name of type course,
    #     :param type_: list: new type of course,
    #     :return: returns an updated list of course types.
    #     """
    #
    #     for item in self.courses:
    #         if item.id == id:
    #             item.name = name
    #             item.type = type_
    #             return self.courses
    #     raise Exception(f'There is no course with id = {id}.')
    #
    # def delete_course(self, id):
    #     """
    #     The function of deleting a course by id.
    #
    #     :param id: id of course,
    #     :return: returns list of courses.
    #     """
    #
    #     for item in self.courses:
    #         if item.id == id:
    #             self.courses.pop(id)
    #             return self.courses
    #     raise Exception(f'There is no course with id = {id}.')
    #
    # def get_course(self, name):
    #     """
    #     Getting a course by name.
    #
    #     :param name: name of course,
    #     :return: returns object of course or None.
    #     """
    #
    #     for item in self.courses:
    #         if item.name == name:
    #             return item
    #     return None
    #
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


class TypeCoursesMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.table_name = 'type_course'

    def all(self):
        statement = f'SELECT * from {self.table_name}'
        self.cursor.execute(statement)
        result = []
        for item in self.cursor.fetchall():
            id, name = item
            type_course = CourseType(id, name)
            result.append(type_course)
        return result

    def find_by_id(self, id):
        statement = f'SELECT id, name FROM {self.table_name} WHERE id=?'
        self.cursor.execute(statement, (id,))
        result = self.cursor.fetchone()
        if result:
            return CourseType(*result)
        else:
            raise RecordNotFoundException(f'Record with id={id} not found.')

    def insert(self, obj_name):
        statement = f'INSERT INTO {self.table_name} (name) VALUES (?)'
        self.cursor.execute(statement, (obj_name,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, obj):
        statement = f'UPDATE {self.table_name} SET name=? WHERE id=?'
        self.cursor.execute(statement, (obj.name, obj.id))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, obj):
        statement = f'DELETE FROM {self.table_name} WHERE id=?'
        self.cursor.execute(statement, (obj.id,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class CoursesMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.table_course = 'course'
        self.table_type_course = 'type_course'
        self.table_link = 'course_type_course'

    def all(self):
        statement = f'SELECT course.id, course.name, type_course.name ' \
                    f'FROM {self.table_course} ' \
                    f'INNER JOIN {self.table_link} ON {self.table_course}.id = {self.table_link}.course_id ' \
                    f'INNER JOIN {self.table_type_course} ON ' \
                    f'{self.table_link}.type_course_id = {self.table_type_course}.id ' \
                    f'WHERE {self.table_course}.id = {self.table_link}.course_id '
        self.cursor.execute(statement)
        result = []
        id_list = []
        for item in self.cursor.fetchall():
            if (item[0] in id_list) is False:
                id = item[0]
                id_list.append(id)
                name = item[1]
                type_ = []
                type_.append(item[2])
                course = Course(id, name, type_)
                result.append(course)
            else:
                for i in result:
                    if i.id == item[0]:
                        i.type.append(item[2])
        return result

    def find_by_id(self, id):
        statement = f'SELECT course.id, course.name, type_course.name ' \
                    f'FROM {self.table_course} ' \
                    f'INNER JOIN {self.table_link} ON {self.table_course}.id = {self.table_link}.course_id ' \
                    f'INNER JOIN {self.table_type_course} ON ' \
                    f'{self.table_link}.type_course_id = {self.table_type_course}.id ' \
                    f'WHERE {self.table_course}.id=?'
        self.cursor.execute(statement, (id,))
        result = self.cursor.fetchone()
        if result:
            return Course(*result)
        else:
            raise RecordNotFoundException(f'Record with id={id} not found.')

    def insert(self, name, type_list):
        statement = f'INSERT INTO {self.table_course} (name) VALUES (?)'
        self.cursor.execute(statement, (name,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)
        statement = f'SELECT id, name FROM {self.table_course} WHERE name=?'
        id = self.cursor.execute(statement, (name,)).fetchone()[0]
        for type in type_list:
            statement = f'INSERT INTO {self.table_link} ' \
                        f'(course_id, type_course_id) VALUES (?, ?)'
            self.cursor.execute(statement, (id, type))
            try:
                self.connection.commit()
            except Exception as e:
                raise DbCommitException(e.args)

    def update(self, id, name, list_type_course):
        statement = f'DELETE FROM {self.table_course} WHERE id=?'
        self.cursor.execute(statement, (id,))
        statement = f'DELETE FROM {self.table_link} WHERE course_id=?'
        self.cursor.execute(statement, (id,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)
        statement = f'INSERT INTO {self.table_course} (id, name) VALUES (?, ?)'
        self.cursor.execute(statement, (id, name))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)
        for type in list_type_course:
            statement = f'INSERT INTO {self.table_link} ' \
                        f'(course_id, type_course_id) VALUES (?, ?)'
            self.cursor.execute(statement, (id, type))
            try:
                self.connection.commit()
            except Exception as e:
                raise DbCommitException(e.args)

    def delete(self, obj):
        statement = f'DELETE FROM {self.table_course} WHERE id=?'
        self.cursor.execute(statement, (obj.id,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


connection = sqlite3.connect('friday_framework_bd.sqlite')


class MapperRegistry:
    mappers = {
        'type_course': TypeCoursesMapper,
        'course': CoursesMapper
    }

    @staticmethod
    def get_current_mapper(name):
        return MapperRegistry.mappers[name](connection)


class DbCommitException(Exception):
    def __init__(self, message):
        super().__init__(f'Db commit error: {message}')


class DbUpdateException(Exception):
    def __init__(self, message):
        super().__init__(f'Db update error: {message}')


class DbDeleteException(Exception):
    def __init__(self, message):
        super().__init__(f'Db delete error: {message}')


class RecordNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(f'Record not found: {message}')
