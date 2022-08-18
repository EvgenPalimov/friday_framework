import copy


# Abstract classes users.
import quopri


class User:
    pass


class Teacher(User):
    pass


class Student(User):
    pass


class UserFactory:
    """The Abstract Factory class is a user factory."""

    types = {
        'student': Student,
        'teacher': Teacher
    }

    @classmethod
    def create(cls, type_):
        """The function creates the desired user class."""
        return cls.types[type_]()


class CoursePrototype:
    """The Prototype class is a prototype of training courses."""

    def clone(self):
        return copy.deepcopy(self)


class Course(CoursePrototype):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)


# Abstract classes courses.
class InteractiveCourse(Course):
    pass


class RecordCourse(Course):
    pass


class Category:
    """
    Class category - initializes data and counts the
    number of courses in the category.
    """

    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []

    def course_count(self):
        """
        The function counts the total number of courses.

        :return: int: returns an update of the number of courses.
        """

        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result


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


class Engine:
    """A class containing the main interface of the project."""

    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []

    @staticmethod
    def create_user(type_):
        """
        A function that triggers the creation of a user.

        :param type_: str: user type - to be created.
        """
        return UserFactory.create(type_)

    @staticmethod
    def create_category(name, category=None):
        """
        A function that starts the creation of a category.

        :param name: str: name of category,
        :param category:
        """
        return Category(name, category)

    def find_category_by_id(self, id):
        """
        The function of searching for the desired category via id.

        :param id: int: id category,
        :return: returns the desired category or error.
        """
        for item in self.categories:
            print('item', item.id)
            if item.id == id:
                return item
        raise Exception(f'There is no category with this id: {id}')

    @staticmethod
    def create_course(type_, name, category):
        """
        A function that starts the creation of a course.

        :param name: str: name of course,
        :param category: str: name of category.
        """

        return CourseFactory.create(type_, name, category)

    def get_course(self, name):
        """
        A function that searches for and returns the desired course.

        :param name: str: name of course,
        :return: returns the desired course or None.
        """
        for item in self.courses:
            if item.name == name:
                return item
        return None

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

    def __init__(self, name):
        self.name = name

    @staticmethod
    def log(text):
        print('log--->', text)