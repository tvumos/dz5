"""
Библиотечные функции
"""
import os
import shutil
import sys
import platform


def show_help():
    print('===================================================')
    print('            Консольный файловый менеджер')
    print('===================================================')
    print(' 1 - Создать папку')
    print(' 2 - Удалить (файл/папку)')
    print(' 3 - Копировать (файл/папку)')
    print(' 4 - Просмотр содержимого рабочей директории')
    print(' 5 - Посмотреть только папки')
    print(' 6 - Посмотреть только файлы')
    print(' 7 - Просмотр информации об операционной системе')
    print(' 8 - Создатель программы')
    print(' 9 - Играть в викторину')
    print(' 10 - Мой банковский счет')
    print(' 11 - Смена рабочей директории')
    print(' 0 - Выход')
    print('===================================================')

def create_dir():
    print("")
    answer = input('Укажите имя создаваемой директории -> ')
    temp_dir = os.path.join(os.getcwd(), answer)
    try:
        if os.path.exists(temp_dir):
            print("ПРЕДУПРЕЖДЕНИЕ. Указанная директория уже существует. Укажите другое имя")
        else:
            os.mkdir(temp_dir)
            print("Директория успешно создана")
            print("")
    except:
        print("ПРЕДУПРЕЖДЕНИЕ. Указаны не допустимые символы в имени директории")


def del_file_or_dir():
    print("")
    answer = input('Укажите имя файла или папки для удаления -> ')
    temp_name = os.path.join(os.getcwd(), answer)
    try:
        if os.path.exists(temp_name):       # Объект найден
            if os.path.isfile(temp_name):   # Файл
                os.remove(temp_name)
                print("Файл успешно удалён")
            elif os.path.isdir(temp_name):  # Директория
                shutil.rmtree(temp_name)
                print("Директория успешно удалена")
        else:
            print("ПРЕДУПРЕЖДЕНИЕ. Указанный файл/директория не найдена в текущей директории")
    except:
        print("ОШИБКА. Ошибка удаления файла/папки - отсутствует доступ к объекту")


def copy_file_or_dir():
    print("")
    src_answer = input('Укажите имя исходного файла/папки для копирования -> ')
    dest_answer = input('Укажите новое имя файла/папки -> ')
    if src_answer == dest_answer:
        print("ПРЕДУПРЕЖДЕНИЕ. Исходное имя файла/папки совпадает с конечным именем. Повторите операцию.")
    else:
        src_answer = os.path.join(os.getcwd(), src_answer)
        dest_answer = os.path.join(os.getcwd(), dest_answer)
        if not os.path.exists(src_answer):
            print("ПРЕДУПРЕЖДЕНИЕ. Исходный файл/папка не найден")
        else:
            try:
                if os.path.isfile(src_answer):          # Файл
                    shutil.copy2(src_answer, dest_answer)
                    print("Файл успешно скопирован")
                elif os.path.isdir(src_answer):         # Директория
                    shutil.copytree(src_answer, dest_answer)
                    print("Каталог успешно скопирован")
            except IOError as e:
                print(f'ОШИБКА. Сообщение: {e.strerror}')


def find_all_in_current_dir():
    folders = []
    print("Список директорий и файлов в текущем каталоге (с вложенными файлами/каталогами):")
    for item in os.walk(os.getcwd()):
        folders.append(item)

    for address, dirs, files in folders:
        for dir in dirs:
            for file in files:
                print(f"Директория: {os.path.join(address, dir)}, Файл: {file}")


def get_files_in_current_dir():
    print("Список файлов в текущей директории:")
    print("\n".join(list(filter(lambda x: os.path.isfile(x), os.listdir(".")))))
    print()


def get_dir_in_current_dir():
    print("Список директорий в текущей директории:")
    print("\n".join(list(filter(lambda x: os.path.isdir(x), os.listdir(".")))))
    print()

def get_system_info():
    print()
    print("Информация о системе:")
    ops, name, oper_ver, build, proc, proc_fam = platform.uname()
    print(f"Операционная система: {ops}")
    print(f"Архитектура: {platform.architecture()}")
    print(f"Платформа: {sys.platform}")
    print(f"Версия операционной системы: {oper_ver}")
    print(f"Релиз операционной системы: {build}")
    print(f"Пользователь системы: {name}")
    print()
    print(f"Архитектура процессора: {proc}")
    print(f"Модель процессора: {proc_fam}")
    print()
    print(f"Версия Python: {' от '.join(platform.python_build())}")
    print(f"Версия компилятора Python: {platform.python_compiler()}")
    print(f"Реализация Python: {platform.python_implementation()}")
    print(f"Папка установки интерпретатора Python: {sys.prefix}")
    print()


def change_current_dir():
    dir = os.getcwd()
    print(f"Текущая рабочая директория: {dir}")
    answer = input('Укажите новую рабочую директорию: -> ')
    try:
        os.chdir(answer)
        print(f"Текущая рабочая директория: {os.getcwd()}")
    except BaseException as e:
        print(f'ОШИБКА. Сообщение: {e.strerror}')
        os.chdir(dir)
        print(f"Текущая рабочая директория не изменилась: {os.getcwd()}")

