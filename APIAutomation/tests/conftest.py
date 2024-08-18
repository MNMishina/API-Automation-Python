import pytest


@pytest.fixture()
def set_up():
    print("Authorized in system")
    yield
    print("Log out")


@pytest.fixture(scope="module")
def some():
    print("Start")
    yield
    print("End")
