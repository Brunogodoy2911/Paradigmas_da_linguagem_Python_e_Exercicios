class Conta:
  def __init__(self, numero, cpf, nomeTitular, saldo):
    self.numero = numero
    self.cpf = cpf
    self.nomeTitular = nomeTitular
    self.saldo = saldo

  def depositar(self, valor):
    self.saldo += valor

  def sacar(self, valor):
    if self.saldo < valor:
      return False
    else:
      self.saldo -= valor
      return True

  def gerar_extrato(self):
    print(f"Número: {self.numero} \ncpf: {self.cpf} \nsaldo: {self.saldo}\n")

  def transfereValor(self, contaDestino, valor):
    if self.saldo < valor:
      return ("Não existe saldo suficiente!")
    else:
      contaDestino.depositar(valor)
      self.saldo -= valor
      return ("Transferência Realizada!")

def main():
  c1 = Conta(1, 1, "Bruno G.", 1000)
  c2 = Conta(2, 2, "Bruno G. 2.", 500)

  c1.depositar(300)
  c1.gerar_extrato()

  valor_saque = 200
  resultado_saque = c1.sacar(valor_saque)

  if resultado_saque:
    print(f"Saque de R${valor_saque} realizado com sucesso!\n")
    print(f"Saldo atual: R${c1.saldo}")
  else:
    print("Saldo insuficiente para realizar o saque.\n")

  c1.gerar_extrato()

  c1.transfereValor(c2, 800)
  print("Saldo após a tranferência")
  print(f"Saldo da conta 1: R${c1.saldo}")
  print(f"Saldo da conta 2: R${c2.saldo}")

if __name__ == "__main__":
  main()