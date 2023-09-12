import menu
from controls import *


def main():
    command = 'Меню'
    while True:
        try:
            match command:
                case 'Меню':
                    com = show_menu(command)
                    command = menu[command][com]
                case 'Проект':
                    com = show_menu(command)
                    command = menu[command][com]
                case 'Создать проект':
                    create_project()
                    command = 'Проект'
                case 'Добавить договор в проект':
                    add_contract()
                    command = 'Проект'
                case 'Завершить договор выбранного проекта':
                    complete_project_contract()
                    command = 'Проект'
                case 'Договор':
                    com = show_menu(command)
                    command = menu[command][com]
                case 'Создать договор':
                    create_contract()
                    command = 'Договор'
                case 'Подтвердить договор':
                    confirm_contract()
                    command = 'Договор'
                case 'Завершить договор':
                    complete_contract()
                case 'Список проектов':
                    view_projects()
                    command = 'Меню'
                case 'Список договоров':
                    view_contracts()
                    command = 'Меню'
                case 'Вернуться в главное меню':
                    command = 'Меню'
                case 'Завершить работу с программой':
                    break
        except KeyError as e:
            print('Неверный номер команды')
        except ValueError as v:
            print('Неверный номер команды')


if __name__ == '__main__':
    main()
