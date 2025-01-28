# импортируем модуль времени и инициализируем пустой список для хранения и добавления заметок
import time

note_list = []


# Задаем функцию для создания заметок
def create_note(
    username, note_name, note_description, note_status, note_create_date, note_deadline
):
    note_dict = {
        "Имя пользователя": username,
        "Наименование заметки": note_name,
        "Описание заметки": note_description,
        "Статус заметки": note_status,
        "Дата создания заметки": note_create_date,
        "Дедлайн": note_deadline,
    }
    note_list.append(note_dict)
    return note_list


# Инициализируем функцию проверки пользовательского ответа после воода заметки с выводом булевого значения по результату проверки
def check_user_answer():
    answer_flag = False
    user_answer = input("Хотите добавить ещё одну заметку? (да/нет): ")
    if user_answer.lower() == "нет":
        answer_flag = False
    elif user_answer.lower() == "да":
        answer_flag = True
    else:
        print("Некорректный ответ, введите заново")
        user_answer = input("Хотите добавить ещё одну заметкуыыыыыыы? (да/нет): ")
        if user_answer.lower() == "нет":
            answer_flag = False
        if user_answer.lower() == "да":
            answer_flag = True
    return answer_flag


# Инициализируем функцию проверки пустых строк заметки с выводом булевого значения по результату проверки
def check_empty_string(*args):
    for arg in args:
        if arg == "":
            return False
    else:
        return True


while True:
    # Инициализируем переменные
    username = input("Введите имя пользователя: ")
    note_name = input("Введите заголовок заметки: ")
    note_description = input("Введите описание заметки: ")
    note_status = input("Введите статус заметки: новая, в процессе, выполнено ")

    # Ввод дат проверяем на наличие ошибок формата через try except. при ошибке формата даты итерация пропускается и цикл создания заметки запускается заново
    try:
        note_create_date = input("Введите дату создания заметки в формате дд-мм-гг: ")
        note_deadline = input("Введите дедлайн заметки в формате дд-мм-гг: ")
        note_valid_create_date = time.strptime(note_create_date, "%d-%m-%y")
        note_valid_deadline = time.strptime(note_deadline, "%d-%m-%y")
    except ValueError:
        print("Неверный формат данных! Введите данные заново.")
        continue
    # Запускаем функцию проверки строк на пустоту, если есть пустая строка - итерация создания заметки перезапускается
    flag = check_empty_string(
        username,
        note_name,
        note_description,
        note_status,
        note_create_date,
        note_deadline,
    )
    if flag == False:
        print("Вы ввели пустую строку, начните заново")
        continue
    # Проверяем наличие такого же заголовка, если уже есть, вводим новый заголовок
    for note in note_list:
        if note_name == note.get("Наименование заметки"):
            print("Наименование заметки занято, введите заново:")
            note_name = input("Введите заголовок заметки:")
    # Запускаем функцию create_note - создаем заметку
    create_note(
        username,
        note_name,
        note_description,
        note_status,
        note_create_date,
        note_deadline,
    )
    # Присваиваем значение функции check_user_answer переменной answer_flag. Запрашиваем у пользователя продолжить ли заполнение заметок, при слове нет цикл останавливается
    answer_flag = check_user_answer()
    if answer_flag == False:
        break
# Выводим список заметок, только если список с заметками непустой
if len(note_list) != 0:
    print("Список заметок: ")
    # Используя вложенный цикл for вытаскиваем из словаря пары ключ значение построчно с нумерацией по индексу в списке + 1, так как начальный индекс 0
    for elem in note_list:
        print(note_list.index(elem) + 1, ". ", sep="", end="")
        for key, value in elem.items():
            print("{0}: {1}".format(key, value))
