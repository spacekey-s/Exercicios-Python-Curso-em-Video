import random

listaGanhos = []

while True:
  numberUser = int(input("Escolha um número inteiro [0/10]: "))
  choiceUser = str(input("Par ou Ímpar? [P/I] = ")).strip().replace(" ", "").upper()
  numberComp = random.randint(0, 10)

  calc = numberUser + numberComp
  rest = calc % 2

  print(f"Computador escolheu {numberComp}.")

  if rest == 0 and choiceUser == "P":#par
    print("Par")
    print("Você ganhou!")
    listaGanhos.append(+1)

  elif rest != 0 and choiceUser == "I":#ímpar
    print("Ímpar")
    print("Você ganhou!")
    listaGanhos.append(+1)

  elif rest != 0 and choiceUser == "P":
    print("Ímpar")
    print("Você perdeu!")
    print(f"Você ganhou {len(listaGanhos)} vezes consecutivas")
    break

  elif rest == 0 and choiceUser == "I":
    print("Par")
    print("Você perdeu!")
    print(f"Você ganhou {len(listaGanhos)} vezes consecutivas")
    break
