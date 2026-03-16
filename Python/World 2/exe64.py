#variables
contador = 0
calcNumeros = 0
quantidadeNumeros = 0

#loop
while contador != 999:
  numbers = int(input("Digite um número[999 pra parar]: "))
  if numbers != 999:
    quantidadeNumeros += 1
    calcNumeros += numbers
  #condition
  elif numbers == 999:
    contador = 999#stop condition

print(f"Você digitou {quantidadeNumeros} números. O cálculo total é {calcNumeros}.")
