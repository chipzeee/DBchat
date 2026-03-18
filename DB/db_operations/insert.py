from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine("sqlite:////project/DBchat/DB/db/mydb.db")

insert_students = "INSERT INTO students (id, name) VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie'), (4, 'Diana'), (5, 'Eve');"
insert_courses = "INSERT INTO courses (id, title) VALUES (1, 'Python'), (2, 'SQL'), (3, 'Web Dev'), (4, 'Data Science'), (5, 'DevOps');"
insert_enrollments = "INSERT INTO enrollments (student_id, course_id) VALUES (1, 1), (2, 2), (3, 3), (4, 4), (5, 5);"

with Session(engine) as session:
    session.execute(text(insert_students))
    session.execute(text(insert_courses))
    session.execute(text(insert_enrollments))
    session.commit()