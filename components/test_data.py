# def add_test_data_type_course(site):
#     type_data = ['Онлайн','Вебинарный','Видео-курс']
#     for i in type_data:
#         name = site.decode_value(i)
#         new_type = site.type_course(name)
#         site.type_courses.append(new_type)
#
#
# def add_test_data_course(site):
#     online = '0'
#     vebinar = '1'
#     video = '2'
#
#     dict_course = {
#         'Основы языка Python': [online, vebinar, video],
#         'Алгоритмы и структуры данных на Python. Базовый курс': [online],
#         'Основы реляционных баз данных. MySQL': [vebinar],
#         'Linux. Рабочая станция': [online]
#     }
#
#     list_course = ['Основы языка Python',
#                    'Алгоритмы и структуры данных на Python. Базовый курс',
#                    'Основы реляционных баз данных. MySQL',
#                    'Linux. Рабочая станция']
#
#     for i in list_course:
#         type_course = dict_course.get(i)
#         list_type = []
#         for item in type_course:
#             list_type.append(site.find_type_course_by_id(int(item)))
#         new_course = site.create_course(i,list_type)
#         site.courses.append(new_course)

def add_test_data_category(site):

    list_course_id = [1, 2, 3, 4]
    list_courses = []
    for i in list_course_id:
        course = site.find_course_by_id(i)
        list_courses.append(course)
    name_category = 'programing'
    new_category = site.create_category(name_category, list_courses)
    site.categories.append(new_category)

def add_test_data_students(site):

    list_course_id = [1, 2]
    list_courses = []
    for i in list_course_id:
        course = site.find_course_by_id(int(i))
        list_courses.append(course)

    data = {'first_name': 'Ivan',
                 'last_name': 'Ivanov',
                 'age': '32',
                 'courses': list_courses,
                 'email': 'email@mail.ru',
                 'phone': '01234567891'}

    data_1 = {'first_name': 'Petr',
              'last_name': 'Petrov',
              'age': '22',
              'courses': list_courses,
              'email': 'mail@mail.ru',
              'phone': '01234567892'}

    new_student = site.create_user('student', data)
    new_student_1 = site.create_user('student', data_1)
    site.students.append(new_student)
    site.students.append(new_student_1)

def add_test_data_teachers(site):

    list_course_id = [1, 2, 3]
    list_courses = []
    for i in list_course_id:
        course = site.find_course_by_id(int(i))
        list_courses.append(course)

    data = {'first_name': 'Uegene',
                 'last_name': 'Palimov',
                 'students': site.students,
                 'courses': list_courses,
                 'email': 'email@mail.ru',
                 'phone': '01234567891'}

    new_teacher = site.create_user('teacher', data)
    site.teachers.append(new_teacher)


def start_add_test_data(site):
    list_func = [add_test_data_category,
                 add_test_data_students,
                 add_test_data_teachers]

    for func in list_func:
        func(site)






