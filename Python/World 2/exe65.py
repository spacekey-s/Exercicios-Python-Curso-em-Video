#variables
condicao = 0
listNumbers = []

#loop
while condicao == 0:
  numbers = int(input("Digite um número: "))
  listNumbers.append(numbers)
  question = str(input("Deseja continuar ? [S/N] -> ")).strip().upper()

  #condition
  if question == "N":
    media = sum(listNumbers) / len(listNumbers)
    print(f"A média na soma dos valores é {media}.")
    print(f"Maior número: {max(listNumbers)}\nMenor número: {min(listNumbers)}")
    condicao = 1
