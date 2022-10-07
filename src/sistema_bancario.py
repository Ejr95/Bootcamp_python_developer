menu = """
        *Menu*
        [d]Depositar
        [s]Sacar
        [e]Extrato
        [q]Sair
        
Informe a opção desejada : 
"""
numero_saques_diario = 0
LIMITE_SAQUE_DIARIO = 3
deposito = 0
saldo = 0
limite_saque = 500
extrato = ''
valor_saque = 0

while True:

    opcao = input(menu)

    if opcao == 'd':
        print("Depósito")
        print("Informe Valor do Depósito : ")
        deposito = int(input())
        if deposito > 0:
            saldo += deposito
            print("Depósito realizado com sucesso!")
            extrato += f"Depósito realizado de : R$ {deposito:.2f}\n"
        else:
            print("Valor precisa ser maior que 0!")
    elif opcao == 's':
        print("Informe Valor do Saque : ")
        valor_saque = int(input())
        if numero_saques_diario <= 3:
            if saldo > 0:
                if valor_saque <= 500:
                    saldo -= valor_saque
                    numero_saques_diario += 1
                    if numero_saques_diario > LIMITE_SAQUE_DIARIO:
                        print("Número de Saques Diário atingido!")
                        break
                    extrato += f"Saque efetuado : R$ {valor_saque:.2f}"
                    print("Retire as notas na boca do caixa\nObrigado!!")
                    print(f"Saques Diários Restantes : {LIMITE_SAQUE_DIARIO - numero_saques_diario}")
                else:
                    print("Não foi possível realizar saque,saldo abaixo do valor de saque desejado")
            else:
                print("Saldo insuficiente")
        else:
            print("Limite diário de 3 Saques atingido")
    elif opcao == 'e':
        print("========Extrato=========")
        print("Não foram Realizadas Movimentações" if not extrato else extrato)
        print(extrato)
        print(f"Saldo Atual : {saldo:.2f}")
        print("=========================")
    elif opcao == 'q':
        break
    else:
        print("Opção inválida")
