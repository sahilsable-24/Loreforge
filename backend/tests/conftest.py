import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.core.config import settings
from app.db.base import Base
from app.db.session import get_db
import app.models as _models  # noqa: F401  (imports every model so Base knows all tables)

# Same server and password as dev, but the database name is swapped.
TEST_URL = "postgresql+psycopg://loreforge:loreforge_dev@localhost:5432/loreforge_test"
engine = create_engine(TEST_URL)
TestSession = sessionmaker(bind=engine)


@pytest.fixture(scope="session", autouse=True)
def create_tables():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture()
def client():
    def override_get_db():
        with TestSession() as db:
            yield db

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

    with engine.begin() as conn:
        for table in reversed(Base.metadata.sorted_tables):
            conn.execute(text(f'TRUNCATE "{table.name}" CASCADE'))