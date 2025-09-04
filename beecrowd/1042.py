# Sort Simples

# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

values = list(map(int, input().split()))

values_no_ordered = values.copy()

values.sort()

values_ordered = values

for val in values_ordered:
  print(val)

print()

for val in values_no_ordered:
  print(val)









