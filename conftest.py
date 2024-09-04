import pytest
import sys
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base_class import Base
from app.db.models.user import User

from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
load_dotenv(dotenv_path='.env.test')


@pytest.fixture(scope='session')
def test_db():
    engine = create_engine(os.environ['DATABASE_URL'], connect_args={"check_same_thread": False})
    
    Base.metadata.create_all(bind=engine)

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    yield TestingSessionLocal  # Retorna a função que cria sessões

    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope='function')
def db_session(test_db):
    db = test_db()
    db.query(User).delete()
    db.commit()
    yield db
    db.close()