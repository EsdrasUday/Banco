class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.limite_saque = 500.0
        self.saques_diarios = 0
        self.limite_saques_diarios = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("❌ Valor inválido. O depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saques_diarios:
            print("❌ Limite diário de saques atingido (3 saques por dia).")
        elif valor <= 0:
            print("❌ Valor inválido. O saque deve ser positivo.")
        elif valor > self.limite_saque:
            print(f"❌ Saque não permitido. O valor máximo por saque é R$ {self.limite_saque:.2f}.")
        elif valor > self.saldo:
            print("❌ Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_diarios += 1
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso.")

    def mostrar_extrato(self):
        print("\n====== EXTRATO ======")
        
        if self.depositos:
            print("Depósitos:")
            for i, valor in enumerate(self.depositos, start=1):
                print(f"{i}. + R${valor:.2f}")
        else:
            print("Nenhum depósito registrado.")

        if self.saques:
            print("\nSaques:")
            for i, valor in enumerate(self.saques, start=1):
                print(f"{i}. - R${valor:.2f}")
        else:
            print("\nNenhum saque registrado.")

        print(f"\nSaldo atual: R${self.saldo:.2f}")
        print("=======================")


def menu():
    banco = Banco()
    while True:
        print("\n[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                valor = float(input("Informe o valor do depósito: R$ "))
                banco.depositar(valor)
            except ValueError:
                print("❌ Entrada inválida. Digite um número válido.")
        elif opcao == '2':
            try:
                valor = float(input("Informe o valor do saque: R$ "))
                banco.sacar(valor)
            except ValueError:
                print("❌ Entrada inválida. Digite um número válido.")
        elif opcao == '3':
            banco.mostrar_extrato()
        elif opcao == '4':
            print("✅ Sistema encerrado. Obrigado por utilizar nossos serviços.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
