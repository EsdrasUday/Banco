# 💰 Sistema Bancário em Python - Versão 1

Este é um projeto simples de um sistema bancário em Python desenvolvido para um grande banco. A versão 1 do sistema implementa funcionalidades básicas para um único usuário.

## ✅ Funcionalidades

- **Depósito**
  - Permite depósitos de valores positivos.
  - Todos os depósitos são registrados e exibidos no extrato.

- **Saque**
  - Permite até **3 saques por dia**.
  - Cada saque pode ter o valor máximo de **R$500.00**.
  - Não permite saques com saldo insuficiente.
  - Todos os saques são registrados e exibidos no extrato.

- **Extrato**
  - Lista todos os depósitos e saques.
  - Exibe o saldo atual no formato `R$xxx.xx`.

## ▶️ Como usar

1. Execute o script `sistema_bancario.py` com Python 3:
   ```bash
   python sistema_bancario.py
   ```

2. No menu, escolha uma das opções:
   ```
   [1] Depositar
   [2] Sacar
   [3] Extrato
   [4] Sair
   ```

3. Siga as instruções no terminal para realizar as operações desejadas.

## 🛠 Requisitos

- Python 3.6 ou superior

## 📌 Observações

- O sistema trabalha com **apenas um usuário**.
- Os dados são armazenados **temporariamente em memória** (não persistem após encerrar o programa).

## 📝 Licença

Este projeto está licenciado sob os termos da [Licença GNU](LICENSE).

