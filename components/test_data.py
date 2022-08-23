def add_test_data_type_course(site):
    type_data = ['Онлайн','Вебинарный','Видео-курс']
    for i in type_data:
        name = site.decode_value(i)
        new_type = site.type_course(name)
        site.type_courses.append(new_type)


def add_test_data_course(site):
    online = '0'
    vebinar = '1'
    video = '2'

    dict_course = {
        'Python': [online, vebinar, video],
        'Java': [online],
        'JavaScript': [vebinar],
        'C': [online]
    }

    list_course = ['Python','Java','JavaScript','C']

    for i in list_course:
        type_course = dict_course.get(i)
        list_type = []
        for item in type_course:
            list_type.append(site.find_type_course_by_id(int(item)))
        new_course = site.create_course(i,list_type)
        site.courses.append(new_course)



