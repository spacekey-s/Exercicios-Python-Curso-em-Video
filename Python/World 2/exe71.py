print("-="*25)
print("CAIXA ELETRÔNICO")
print("-="*25)

valor = int(input("Valor a ser sacado(int number): R$"))

print("-="*20)

#NOTAS 50
if valor >= 50:#notas de 50
  notas_50 = valor // 50
  print(f"{notas_50} nota(s) de R$50.")
  valor = valor % 50

#NOTAS 20
if valor >= 20:#notas de 20
  notas_20 = valor // 20
  print(f"{notas_20} nota(s) de R$20.")
  valor = valor % 20

#NOTAS 10
if valor >= 10:#notas de 10
  notas_10 = valor // 10
  print(f"{notas_10} nota(s) de R$10.")
  valor = valor % 10

#NOTAS 1
if valor >= 1:#notas de 1
  notas_1 = valor // 1
  print(f"{notas_1} nota(s) de R$1.")
  valor = valor % 1

print("-="*20)
