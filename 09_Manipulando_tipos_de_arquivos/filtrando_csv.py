import csv

def read_csv_file(file_path):
  data = []
  with open(file_path, encoding='utf-8') as file:
    ler_csv = csv.reader(file)

    for row in ler_csv:
      data.append(row)
  return data


csv_file_path = r'produtos.csv'
data_list = read_csv_file(csv_file_path)

  
filtered_data = list(filter( lambda x: x[2].strip() == 'eletrodoméstico' , data_list))

print(filtered_data)





# produto =  open("09_Manipulando_tipos_de_arquivos/produtos.csv", 'r', encoding='utf-8')
# for linha in produto:
#   item = linha.split(",")
#   print(item[2])