import datetime as DT

date_str = input("Введите дату завершения заметки (dd.mm.yyyy)\n")
vypusk = DT.datetime.strptime(date_str, "%d.%m.%Y").date()
now = DT.datetime.now()
print(now)
print(vypusk)
if (
    now.day > vypusk.day
    and now.month >= vypusk.month
    and now.year >= vypusk.year
    or now.day < vypusk.day
    and now.month > vypusk.month
    and now.year >= vypusk.year
    or now.year > vypusk.year
    or now.month < vypusk.month
    and now.year > vypusk.year
):
    print("Срок выполнения заметки истёк")
else:
    print("Заметка в процессе")
