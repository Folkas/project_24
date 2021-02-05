import psycopg2
import os
from dotenv import load_dotenv

    
def create_table() -> str:
    load_dotenv(override=True)
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = connection.cursor()
    cur.execute("\
    CREATE TABLE IF NOT EXISTS autoplius (\
        id serial PRIMARY KEY,\
        manufacturingDate int,\
        engine_l float8,\
        power_kw float8,\
        mileage_km float8,\
        gearbox_auto int,\
        gearbox_manual int,\
        price_euro int\
    );\
    ")
    connection.commit()
    return "Table successfully created"

def drop_table() -> str:

    load_dotenv(override=True)
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = connection.cursor()
    cur.execute("\
        DROP TABLE IF EXISTS autoplius;\
            ")
    connection.commit()
    return "Table autoplius was successfully dropped"

def show_table() -> str:
    load_dotenv(override=True)
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = connection.cursor()
    cur.execute("\
        SELECT * from autoplius;\
            ")
    return cur.fetchall()

def insert_example() -> str:
    load_dotenv(override=True)
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = connection.cursor()
    cur.execute("insert into autoplius(\
    manufacturingDate,\
    engine_l,\
    power_kw, \
    mileage_km, \
    gearbox_auto, \
    gearbox_manual, \
    price_euro) \
    VALUES (2016, 1.5, 70.0, 188928.0, 0, 1, 7550 ) \
    ")

show_table()