# Создаем пустой список и счётчик заголовков для корректного вывода значений
# Также создаем флаг для проверки включения элемента в список. Если элемента нет в списке: flag = True. По умолчанию flag = True.
name_list = []
counter = 0
flag = True
# Формируем цикл ввода заголовков с выходом из цикла при помощи "stop".
# Счётчик считает наши заголовки для корректного вывода результата.
while True:
    name = input("Введите заголовок заметки, stop для завершения: ")
    if name.lower() == "stop":
        break
    for el in name_list:
        if el.lower() == name.lower():
            flag = False
    if flag == True:
        name_list.append(name)
        counter += 1
    flag = True

# Проверка количества заголовков
if counter > 0:
    print("Заголовки заметки:")
else:
    print("Заголовков нет")
# Вывод заголовков, пустота если список без заголовков
for name in name_list:
    print("-", name)
