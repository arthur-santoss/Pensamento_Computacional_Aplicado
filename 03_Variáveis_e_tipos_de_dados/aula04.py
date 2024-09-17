salario = int(input('Qual o seu salário? '))
reajuste = int(input('Reajuste de quanto por ano? '))

reajuste = reajuste /100

aumento = salario + (salario*reajuste)

print(f'Salário com reajuste de {reajuste*100}%: R$ {aumento}')