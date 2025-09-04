def calcula_imc (peso, altura):
  return peso * 100 / (altura * 2)

peso = eval(input("Digite o peso em KG: "))
altura = eval(input("Digite a altura em CM: "))
calcula_imc(peso, altura)
imc = calcula_imc(peso, altura)
print(f"IMC é de {imc:.2f}")