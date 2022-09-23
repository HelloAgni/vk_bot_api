from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from vk_bot.vk_bot.settings import MEDIA_ROOT

# conn_url = 'postgresql+psycopg2://yourUserDBName:yourUserDBPassword@yourDBDockerContainerName/yourDBName'
conn_url = 'postgresql+psycopg2://postgres:docker@localhost:49150/new_base'
engine = create_engine(conn_url)
db = scoped_session(sessionmaker(bind=engine))


def bot_commands():
    query_rows = db.execute(
        "SELECT * FROM baking_bot_simpletext").fetchall()
    # for register in query_rows:
        # if register.title == '/Бот привет':
            # print(f"{register.title.replace('Бот', 'Босс')}")
            # print(f"{register.text}")
    return ', '.join([_.title for _ in query_rows])


def photoz():
    # query_rows = db.execute(
    #     "SELECT * FROM baking_bot_baking").fetchall()
    # img = requests.get()query_rows[0].image
    return f'{MEDIA_ROOT}\\baking_bot\\images\\1.jpg'

# photo()
# print(f'{MEDIA_ROOT}\\baking_bot\\images\\1.jpg')


def xxx():
    query_rows = db.execute(
        "SELECT * FROM baking_bot_image").fetchall()
    for register in query_rows:
        print(register.image_file)
        print(register.image_b64)


xxx()