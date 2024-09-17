from heranca import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, CPF, nome, idade):
        super().__init__(nome, idade)
        self.cpf = CPF

    def getCPF(self):
        return self.cpf

    def setCPF(self, CPF):
        self.cpf = CPF

# Criar uma instância de PessoaFisica
pessoa_fisica = PessoaFisica("654645415416", "Arthur", 22)

# Agora você chama o método getNome a partir da instância
print(pessoa_fisica.getNome())
print(pessoa_fisica.getIdade())
print(pessoa_fisica.getCPF())
