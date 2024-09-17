import os

with open("07_Leitura e escrita de arquivos/frases.txt", 'r', encoding='utf-8') as arquivo:
  print(arquivo.read())

os.rename("06_Trabalhando com string", "06_Trabalhando_com_string")
