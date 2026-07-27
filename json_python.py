import json

json_data = """{
  "name": "Ivan",
  "age": 30,
  "is_student": true,
  "courses": [
    "Python",
    "QA Automation",
    "API Testing"
  ],
  "address": {
    "city": "Moscow",
    "ZIP": "12345"
  }
}"""
parsed_data = json.loads(json_data)

print(parsed_data['name'], type(parsed_data))

#Это словарь в Питоне
data = {
    "name": "Maria",
    "age": 25,
    "is_student": True}

json_str = json.dumps(data, indent=4)
print(json_str, type(json_str))

with open("json_example.json", "r") as file:
    read_data = json.load(file)
    print(read_data, type(data))

with open("json_user.json", "w") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)