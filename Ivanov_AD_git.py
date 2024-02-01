import os
import shutil

def create_file(file_path):
    with open(file_path, 'w') as f:
        f.write('')
def delete_file(file_path):
    os.remove(file_path)

def move_file(src_path, dst_path):
    shutil.move(src_path, dst_path)

def copy_file(src_path, dst_path):
    shutil.copy(src_path, dst_path)

def create_folder(folder_path):
    os.mkdir(folder_path)

def delete_folder(folder_path):
    shutil.rmtree(folder_path)

def move_folder(src_path, dst_path):
    shutil.move(src_path, dst_path)

def copy_folder(src_path, dst_path):
    shutil.copytree(src_path, dst_path)

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
            file_path = input('Укажите имя файла: ')
            create_file(file_path)
        elif choice == '2':
            file_path = input('Укажите имя файла: ')
            delete_file(file_path)
        elif choice == '3':
            src_path = input('Укажите имя файла: ')
            dst_path = input('Куда перемещаем? имя папки:  ')
            move_file(src_path, dst_path)
        elif choice == '4':
            src_path = input('Укажите имя файла: ')
            dst_path = input('Куда копируем? имя папки: ')
            copy_file(src_path, dst_path)
        elif choice == '5':
            folder_path = input('Укажите имя папки: ')
            create_folder(folder_path)
        elif choice == '6':
            folder_path = input('Укажите имя папки: ')
            delete_folder(folder_path)
        elif choice == '7':
            src_path = input('Укажите имя папки: ')
            dst_path = input('Куда перемещаем? имя папки: ')
            move_folder(src_path, dst_path)
        elif choice == '8':
            src_path = input('Укажите мя папки: ')
            dst_path = input('Укажите новое имя папки: ')
            copy_folder(src_path, dst_path)
        elif choice == '9':
            break
        else:
            print('Нет такой команды')

if __name__ == '__main__':
    main()