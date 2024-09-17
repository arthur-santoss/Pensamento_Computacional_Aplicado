import json

with open('dados.json', encoding='utf-8') as f:
  dados = json.load(f)

for dado in dados:
  print(dado['nome'], dado['idade'])