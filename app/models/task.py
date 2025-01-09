from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

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


"""
1. Класс Base – это ваш базовый класс, который вы создали при настройке SQLAlchemy. Он обычно создается так:

   from sqlalchemy.ext.declarative import declarative_base

   Base = declarative_base()

2. Атрибуты классов:
   - Column: Это столбцы вашей базы данных. Например, Integer означает целочисленный тип данных, а String – строку.
   - ForeignKey: Внешний ключ, связывающий модели друг с другом. В данном случае user_id ссылается на id в таблице users.
   - relationship: Устанавливает связь между моделями. Параметр back_populates указывает, какой атрибут другой модели будет использоваться для обратной ссылки.

3. Индексы: Индексы (index=True) ускоряют поиск записей по этим полям.

4. Уникальные поля: Уникальность полей задается через параметр unique=True. Например, slug должно быть уникальным для каждой записи.
"""

