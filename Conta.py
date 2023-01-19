from usuario import *


class Conta(Usuario):
    def __init__(self, id, nome, cpf, telefone, idade, valor=0, emprestimo=0):
        Usuario.__init__(self, id, nome, cpf, telefone, idade, valor, emprestimo)
        self.emprestimo = emprestimo
        self.valor = valor

    def adicionar(self, valor):
        self.valor += valor
        return print(f" O valor: {valor} foi adicionado á sua conta !")

    def retirar(self, valor):
        if self.valor != 0:
            self.valor -= valor
            return print(f' O valor: {valor} foi retirado da conta !')

        else:
            print(f"você não pode retirar nenhum valor, pois tem R${self.valor} na conta")
            opcao = input("deseja fazer um empréstimo do mesmo valor?: ")
            if opcao == "sim":
                self.emprestimo += valor + valor * 0.10
                self.valor += valor
            else:
                print('ok, se precisa conte conosco :)')

    def emprestar(self, valor):
        if self.emprestimo > 0:
            print("primeiro pague o empréstimo anterior !!!!")
        else:
            self.emprestimo += valor + valor * 0.10
            self.valor += valor
            print("valor do empréstimo adicionado a sua conta !")

    def pagar_emprestimo(self, valor):
        if self.emprestimo < 0:
            print("Você não tem emprestimos à pagar !!!!")
        if self.valor < 0:
            print("Você não tem saldo suficiente para pagar o emprestimo !")
        if self.emprestimo == 0:
            print("Você não tem emprestimos à pagar !")
        else:
            self.emprestimo -= valor
            self.valor -= valor
            print("quantia abatida do valor do emprestimo !")





