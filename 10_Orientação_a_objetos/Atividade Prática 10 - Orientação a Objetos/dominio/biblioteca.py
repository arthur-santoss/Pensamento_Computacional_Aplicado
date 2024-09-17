class Biblioteca:
  def __init__(self, aluno):
    self.aluno = aluno
    self.reservas = []

  def alugar_livro(self, nome_livro):
    self.reservas.append(nome_livro) 

  def mostrar_alugados(self):
    return self.reservas