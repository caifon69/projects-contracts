import datetime
from datetime import datetime

from pony.orm import *

from models import Contract, Project
from sup import ContractStatus, menu


def show_menu(command):
    """
    Отобразить меню
    """
    for n, command in menu[command].items():
        print(f'{n}. {command}', end=' ')
    print()
    com = int(input('Введите номер команды: '))
    return com


def get_contract():
    """
    Получить договор
    """
    name_contract = input('Введите название договора: ')
    if name_contract in select(c.name_contract for c in Contract):
        return Contract.get(name_contract=name_contract)
    else:
        raise Exception(f'Нет договора с  именем {name_contract}.')


def get_project():
    """
    Получить проект
    """
    name_project = input('Введите имя проекта: ')
    if name_project in select(p.name_project for p in Project):
        return Project.get(name_project=name_project)
    else:
        raise Exception(f'Нет проекта с  именем {name_project}.')


def check_contract_status_for_complete(contract):
    """
    Проверить статус договора для завершения
    """
    if contract.contract_status != ContractStatus.completed:
        contract.contract_status = ContractStatus.completed
        print(f'Статус договора {contract.name_contract} изменен.')
    else:
        print(f'Договор {contract.name_contract} уже завершен.')


@db_session
def create_contract():
    """
    Создать договор
    """
    name_contract = input('Введите название договора: ')
    if name_contract not in select(c.name_contract for c in Contract):
        Contract(name_contract=name_contract, date_of_creation=datetime.now().date(),
                 contract_status=ContractStatus.draft)
        print(f'Создан договор с именем {name_contract}.')
    else:
        print(f'Договор с именем {name_contract} уже существует.')


@db_session
def view_contracts():
    """
    Показать таблицу с договорами
    """
    print('ТАБЛИЦА ДОГОВОРОВ')
    select(c for c in Contract).show()
    print('--+-------------+----------------+---------------+---------------+----------')


@db_session
def add_contract():
    """
    Добавить договор в проект
    """
    try:
        project = get_project()
        for c in project.contracts:
            if c.contract_status == ContractStatus.active:
                print(f'В проекте {project.name_project} уже есть активный договор.')
                break
        else:
            try:
                contract = get_contract()
                if contract.project is None:
                    if contract.contract_status == ContractStatus.active:
                        contract.project = project
                        print(f'Договор {contract.name_contract} добавлен в проект {project.name_project}.')
                    else:
                        print('Договор должен быть активен.')
                else:
                    print(f'Договор {contract.name_contract} уже добавлен в проект.')
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


@db_session
def create_project():
    """
    Создать проект
    """
    if ContractStatus.active in select(c.contract_status for c in Contract):
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
    """
    Показать таблицу с договорами
    """
    print('ТАБЛИЦА ПРОЕКТОВ.')
    select(p for p in Project).show()
    print('--+------------+----------------')


@db_session
def confirm_contract():
    """
    Подтвердить договор
    """
    try:
        contract = get_contract()
        if contract.contract_status == ContractStatus.draft:
            contract.contract_status = ContractStatus.active
            contract.date_of_signing = datetime.now().date()
            print(f'Статус договора {contract.name_contract} изменен.')
        else:
            print(f'Договор {contract.name_contract} уже подтвержден или завершен.')
    except Exception as e:
        print(e)


@db_session
def complete_contract():
    """
    Завершить договор
    """
    try:
        check_contract_status_for_complete(get_contract())
    except Exception as e:
        print(e)


@db_session
def complete_project_contract():
    """
    Завершить договор выбранного проекта
    """
    try:
        project = get_project()
        if project.contracts:
            for c in project.contracts:
                if c.contract_status == ContractStatus.active:
                    name_contract = input('Введите имя договора: ')
                    if name_contract in select(c.name_contract for c in Contract if c.project == Project[project.id]):
                        check_contract_status_for_complete(Contract.get(name_contract=name_contract))
                    else:
                        print(f'В проекте {project.name_project} нет договора с таким именем.')
                    break
            else:
                print(f'В проекте {project.name_project} нет активного договора.')
        else:
            print(f'В проекте {project.name_project} нет договоров.')
    except Exception as e:
        print(e)
