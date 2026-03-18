from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# query="select name from sqlite_master where type='table';"
query="select * from students;"
engine = create_engine("sqlite:////project/DBchat/DB/db/mydb.db")

with Session(engine) as session:
    result = session.execute(text(query))
    for row in result:
        print(row)
    