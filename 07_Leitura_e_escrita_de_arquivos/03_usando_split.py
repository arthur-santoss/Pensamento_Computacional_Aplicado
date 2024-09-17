arquivo = open("07_Leitura_e_escrita_de_arquivos/alunos.txt", 'r', encoding='utf-8')

for linha in arquivo:
  aluno = linha.strip().split(",")
  
  if float(aluno[2]) >= 7:
    print(f'+ APROVADO: {aluno[0]} com nota {aluno[2]}')
  else:
    print(f'REPROVADO: {aluno[0]} com nota {aluno[2]}')