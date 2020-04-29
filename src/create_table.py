from models import *
import db
import os

if __name__ == "__main__":
    path = SQLITE3_NAME
    if not os.path.isfile(path):

        # create new table
        Base.metadata.create_all(db.engine)

    admin = User(username='admin', password='fastapi', mail='hoge@example.com')
    db.session.add(admin)
    db.session.commit()

    task = Task(
        user_id=admin.id,
        content='締め切り',
        deadline=datetime(2020, 5, 1, 12, 00, 00),
    )
    print(task)
    db.session.add(task)
    db.session.commit()

