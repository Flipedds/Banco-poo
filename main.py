from Conta import Conta
from random import sample


def numero():
    main_numbers = sample(range(20000), 10)
    return main_numbers[0]


nome, cpf = input("digite o seu nome: "), input("digite o seu cpf: ")
telefone, idade = input("digite o seu telefone: "), int(input("digite a sua idade: "))
id = numero()

cliente = Conta(id, nome, cpf, telefone, idade)

loop = 1
id = numero()


while loop == 1:
    opcao = input("Olá cliente, O que deseja fazer ?: ")
    if opcao == "mostrar":
        cliente.mostrar()
        continue
    elif opcao == "adicionar":
        valor = float(input("Quanto deseja adicionar ?: "))
        cliente.adicionar(valor)
        continue
    elif opcao == "retirar":
        valor = float(input("Quanto deseja retirar ?: "))
        cliente.retirar(valor)
        continue
    elif opcao == "emprestimo":
        valor = float(input("De quanto será o empréstimo ?: "))
        cliente.emprestar(valor)
        continue
    elif opcao == "pagar emprestimo":
        valor = float(input("Quanto deseja pagar do empréstimo ?: "))
        cliente.pagar_emprestimo(valor)
    else:
        continue

# conta.mostrar()
# teste para transformar objets numa lista
# dados = (cliente.__dict__.values())
# dados_lista = (list(dados))
# nome = (dados_lista[0])
# cpf = (dados_lista[1])
# telefone = (dados_lista[2])
# idade = (dados_lista[3])
# conta = Conta(nome, cpf, telefone, idade, 10)
