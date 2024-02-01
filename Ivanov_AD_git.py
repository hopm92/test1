import os
import shutil
def print_menu():
    print('1. Создать файл')
    print('2. Удалить файл')
    print('3. Переместить файл')
    print('4. Копировать файл')
    print('5. Создать папку')
    print('6. Удалить папку')
    print('7. Переместить папку')
    print('8. Копировать папку')
    print('9. Выйти')

def main():
    while True:
        print_menu()
        choice = input('Введите номер команды: ')
        if choice == '1':
            file_path = input('Укажите путь к файлу: ')
            create_file(file_path)
        if choice == '2':
            file_path = input('Укажите путь к файлу: ')
            delete_file(file_path)