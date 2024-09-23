from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
#DATABASE_URL = "sqlite:///dreams.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'dreams.db')}"
#create engine
engine = create_engine(DATABASE_URL)

#session for a class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()