
class Usuario:
    def __init__(self, id, nome, cpf, telefone, idade, valor, emprestimo):
        self.id = id
        self.emprestimo = emprestimo
        self.valor = valor
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.idade = idade

    def mostrar(self):
        print('''
        Dados do usuário:
        Id: {}
        Cliente: {}
        Cpf: {}
        Telefone {}
        Idade: {}
        saldo atual : R${}
        Empréstimo: R${}
            '''.format(self.id, self.nome, self.cpf, self.telefone, self.idade, self.valor, self.emprestimo))
