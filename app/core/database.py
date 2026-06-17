from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings



#create engine
engine = create_engine(
    settings.DATABASE_URL, connect_args = {"check_same_thread": False}
    if settings.DATABASE_URL.startswith("sqlite") else {}
)

#create Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#create base class
Base = declarative_base()

#dependency injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()