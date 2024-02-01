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
            file_path = input('Укажите путь: ')
            create_file(file_path)
        elif choice == '2':
            file_path = input('Укажите путь к файлу: ')
            delete_file(file_path)
        elif choice == '3':
            src_path = input('Укажите путь к файлу: ')
            dst_path = input('Введите новый путь:  ')
            move_file(src_path, dst_path)
        elif choice == '4':
            src_path = input('Укажите путь к файлу: ')
            dst_path = input('Укажите новый путь к файлу: ')
            copy_file(src_path, dst_path)
        elif choice == '5':
            folder_path = input('Укажите путь: ')
            create_folder(folder_path)
        elif choice == '6':
            folder_path = input('Укажите путь к папке: ')
            delete_folder(folder_path)
        elif choice == '7':
            src_path = input('Укажите путь к папке: ')
            dst_path = input('Укажите новый путь: ')
            move_folder(src_path, dst_path)
        elif choice == '8':
            src_path = input('Укажите путь к папке: ')
            dst_path = input('Укажите новый путь: ')
            copy_folder(src_path, dst_path)
        elif choice == '9':
            break
        else:
            print('Нет такой команды')

if __name__ == '__main__':
    main()

def create_file(file_path):
    with open(file_path, 'w') as f:
        f.write('')
def delete_file(file_path):
    os.remove(file_path)

def move_file(src_path, dst_path):
    shutil.move(src_path, dst_path)

def copy_file(src_path, dst_path):
    shutil.copy(src_path, dst_path)