from controls import *


def main():
    command = 'Меню'
    command_1 = 'Меню'
    while True:
        try:
            match command:
                case 'Меню':
                    com = show_menu(command)
                    command_1 = command
                    command = menu[command][com]
                case 'Проект':
                    com = show_menu(command)
                    command_1 = command
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
                    command_1 = command
                    command = menu[command][com]
                case 'Создать договор':
                    create_contract()
                    command = 'Договор'
                case 'Подтвердить договор':
                    confirm_contract()
                    command = 'Договор'
                case 'Завершить договор':
                    complete_contract()
                    command = 'Договор'
                case 'Список проектов':
                    view_projects()
                    command = command_1
                case 'Список договоров':
                    view_contracts()
                    command = command_1
                case 'Вернуться в главное меню':
                    command = 'Меню'
                case 'Завершить работу с программой':
                    break
        except KeyError as e:
            print('Неверный номер команды')
        except ValueError as v:
            print('Команда должна быть целым числом.')


if __name__ == '__main__':
    main()
