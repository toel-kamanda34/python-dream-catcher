from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base

item_category = Table('item_categories', Base.metadata,
    Column('item_id', Integer, ForeignKey('quests.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True)
)

class Quest(Base):
    __tablename__ = 'quests'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime)
    deadline = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    categories = relationship("Category", secondary=item_category, back_populates="quests")
    user = relationship('User', back_populates='quests')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    quests = relationship('Quest', back_populates='user')

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    
    quests = relationship("Quest", secondary=item_category, back_populates="categories")