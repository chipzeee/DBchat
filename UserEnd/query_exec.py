from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

 
engine = create_engine("sqlite:////project/DBchat/DB/db/mydb.db")

 
def execute(query):
    try:
        with Session(engine) as session:
            result = session.execute(text(query))
            session.commit()
            
            # For SELECT queries
            if query.strip().upper().startswith("SELECT"):
                rows = result.fetchall()
                buffer=f"Retrieved {len(rows)} rows:"+"\n"
                for row in rows:
                    buffer+=f"  {row}"+"\n"
                return buffer
            # For INSERT/UPDATE/DELETE
            else:
                return(f"Operation successful! Rows affected: {result.rowcount}")
    except Exception as e:
        return(f"Error: {str(e)}")



if __name__=='__main__':
    result=execute("Select * from student;")
    print(result)