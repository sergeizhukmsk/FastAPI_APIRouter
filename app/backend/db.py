from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Создаем движок SQLite
engine = create_engine('sqlite:///taskmanager.db', echo=True)

# Создаем фабрику сессий
SessionLocal = sessionmaker(bind=engine)

# Базовая модель для всех таблиц
Base = declarative_base()


class Task(Base):
	__tablename__ = 'tasks'

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String)
	content = Column(String)
	priority = Column(Integer, default=0)
	completed = Column(Boolean, default=False)
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)

	slug = Column(String, unique=True, index=True)

	# Связь с моделью User
	user = relationship("User", back_populates="tasks")


class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, index=True)
	username = Column(String)
	firstname = Column(String)
	lastname = Column(String)
	age = Column(Integer)

	slug = Column(String, unique=True, index=True)

	# Связь с моделью Task
	tasks = relationship("Task", back_populates="user")


if __name__ == "__main__":
	# Создаем все таблицы
	Base.metadata.create_all(engine)
