import json

dado = {
  "nome": "Arthur",
  "idade": 22,
  "cidade": "POA"
}

with open ("data.json", "w") as file:
  json.dump(dado, file)

with open("data.json", "r") as file2:
  data = json.load(file2)

print(data)