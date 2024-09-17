import csv

with open('produtos.csv', encoding='utf-8') as file:
  ler_csv = csv.reader(file)
  
  for row in ler_csv:
    print(row)





# produto =  open("09_Manipulando_tipos_de_arquivos/produtos.csv", 'r', encoding='utf-8')
# for linha in produto:
#   item = linha.split(",")
#   print(item[2])