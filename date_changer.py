#Вводим даты для заметки
temp_created_date = input("Введите дату создания заметки в формате дд.мм.гг:")
temp_issue_date = input("Введите дату завершения заметки в формате дд.мм.гг:")

#Преобразуем даты к виду дд.мм
created_date = temp_created_date.replace(temp_created_date[2], ".")
issue_date = temp_issue_date.replace(temp_issue_date[2], ".")

#Выводим данные
print(
    "Дата создания заметки:",
    created_date[:5],
    "\nДата завершения заметки: ",
    issue_date[:5],
)
