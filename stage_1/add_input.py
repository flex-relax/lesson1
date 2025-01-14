# Инициализация заголовков и переменных для заметки
list_title = [
    input("Введите 1-ый заголовок заметки: "),
    input("Введите 2-ой заголовок заметки: "),
    input("Введите 3-ий заголовок заметки: "),
]
content = input("Введите текст: ")
temp_created_date = input("Введите дату создания заметки в формате дд.мм.гг:")
temp_issue_date = input("Введите дату завершения заметки в формате дд.мм.гг:")

# Редактируем формат даты по типу: дд.мм
created_date = temp_created_date.replace(temp_created_date[2], ".")
issue_date = temp_issue_date.replace(temp_issue_date[2], ".")

# Выводим переменные
print("Первый заголовок: ", list_title[0])
print("Второй заголовок: ", list_title[1])
print("Третий заголовок: ", list_title[2])
print("Текст: ", content)
print("Дата создания заметки: ", created_date[:5])
print("Дата завершения заметки: ", issue_date[:5])
