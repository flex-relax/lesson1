# Импортируем модуль datetime для сравнения дат
import datetime as DT

# Вводим дату и создаем объект datetime методом класса strptime
issue_date = input("Введите дату завершения заметки (dd.mm.yyyy)\n")
deadline = DT.datetime.strptime(issue_date, "%d.%m.%Y").date()
now = DT.datetime.now()
print(now)
print(deadline)
# Сравниваем текущую дату с дедлайном и выводим соответствующее сравнению сообщение
if (
    now.day > deadline.day
    and now.month >= deadline.month
    and now.year >= deadline.year
    or now.day < deadline.day
    and now.month > deadline.month
    and now.year >= deadline.year
    or now.year > deadline.year
    or now.month < deadline.month
    and now.year > deadline.year
):
    print("Срок выполнения заметки истёк")
else:
    print("Заметка в процессе")
