class Calculadora:
  def __init__(self, val1, val2):
    self.a = val1
    self.b = val2
  
  def soma(self):
    return self.a + self.b
  
  def subtrai(self):
    return self.a - self.b
  
  def multi(self):
    return self.a * self.b
  
  def divi(self):
    return self.a / self.b
    


calc = Calculadora(2,4)    
print(calc.soma())
