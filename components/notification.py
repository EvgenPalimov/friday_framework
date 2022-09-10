import jsonpickle as jsonpickle


class Observer:
    """Abstract class - to enable the update method."""

    def update(self, subject):
        pass


class Subject:
    """Signal class - informs users."""

    def __init__(self):
        self.observers = []

    def notify_student(self, site):
        text = 'You have joined the course'
        for item in self.observers:
            item.update(self, text, site, 'student')

    def notify_teacher(self, site):
        text = 'You have a new teacher.'
        for item in self.observers:
            item.update(self, text, site, 'teacher')


class SmsNotifier(Observer):
    """Class SmsNotifier - informing the user by sending sms."""

    def update(self, subject):
        """Function - sending sms."""

        print('SMS-->', 'joined us.')


class EmailNotifier(Observer):
    """Class EmailNotifier - informing the user by sending email."""

    def update(self, subject, text, site, type_data):
        """
        Function - sending e-mail.

        :param subject: subject of
        :param text: text of email message,
        :param site: subject of site,
        :param type_data: type of subject to send message.
        """
        if type_data == 'student':
            for course in subject.courses:
                print(f'Email-->{text}',
                      site.find_course_by_id(int(course.id)).name)

        elif type_data == 'teacher':
            for student in subject.students:
                print(f'Email-->{text}',
                      site.find_student_by_id(int(student.id)).last_name)
        else:
            pass


class BaseSerializer:
    """
    BaseSerializer the basic serializer class.

    Saving and loading data from the format jsonpickle.
    """

    def __init__(self, obj):
        self.obj = obj

    def save(self):
        """The function saves data in jsonpickle."""

        return jsonpickle.dumps(self.obj)

    @staticmethod
    def load(data):
        """
        The function loads the data in jsonpickle.

        :param data: data of the format jsonpickle.
        """
        return jsonpickle.loads(data)


class ConsoleWriter:
    """ConsoleWriter the class of information output to the console."""

    def write(self, text):
        """
        Function - displaying information in the console.

        :param text: text of message.
        """
        print(text)


class FileWriter:
    """ConsoleWriter the class saves data to a file."""

    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, text):
        """
        Functions saves data to a txt file.

        :param text: the text to be recorded.
        """
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(f'{text}\n')
