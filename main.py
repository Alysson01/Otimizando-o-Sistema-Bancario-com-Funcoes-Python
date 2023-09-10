
import textwrap


def menu():
    menu = """\n
    —————————————— Opções ——————————————
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    if limite_saques <= numero_saques:
        print(f"Operação falhou!!! A quantidades de saques excedeu o limite de {limite_saques} saques")
    else:
        valor = float(input("Digite o valor do Saque: "))

        if valor > saldo:
            print("Operação falhou!!! Não há saldo o suficiente para saque!")
            
        elif valor > limite:
            print(f"Operação falhou!!! O limite de saque é de {limite} reais") 
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\tR$ {valor:.2f}\n"
            numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        return saldo, extrato, numero_saques
    

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome.title, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def buscar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = buscar_usuario(cpf, usuarios)
    
    while not usuario: 
        print("\n Usuário não encontrado")
        print("\nCriando usuário")
        criar_usuario(usuarios)
        usuario = buscar_usuario(cpf, usuarios)

    print("\n=== Conta criada com sucesso! ===")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}



def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



def main():
    LIMITE_SAQUES = 3
    LIMITE = 500
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    numero_saques = 0
    op = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu().lower

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=LIMITE,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "q":
            break
        else:
            print("Opção invalida!!! Digite um valor dentro dos colchetes")

main()
