import httpx

response = httpx.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2")

print(response.status_code)
print(response.json())

data = {
    "foo1": "bar1",
    "foo2": "bar2"
  }

response = httpx.post("https://postman-echo.com/post", json=data)

print(response.status_code)
print(response.json())

headers = {"Authorization": f"Bearer my_token"}
response = httpx.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2", headers=headers)

print(response.request.headers)
print(response.json())


params = {"foo1": "bar1"}
response = httpx.get("https://postman-echo.com/get", params=params)

print(response.url)
print(response.json())

with httpx.Client() as client:
    response1  = client.get("https://postman-echo.com/get?foo1=bar1")
    response2 = client.get("https://postman-echo.com/get?foo2=bar2")

print("Client", response1.json())
print("Client", response2.json())

try:
    response = httpx.get("https://postman-echo.com/get/invalid_url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"HTTPError: {e}")