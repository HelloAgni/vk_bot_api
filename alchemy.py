# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
#
#
# # conn_url = 'postgresql+psycopg2://yourUserDBName:yourUserDBPassword@yourDBDockerContainerName/yourDBName'
# conn_url = 'postgresql+psycopg2://postgres:postgrespw@localhost:49153/new_base'
#
# engine = create_engine(conn_url)
#
# db = scoped_session(sessionmaker(bind=engine))
#
#
# query_rows = db.execute("SELECT * FROM baking_bot_simpletext").fetchall()
# for register in query_rows:
#     if register.title == 'Бот привет':
#         print(f"{register.title.replace('Бот', 'Босс')}")
#         print(f"{register.text}")
# # Note that this Python way of printing is available in Python3 or more!!
