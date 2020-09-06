import pytest



@pytest.fixture(scope="module")
def app():
    return create_app()