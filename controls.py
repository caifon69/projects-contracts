import datetime
from datetime import datetime

from pony.orm import *

from menu import menu
from models import Contract, Project


def show_menu(command):
    for n, command in menu[command].items():
        print(f'{n}. {command}', end=' ')
    print()
    com = int(input('Введите номер команды: '))
    return com


@db_session
def create_contract():
    name_contract = input('Введите название договора: ')
    if name_contract not in select(c.name_contract for c in Contract):
        Contract(name_contract=name_contract, date_of_creation=datetime.now().date(), contract_status='Черновик')
        print(f'Создан договор с именем {name_contract}.')
    else:
        print(f'Договор с именем {name_contract} уже существует.')


@db_session
def view_contracts():
    print('Таблица договоров.')
    select(c for c in Contract).show()


@db_session
def add_contract():
    name_project = input('Введите имя проекта: ')
    if name_project in select(p.name_project for p in Project):
        project = Project.get(name_project=name_project)
        for c in project.contracts:
            if c.contract_status == 'Активен':
                print(f'В проекте {name_project} уже есть активный договор.')
                break
        else:
            name_contract = input('Введите имя договора: ')
            if name_contract in select(c.name_contract for c in Contract):
                contract = Contract.get(name_contract=name_contract)
                if contract.project is None:
                    if contract.contract_status == 'Активен':
                        contract.project = project
                        print(f'Договор {name_contract} добавлен в проект {name_project}.')
                    else:
                        print('Договор должен быть активен.')
                else:
                    print(f'Договор {name_contract} уже добавлен в проект.')
            else:
                print(f'Нет договора с именем {name_contract}.')
    else:
        print(f'Нет проекта с именем {name_project}')


@db_session
def create_project():
    if 'Активен' in select(c.contract_status for c in Contract):
        name_project = input('Введите название проекта: ')
        if name_project not in select(p.name_project for p in Project):
            Project(name_project=name_project, date_of_creation=datetime.now().date())
            print(f'Создан проект с именем {name_project}.')
        else:
            print(f'Проект с именем {name_project} уже существует.')
    else:
        print('Нет активных договоров. Не возможно создать проект.')


@db_session
def view_projects():
    print('Таблица проектов.')
    select(p for p in Project).show()


@db_session
def confirm_contract():
    name_contract = input('Введите название договора: ')
    if name_contract in select(c.name_contract for c in Contract):
        contract = Contract.get(name_contract=name_contract)
        if contract.contract_status == 'Черновик':
            contract.contract_status = 'Активен'
            contract.date_of_signing = datetime.now().date()
            print(f'Статус договора {name_contract} изменен.')
        else:
            print(f'Договор {name_contract} уже подтвержден.')
    else:
        print(f'Нет договора с именем {name_contract}.')


@db_session
def complete_contract():
    name_contract = input('Введите название договора: ')
    if name_contract in select(c.name_contract for c in Contract):
        contract = Contract.get(name_contract=name_contract)
        if contract.contract_status != 'Завершен':
            contract.contract_status = 'Завершен'
            print(f'Статус договора {name_contract} изменен.')
        else:
            print(f'Договор {name_contract} уже завершен.')
    else:
        print(f'Нет договора с именем {name_contract}.')


@db_session
def complete_project_contract():
    name_project = input('Введите имя проекта: ')
    if name_project in select(p.name_project for p in Project):
        project = Project.get(name_project=name_project)
        name_contract = input('Введите имя договора: ')
        if name_contract in select(c.name_contract for c in Contract if c.project == Project[project.id]):
            contract = Contract.get(name_contract=name_contract)
            if contract.contract_status != 'Завершен':
                contract.contract_status = 'Завершен'
                print(f'Статус договора {name_contract} изменен.')
            else:
                print(f'Договор {name_contract} уже завершен.')
        else:
            print(f'В проекте {name_project} нет договора с таким именем.')
    else:
        print(f'Нет проекта с именем {name_project}.')
