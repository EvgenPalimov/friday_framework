import quopri


# Abstract classes users.

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


class Course:
    auto_id = 0

    def __init__(self, name, course_type):
        self.name = name
        self.type = course_type
        self.id = Course.auto_id
        Course.auto_id += 1


class CourseType:
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
        self.teachers = []

    def course_count(self):
        """
        The function counts the total number of courses.

        :return: int: returns an update of the number of courses.
        """

        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result


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
        :name: str: new name of type course,
        :return: returns an updated list of course types.
        """
        print(f'item{id}, {name}')
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
        Updating course  data.

        :param id: id of type course,
        :name: str: new name of type course,
        :type_: str: new type of course,
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

    @staticmethod
    def create_user(type_):
        """
        A function that triggers the creation of a user.

        :param type_: str: user type - to be created.
        """

        return UserFactory.create(type_)

    @staticmethod
    def create_category(name, category=None):
        """A function that starts the creation of a category."""

        return Category(name, category)

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

    def create_course_with_type(self, type_, name, category):
        """
        A function that triggers the creation of a user.

        :param type_: type of course,
        :param name: name of course,
        :param category: name of category.
        """

        return CourseFactory.create(type_, name, category)

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
