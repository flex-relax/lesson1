# Создадим флаг для отслеживания изменения статуса заметки и статус по умолчанию
flag = True
status = "в процессе"

# Инициализируем cписок и даты для заметки
list_title = [input("Введите название заметки: "), input("Введите название заметки: ")]
temp_created_date = input("Введите дату создания заметки в формате дд.мм.гг:")
temp_issue_date = input("Введите дату завершения заметки в формате дд.мм.гг:")

# Преобразуем даты к виду дд.мм
created_date = temp_created_date.replace(temp_created_date[2], ".")
issue_date = temp_issue_date.replace(temp_issue_date[2], ".")

# Вводим статус заметки и получаем результат
print(f'Текущий статус заметки: "{status}"')

new_status = input(
    "Выберите новый статус заметки:\n1. выполнено \n2. в процессе\n3. отложено\n"
)

if new_status == "1" or new_status == "выполнено":
    status = "выполнено"
elif new_status == "2" or new_status == "в процессе":
    print("Статус заметки не обновлён")
    flag = False
elif new_status == "3" or new_status == "отложено":
    status = "отложено"
else:
    print("Некорректное значение, повторите попытку")
    flag = False

if flag == True:
    print("Ваш выбор: ", new_status)
    print("Статус заметки успешно обновлён: ", status)
