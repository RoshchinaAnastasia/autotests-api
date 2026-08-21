import httpx
from tools.fakers import fake

user_create_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "Wick",
    "firstName": "John",
    "middleName": "Jr"
}

user_create_response = httpx.post(
    f"http://127.0.0.1:8000/api/v1/users",
    json=user_create_payload
)

print ('User created successfully, status code:', user_create_response.status_code)
print(user_create_response.json())

user_create_response_json = user_create_response.json()
user_id = user_create_response_json["user"]["id"]

user_login_payload = {
    "email": user_create_payload["email"],
    "password": user_create_payload["password"]
}

user_login_response = httpx.post(
    f"http://127.0.0.1:8000/api/v1/authentication/login",
    json=user_login_payload
)

print ('User logged in, status code:', user_login_response.status_code)
print (user_login_response.json())

user_update_payload = {
  "email": fake.email(),
  "lastName": "NewWick",
  "firstName": "NewJohn",
  "middleName": "NewJr"
}

user_token = user_login_response.json()["token"]["accessToken"]

user_update_response = httpx.patch(
    f"http://127.0.0.1:8000/api/v1/users/{user_id}",
    json=user_update_payload,
    headers={"Authorization": f"Bearer {user_token}"}
)

print ("User updated successfully, status code:", user_update_response.status_code)
print(user_update_response.json())
