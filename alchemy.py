from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from vk_bot.vk_bot import settings
from vk_bot.baking_bot.models import Baking

# conn_url = 'postgresql+psycopg2://yourUserDBName:yourUserDBPassword@yourDBDockerContainerName/yourDBName'
# conn_url = 'postgresql+psycopg2://postgres:docker@localhost:49150/new_base'
conn_url = 'postgresql+psycopg2://postgres:postgres@localhost:5433/postgres'
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
    #     "SELECT * FROM baking_bot_baking where ID = 1").fetchone()
    # # return 'http://localhost/media/' + query_rows.image
    # print(query_rows.image)
    x = Baking.objects.get(id=1)
    print(x)
#
# # photo()
# # print(f'{MEDIA_ROOT}\\baking_bot\\images\\1.jpg')
#
#
# def xxx():
#     query_rows = db.execute(
#         "SELECT * FROM baking_bot_image").fetchall()
#     for register in query_rows:
#         print(register.image_file)
#         print(register.image_b64)
#
#

#
photoz()

