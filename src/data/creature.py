import sqlite3
from src.model.creature import Creature

DB_NAME = 'cryptid.db'
conn = sqlite3.connect(DB_NAME)
curs = conn.cursor()

def init():
    curs.execute("CREATE TABLE creature(name, description, country, area, aka)")

def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(name=name,
                    description=description,
                    country=country, area=area,
                    aka=aka)

def model_to_dict(creature: Creature) -> dict:
    return creature.dict()

def get_one(name: str) -> Creature:
    query = "SELECT * FROM creature WHERE name=:name"
    params = {"name": name}
    curs.execute(query, params)
    row = curs.fetchone()
    return row_to_model(row)

def get_all() -> list[Creature]:
    query = "SELECT * FROM creature"
    curs.execute(query)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(creature: Creature):
    query = 'INSERT INTO creature VALUES (:name, :description, :country, :area, :aka)'
    params = model_to_dict(creature)

    curs.execute(query, params)

def modify(creature: Creature):
    return creature

def replace(creature: Creature):
    return creature

def delete(creature: Creature):
    query = "DELETE FROM creature WHERE name=:name"
    params = {"name": creature.name}
    curs.execute(query, params)
