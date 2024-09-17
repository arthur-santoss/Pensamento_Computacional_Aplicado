class Aluno:
  def __init__(self, nome, telefone):
    self.nome = nome
    self.telefone = telefone

  def mostrar_dados_cadastrais(self):
    return f'{self.nome} - {self.telefone}  '