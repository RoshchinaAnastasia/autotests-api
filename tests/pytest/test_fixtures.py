import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
   print("[AUTOUSE] Send data to analytics service")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Set up settings for session")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Create users data once per class")

@pytest.fixture(scope="function")
def users_client(settings):
    print("[FUNCTION] New API client for every test")

class TestUserFlow():
    def test_user_can_login(self, settings, user, users_client):
        ...

    def test_user_can_create_course(self,settings, user, users_client):
        ...

class TestAccountFlow():
    def test_user_account(self, settings, user, users_client):
        ...

@pytest.fixture
def user_data()-> dict:
    print("Create user before test(setup)")
    yield {"username": "test_user", "email": "test@example.com"}
    print("Delete user after tes (teardown)")

def test_user_email(user_data:dict):
    print(user_data)
    assert user_data['email'] == 'test@example.com'

def test_username(user_data:dict):
    print(user_data)
    assert user_data['username'] == 'test_user'