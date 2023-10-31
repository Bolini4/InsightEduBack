from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, scoped_session, sessionmaker, Query


engine = create_engine('mysql://root:root@localhost:3306/projetisfec', echo=False)
Base = declarative_base()
Base.metadata.reflect(engine)

class User(Base):
    __table__ = Base.metadata.tables['utilisateurs']


if __name__ == '__main__':
    print("coucou")
    print(Base.metadata.tables)
    print(engine)
    db_session = scoped_session(sessionmaker(bind=engine))
    for item in db_session.query(User.id, User.nom):
        print (item)