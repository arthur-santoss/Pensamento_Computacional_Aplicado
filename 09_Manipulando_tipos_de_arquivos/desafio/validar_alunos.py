import json

with open("estudantes.json", encoding='utf-8') as file_alunos:
  dados = json.load(file_alunos)

for dado in dados['estudantes']:
  notas = dado['notas']

  avg_notas = sum(notas) / len(notas)

  dado["avg_notas"] = avg_notas

  if avg_notas > 6:
    with open("estudantes_aprovados.json", 'a', encoding='utf-8') as file_alunos_aprovados:
      json.dump(dado,file_alunos_aprovados, ensure_ascii=False,indent=4)

  if avg_notas < 6:
    with open("estudantes_reprovados.json", 'a', encoding='utf-8') as file_alunos_reprovados:
      json.dump(dado,file_alunos_reprovados, ensure_ascii=False,indent=4)

  # print(calcular_media(notas))