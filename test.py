# def imprimir_valores (n1, n2, n3):
#     print(f"Número inteiro: {n1} (tipo: {type(n1)})")
#     print(f"Número de ponto flutuante: {n2} (tipo: {type(n2)})")
#     print(f"Valor booleano: {n3} (tipo: {type(n3)})")
    
# n1 = int(input("Digite um número inteiro: "))
# n2 = float(input("Digite um número de ponto flutuante: "))
# n3 = bool(input("Digite um valor booleano: "))

# imprimir_valores(n1, n2, n3)

def calcula_preco (preco_unitario, quantidade):
    try:
        return preco_unitario * quantidade
    except TypeError:
        print(f"Erro: Os valores de preço e quantidade devem ser numéricos.")
        return None

try:
    preco_unitario = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))

    preco = calcula_preco(preco_unitario, quantidade)

    if preco is not None:
        print(f"Preço do produto é de {preco:.2f}")
    else:
        print("Não foi possível calcular o preço final.")

except ValueError:
    print("Erro: Por favor, digite valores numéricos válidos para preço e quantidade.")
