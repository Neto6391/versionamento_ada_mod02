from sqlalchemy.orm import Session
from app.db.session import SessionLocal

def test_db_connection():
    db: Session = SessionLocal()
    try:
        assert db is not None
    finally:
        db.close()
