from app.database.engine import get_engine
from app.database.tables import Base
import app.database.tables

engine = get_engine(testing=True)
Base.metadata.create_all(engine)