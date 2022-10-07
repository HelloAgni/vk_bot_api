from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# For Docker
conn_url = 'postgresql+psycopg2://postgres:postgres@host.docker.internal:5433/postgres'
# For local
# conn_url = 'postgresql+psycopg2://postgres:postgres@localhost:5433/postgres'

engine = create_engine(conn_url, echo=True)
db_session = scoped_session(sessionmaker(bind=engine))


def bot_commands():
    query_rows = db_session.execute(
        "SELECT title, description FROM baking_bot_simpletext"
    ).fetchall()
    return '\n'.join(
        [' '.join([title, " -> ", desc]) for title, desc in query_rows]
    )


# For Docker
def photo_bot(prod_title):
    query_rows = db_session.execute(
        "SELECT image FROM baking_bot_baking where title=:title",
        {'title': prod_title}).fetchone()
    return '/app/media/' + query_rows.image
# For local test
# def photo_bot()
#     absolute_path = 'E:\\PyCharm_projects\\vk_bot_api\\vk_bot\\media\\'
#     return absolute_path + 'baking_bot\\images\\4.jpg'


def baking_type():
    rows = db_session.execute(
        'SELECT * FROM baking_bot_bakingtype').fetchall()
    return [dict(x) for x in rows]
    # [{'id': 1, 'type': 'a'}, {'id': 2, 'type': 'b'}]


def baking_products_title(text):
    type_id = db_session.execute(
            'SELECT id FROM baking_bot_bakingtype where type=:type_name',
            {'type_name': text}
        ).fetchone()
    products = db_session.execute(
            'SELECT title FROM baking_bot_baking where type_id=:id',
            {'id': type_id[0]}
        ).fetchall()
    return products


def full_info(prod):
    product = db_session.execute(
            'SELECT title, description, image FROM baking_bot_baking where title=:title',
            {'title': prod}).fetchall()
    columns = ['title', 'desc', 'img']
    return dict(zip(columns, product[0]))
    # {'title': 'title4', 'desc': 'aaaa', 'img': 'baking_bot/images/011_zFpA2YT.png'}


# print(baking_products_title(text='b'))
# print(baking_type())
# print(photo_bot())
# print(full_info(prod='title4'))
# print(bot_commands())
