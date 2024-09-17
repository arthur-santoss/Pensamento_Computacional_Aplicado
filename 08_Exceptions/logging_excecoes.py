import logging

logging.basicConfig(filename='logA.log', level=logging.DEBUG)

def calculoValores(num1, num2):
  try:
    resultado = num1/num2
  except ZeroDivisionError:
    logging.exception("Problema de divisão dos números por zero")
  else:
    return resultado
  
print(calculoValores(2,4))