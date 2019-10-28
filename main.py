"""
Домашнее задание № 5 - Трясцын Владимир
"""
import dz_lib
import module.my_bill as game_bill
import module.victory as game_victory


# Меню программы
while True:
    dz_lib.show_help()
    response = input('Укажите пункт меню -> ')
    if response == '1':  # Создать папку
        dz_lib.create_dir()
    elif response == '2':  # Удалить (файл/папку)
        dz_lib.del_file_or_dir()
    elif response == '3':  # Копировать (файл/папку)
        dz_lib.copy_file_or_dir()
    elif response == '4':  # Просмотр содержимого рабочей директории
        dz_lib.find_all_in_current_dir()
    elif response == '5':  # Посмотреть только папки
        dz_lib.get_dir_in_current_dir()
    elif response == '6':  # Посмотреть только файлы
        dz_lib.get_files_in_current_dir()
    elif response == '7':  # Просмотр информации об операционной системе
        dz_lib.get_system_info()
    elif response == '8':  # Создатель программы
        print(f"Создатель программы: Трясцын Владимир")
        print(f"Дата создания программы: 25.10.2019")
        print()
    elif response == '9':  # Играть в викторину
        answer = input('Укажите количество вопросов в викторине: -> ')
        if answer.isdigit():
            count_questions = int(answer)
            if (count_questions >= 10) | (count_questions < 2):
                print("В викторине будет 5 вопросов")
                game_victory.victory_run()
            else:
                game_victory.victory_run(count_questions)
    elif response == '10':  # Мой банковский счет
        game_bill.my_bill_run()
    elif response == '11':  # Смена рабочей директории
        dz_lib.change_current_dir()
    elif response == '0':  # Выход
        print('Программа завершается!')
        break
    else:
        print("Не корректный вод пункта меню. Повторите ввод.")
