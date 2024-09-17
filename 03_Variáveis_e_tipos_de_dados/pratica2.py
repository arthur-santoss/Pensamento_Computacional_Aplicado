custoFabrica = float(input('Informe o Custo de Fábrica: '))

custoDistribuidor = custoFabrica * 0.28 
custoImposto = custoFabrica * 0.45
custoFinal = custoFabrica + custoImposto + custoDistribuidor

print(f'Custo do Distribuidor: R$ {custoDistribuidor:.2f}\nCusto do Imposto: R$ {custoImposto:.2f}\nCusto do Final: R$ {custoFinal:.2f}')

