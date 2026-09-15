import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_number(number: int):
    assert number>0


@pytest.mark.parametrize("number, expected", [(1,1), (2,4), (3,9), ])
def test_several_numbers(number: int, expected: int):
    assert number **2 == expected

@pytest.mark.parametrize("OS", ["MacOs", "Windows", "Linux", "Unix"])
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stage.company.com",
    "https://prod.company.com"
])
def test_multiplication_of_numbers(OS: str, host: str):
    assert len(OS + host) > 0

@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stage.company.com",
    "https://prod.company.com"
])
def host(request: SubRequest) -> str:
    return request.param

def test_host(host: str):
    print(f"Running test on host: {host}")

@pytest.mark.parametrize("user", ["Alise", "Zara"])
class TestOperations:
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")

users = {
    "+700000011": "User with money on bank account",
    "+700000022": "User with money on bank account",
    "+700000023": "User with operations on bank account",
}

@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
    )
def test_identifiers(phone_number: str):
    pass