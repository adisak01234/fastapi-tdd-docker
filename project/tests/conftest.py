import os

import pytest
from starlette.testclient import TestClient

from app import main
from app.config import get_setting, Settings


def get_setting_override():
    return Settings(testing=1, database_url=os.environ.get('DATABASE_TEST_URL'))


@pytest.fixture(scope='module')
def test_app():
    main.app.dependency_overrides[get_setting] = get_setting_override
    with TestClient(main.app) as test_client:
        yield test_client

