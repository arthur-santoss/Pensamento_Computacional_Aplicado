from dominio.aluno import Aluno
from dominio.biblioteca import Biblioteca

def registros(cliente, livro):
  print()
  print(f'Cliente: {cliente.mostrar_dados_cadastrais()}')
  print(f'Livros Alugados: {livro.mostrar_alugados()}')

aluno1 = Aluno("Arthur", '51 9 954545-5212')
aluno2 = Aluno("Fernanda", '51 9 95111-5313')

aluguel1 = Biblioteca(aluno1)
aluguel2 = Biblioteca(aluno2)

aluguel1.alugar_livro('O hobbit')
aluguel1.alugar_livro('Relampago Maquin')
aluguel1.alugar_livro('Churrasquinho de esqueiro')

aluguel2.alugar_livro('O Pequeno Príncipe')
aluguel2.alugar_livro('Romeu E Julieta')
aluguel2.alugar_livro('1984 George Orwell')

registros(aluno1, aluguel1)
registros(aluno2, aluguel2)