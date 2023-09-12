from controls import *


def main():
    while True:
        print('1.Проект 2.Договор 7.Список проектов 8.Список договоров 0.Завершить работу с программой')
        command = input('Введите номер команды: ')
        if command == '1':
            while True:
                print('1.Создать проект 2.Добавить договор в проект 3.Завершить договор выбранного проекта '
                      '7.Список проектов 8.Список договоров 0.Вернуться')
                command_1 = input('Введите номер команды: ')
                if command_1 == '0':
                    break
                elif command_1 == '1':
                    create_project()
                elif command_1 == '2':
                    add_contract()
                elif command_1 == '3':
                    complete_project_contract()
                elif command_1 == '7':
                    view_projects()
                elif command_1 == '8':
                    view_contracts()
                else:
                    print('Неверный номер команды')
        elif command == '2':
            while True:
                print('1.Создать договор 2.Подтвердить договор 3.Завершить договор 7.Список проектов '
                      '8.Список договоров 0.Вернуться')
                command_2 = input('Введите номер команды: ')
                if command_2 == '0':
                    break
                elif command_2 == '1':
                    create_contract()
                elif command_2 == '2':
                    confirm_contract()
                elif command_2 == '3':
                    complete_contract()
                elif command_2 == '7':
                    view_projects()
                elif command_2 == '8':
                    view_contracts()
                else:
                    print('Неверный номер команды')
        elif command == '3':

            complete_contract()
        elif command == '7':
            view_projects()
        elif command == '8':
            view_contracts()
        elif command == '0':
            break
        else:
            print('Неверный номер команды')


if __name__ == '__main__':
    main()
