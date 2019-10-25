"""
Домашнее задание № 5 - Трясцын Владимир
"""
import dz_lib


# Меню программы
while True:
    dz_lib.show_help()
    response = input('Укажите пункт меню -> ')
    if response == '1':  # Создать папку
        dz_lib.create_dir()
    elif response == '2':  # Удалить (файл/папку)
        dz_lib.del_file_or_dir()
    elif response == '3':  # Копировать (файл/папку)
        pass
    elif response == '4':  # Просмотр содержимого рабочей директории
        pass
    elif response == '5':  # Посмотреть только папки
        pass
    elif response == '6':  # Посмотреть только файлы
        pass
    elif response == '7':  # Просмотр информации об операционной системе
        pass
    elif response == '8':  # Создатель программы
        pass
    elif response == '9':  # Играть в викторину
        pass
    elif response == '10':  # Мой банковский счет
        pass
    elif response == '11':  # Смена рабочей директории
        pass
    elif response == '0':  # Выход
        print('Программа завершается!')
        break
    else:
        print("Не корректный вод пункта меню. Повторите ввод.")
