from task_manager.models import create_engine, Column, Integer, String, ForeignKey
from task_manager.models import declarative_base, relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    tasks = relationship('Task', back_populates='user')

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='tasks')

engine = create_engine('sqlite:///tasks.db')
Base.metadata.create_all(engine)
