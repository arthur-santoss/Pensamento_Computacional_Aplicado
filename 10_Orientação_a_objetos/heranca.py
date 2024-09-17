class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def setNome(self, nome):
    self.nome = nome

  def getNome(self):
    return self.nome
  
  def setIdade(self, idade):
    self.idade = idade

  def getIdade(self):
    return self.idade
  
# pessoaArthur = Pessoa("Arthur", 22)
# print(pessoaArthur.getNome())
# print(pessoaArthur.getIdade())

# print(pessoaArthur.setNome("Fulano"))
# print(pessoaArthur.setIdade(25))

# print(pessoaArthur.getNome())
# print(pessoaArthur.getIdade())