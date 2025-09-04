class Conta:
  def __init__(self, numero, cpf, nomeTitular, saldo):
    self.numero = numero
    self.cpf = cpf
    self.nomeTitular = nomeTitular
    self.saldo = saldo

def main():
  c1 = Conta(1, 1, "Bruno G.", 1200)
  print(f"Nome do Titular: {c1.nomeTitular}")
  print(f"Número da Conta: {c1.numero}")
  print(f"CPF: {c1.cpf}")
  print(f"Saldo da conta: {c1.saldo}")

if __name__ == "__main__":
  main()


