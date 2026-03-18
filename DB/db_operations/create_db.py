from sqlalchemy import create_engine, MetaData

engine=create_engine("sqlite:////project/DBchat/DB/db/mydb.db")

metadata = MetaData()
# Define your tables here
metadata.create_all(engine)