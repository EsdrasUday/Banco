class SistemaBancario:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.AGENCIA = "0001"

    def criar_usuario(self):
        cpf = input("Informe o CPF (apenas números): ").strip()
        if any(usuario["cpf"] == cpf for usuario in self.usuarios):
            print("❌ Já existe um usuário com esse CPF.")
            return

        nome = input("Informe o nome completo: ").strip()
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
        endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/UF): ").strip()

        self.usuarios.append({
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        })
        print("✅ Usuário criado com sucesso.")

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ").strip()
        usuario = next((u for u in self.usuarios if u["cpf"] == cpf), None)

        if usuario:
            numero_conta = len(self.contas) + 1
            self.contas.append({
                "agencia": self.AGENCIA,
                "numero_conta": numero_conta,
                "usuario": usuario,
                "saldo": 0.0,
                "saques": [],
                "depositos": [],
                "saques_diarios": 0
            })
            print(f"✅ Conta criada com sucesso. Número: {numero_conta}")
        else:
            print("❌ Usuário não encontrado. Cadastre o usuário antes.")

    def depositar(self, conta, valor):
        if valor > 0:
            conta["saldo"] += valor
            conta["depositos"].append(valor)
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("❌ Valor inválido. O depósito deve ser positivo.")

    def sacar(self, *, conta, valor, limite=500.0, limite_saques=3):
        if conta["saques_diarios"] >= limite_saques:
            print("❌ Limite diário de saques atingido.")
        elif valor <= 0:
            print("❌ Valor inválido. O saque deve ser positivo.")
        elif valor > limite:
            print(f"❌ Saque não permitido. Máximo por saque: R$ {limite:.2f}.")
        elif valor > conta["saldo"]:
            print("❌ Saldo insuficiente.")
        else:
            conta["saldo"] -= valor
            conta["saques"].append(valor)
            conta["saques_diarios"] += 1
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso.")

    def exibir_extrato(self, conta):
        print("\n====== EXTRATO ======")
        if conta["depositos"]:
            print("Depósitos:")
            for i, v in enumerate(conta["depositos"], 1):
                print(f"{i}. + R${v:.2f}")
        else:
            print("Nenhum depósito registrado.")

        if conta["saques"]:
            print("\nSaques:")
            for i, v in enumerate(conta["saques"], 1):
                print(f"{i}. - R${v:.2f}")
        else:
            print("\nNenhum saque registrado.")

        print(f"\nSaldo atual: R${conta['saldo']:.2f}")
        print("=======================")

    def selecionar_conta(self):
        if not self.contas:
            print("❌ Nenhuma conta cadastrada.")
            return None
        print("\nContas disponíveis:")
        for i, conta in enumerate(self.contas):
            print(f"[{i}] Conta {conta['numero_conta']} - Titular: {conta['usuario']['nome']}")
        try:
            indice = int(input("Escolha o número da conta: "))
            return self.contas[indice] if 0 <= indice < len(self.contas) else None
        except (ValueError, IndexError):
            print("❌ Seleção inválida.")
            return None

    def menu(self):
        while True:
            print("\n[1] Criar usuário\n[2] Criar conta\n[3] Depositar\n[4] Sacar\n[5] Extrato\n[6] Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.criar_usuario()
            elif opcao == '2':
                self.criar_conta()
            elif opcao == '3':
                conta = self.selecionar_conta()
                if conta:
                    try:
                        valor = float(input("Valor do depósito: R$ "))
                        self.depositar(conta, valor)
                    except ValueError:
                        print("❌ Entrada inválida.")
            elif opcao == '4':
                conta = self.selecionar_conta()
                if conta:
                    try:
                        valor = float(input("Valor do saque: R$ "))
                        self.sacar(conta=conta, valor=valor)
                    except ValueError:
                        print("❌ Entrada inválida.")
            elif opcao == '5':
                conta = self.selecionar_conta()
                if conta:
                    self.exibir_extrato(conta)
            elif opcao == '6':
                print("✅ Sistema encerrado. Obrigado por utilizar nossos serviços.")
                break
            else:
                print("❌ Opção inválida.")


if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.menu()
