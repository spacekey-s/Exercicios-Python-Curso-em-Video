#lista
listNumeros = []

#loop
while True:
  numeros = int(input("Digite um número: "))
  #condição
  if numeros == 999:
    break
  listNumeros.append(numeros)

#resultado
print(f"A soma entre os números: {sum(listNumeros)}.")
print(f"{len(listNumeros)} números foram digitados.")
