from sqlalchemy import create_engine, select
from sqlalchemy.sql import text
from sqlalchemy.orm import scoped_session, sessionmaker

# For Docker
# conn_url = 'postgresql+psycopg2://postgres:postgres@host.docker.internal:5433/postgres'
conn_url = 'postgresql+psycopg2://postgres:postgres@localhost:5433/postgres'
engine = create_engine(conn_url, echo=True)
db_session = scoped_session(sessionmaker(bind=engine))


def bot_commands():
    query_rows = db_session.execute(
        "SELECT * FROM baking_bot_simpletext").fetchall()
    # for register in query_rows:
        # if register.title == '/Бот привет':
            # print(f"{register.title.replace('Бот', 'Босс')}")
            # print(f"{register.text}")
    return ', '.join([_.title for _ in query_rows])


def photo_bot():
    query_rows = db_session.execute(
        "SELECT * FROM baking_bot_baking where ID = 1").fetchone()
    # For Docker
    # return '/app/media' + query_rows.image
    return query_rows.image


def baking_type():
    rows = db_session.execute(
        'SELECT * FROM baking_bot_bakingtype').fetchall()
    # return [''.join(x) for x in rows]
    return [dict(x) for x in rows]
    # return [x.get('type') for x in [dict(x) for x in rows]]


def baking_products_title(text):
    type_id = db_session.execute(
            'SELECT id FROM baking_bot_bakingtype where type=:type_name', {'type_name': text}
        ).fetchone()
    products = db_session.execute(
            'SELECT title FROM baking_bot_baking where type_id=:id', {'id': type_id[0]}
        ).fetchall()
    return products


# print(baking_products_title(text='b'))
# print(baking_type())
# print(photo_bot())
