list_title = [
    input("Введите 1-ый заголовок заметки: "),
    input("Введите 2-ой заголовок заметки: "),
    input("Введите 3-ий заголовок заметки: "),
]

temp_created_date = input("Введите дату создания заметки в формате дд.мм.гггг:")
temp_issue_date = input("Введите дату завершения заметки в формате дд.мм.гггг:")

created_date = temp_created_date.replace(temp_created_date[2], ".")
issue_date = temp_issue_date.replace(temp_issue_date[2], ".")

username = input("Введите имя пользователя: ")
content = input("Введите текст: ")
status = input("Введите статус: ")

list_main = (
    username,
    content,
    status,
    created_date[0:5],
    issue_date[0:5],
    list_title,
)

print(
    f"Пользователь: {list_main[0]},\nТекст: {list_main[1]},\nСтатус: {list_main[2]},\nДата создания заметки: {list_main[3]},\nДата завершения заметки: {list_main[4]},\nЗаголовки: {list_main[5]}"
)
