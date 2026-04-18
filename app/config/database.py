from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"

DB_PATH = DATA_DIR / "recipes.db"
TEST_DB_PATH = DATA_DIR / "test.db"

DEV_DB_URL = f"sqlite:///{DB_PATH.as_posix()}"
TEST_DB_URL = f"sqlite:///{TEST_DB_PATH.as_posix()}"