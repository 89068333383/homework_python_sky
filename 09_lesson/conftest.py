import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DB_URL = "postgresql://postgres:Qwert123@localhost:5432/postgres"
engine = create_engine(DB_URL, echo=False)

@pytest.fixture(scope="function")
def session() -> Session:
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    sess = SessionLocal()
    transaction = sess.begin()
    yield sess
    transaction.rollback()
    sess.close()