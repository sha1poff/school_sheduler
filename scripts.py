# Импортируем библиотеки
from openpyxl import load_workbook
from string import ascii_uppercase


wb = load_workbook(r'assets\src\shedule.xlsx')
sheet_students = wb['students']
sheet_teachers = wb['teachers']

first_alphabet = ascii_uppercase
second_alphabet = ''.join(map(lambda x: f'A{x}', ascii_uppercase))

# Создаем словарь с классами
classes = {}  # Словарь с классами
for letter in first_alphabet + second_alphabet:  # Цикл по буквам колонн
    pos = f'{letter}1'  # Позиция
    _class = sheet_students[pos].value  # Значение ячейки
    if _class:  # Если значение не пустое
        classes[_class.lower()] = pos  # Сохраняем класс и его позицию
    else:  # Иначе цикл заканчивается
        break

# Создаем словарь с учителями
teachers = {}
for row_index in range(1, 52 + 1):
    data = sheet_teachers[f'A{row_index}'].value
    surname = data[:data.find(' ')].lower()
    if surname:
        teachers[surname] = f'A{row_index}'
    else:
        break

# Создаем список со значениями номеров строк для каждого урока
row_range_list = []
start_num = 2
for i in range(5):
    row_range_list.append([start_num, start_num + 8])
    start_num += 8
row_range_list = map(lambda x: range(*x), row_range_list)

# Создаем список со значениями букв столбцов для каждого урока
columns = [
    'B C D E F G H I',
    'J K L M N O P Q',
    'R S T U V W X Y',
    'Z AA AB AC AD AE AF AG',
    'AH AI AJ AK AL AM AN AO'
]
column_range_list = map(lambda x: x.split(' '), columns)


# Парсим лист с учениками
def parse_student(cls: str):
    result = []
    if cls.lower() in classes.keys():
        for row_range in row_range_list:
            lesson_index = 0
            day_shedule = ''
            for row_index in row_range:
                lesson_index += 1
                column_letter = classes[cls.lower()][0]
                lesson = sheet_students[f'{column_letter}{row_index}'].value
                day_shedule += f' {lesson_index}. {lesson}\n'
            result.append(day_shedule[:-1])
        return result
    else:
        pass


def parse_teacher(teacher):
    result = []
    if teacher.lower() in teachers.keys():
        for column_range in column_range_list:
            lesson_index = 0
            day_shedule = ''
            for column_letter in column_range:
                lesson_index += 1
                row_index = teachers[teacher.lower()][1:]
                lesson = sheet_teachers[f'{column_letter}{row_index}'].value
                lesson = lesson[:lesson.find(' ')] + lesson[lesson.find(' '):]
                day_shedule += f'   {lesson_index}. {lesson}\n'
            result.append(day_shedule[:-1])
        return result
    else:
        pass
