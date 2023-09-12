from datetime import date

from pony.orm import *

db = Database()
db.bind(provider='sqlite', filename='db.sqlite3', create_db=True)


class Contract(db.Entity):
    id = PrimaryKey(int, auto=True)
    name_contract = Required(str)
    date_of_creation = Required(date)
    date_of_signing = Optional(date)
    contract_status = Required(str)
    project = Optional('Project')


class Project(db.Entity):
    id = PrimaryKey(int, auto=True)
    name_project = Required(str)
    date_of_creation = Required(date)
    contracts = Set(Contract)


db.generate_mapping(create_tables=True)
