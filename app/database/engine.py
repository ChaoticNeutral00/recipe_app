from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.database import DEV_DB_URL, TEST_DB_URL


def get_database_url(testing: bool = False) -> str:
    if testing:
        return TEST_DB_URL
    return DEV_DB_URL

def get_engine(testing: bool = False):
    db_url = get_database_url(testing=testing)
    return create_engine(db_url, echo=True)