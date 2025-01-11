name1 = input("Введите заголовок заметки: ")
name2 = input("Введите заголовок заметки: ")
list_title = (name1, name2)

temp_created_date = input("Введите дату заметки:")
created_date = temp_created_date.replace(temp_created_date[2], ".")

username = input("Введите имя пользователя: ")
text = input("Введите текст: ")
status = input("Введите статус: ")

list_main = (username, text, status, created_date, list_title)

print(list_main)
