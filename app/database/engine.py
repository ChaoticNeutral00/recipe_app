from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.database import DEV_DB_URL, TEST_DB_URL

# Return the database URL for the selected environment.
#
# Args:
#     testing: If True, return the test database URL.
#
# Returns:
#     Database connection URL string.
def get_database_url(testing: bool = False) -> str:
    if testing:
        return TEST_DB_URL
    return DEV_DB_URL

# Create and return a SQLAlchemy engine instance.
#
# Args:
#     testing: If True, connect to the test database.
#
# Returns:
#     SQLAlchemy Engine object
def get_engine(testing: bool = False):
    db_url = get_database_url(testing=testing)
    engine = create_engine(db_url, echo=True)
    return engine

# Create and return a SQLAlchemy session instance
#
# Args:
#     testing: If True, connect to the test database.
#
# Returns:
#     SQLAlchemy Session factory
def get_session_factory(testing: bool = False):
    engine = get_engine(testing=testing)
    Session = sessionmaker(engine)
    return Session