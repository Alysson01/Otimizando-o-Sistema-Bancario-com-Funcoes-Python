saldo = 0
depositos = []
saques = []

def realizar_deposito():
    global saldo
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        saldo += valor
        depositos.append(valor)
    else:
        print("Valor inválido.")

def realizar_saque():
    global saldo
    valor = float(input("Digite o valor do saque: "))
    if valor > 0 and valor <= 500 and valor <= saldo:
        saldo -= valor
        saques.append(valor)
    else:
        print("Não foi possível realizar o saque. Verifique o valor ou saldo disponível.")

def exibir_extrato():
    if not depositos and not saques:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato:")
        for deposito in depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in saques:
            print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")

while True:
    print("Escolha uma operação:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")
    
    escolha = input("Digite o número da operação: ")
    
    if escolha == "1":
        realizar_deposito()
    
    elif escolha == "2":
        realizar_saque()
    
    elif escolha == "3":
        exibir_extrato()
    
    elif escolha == "4":
        break
    
    else:
        print("Opção inválida. Digite 1, 2, 3 ou 4 para escolher uma operação.")
