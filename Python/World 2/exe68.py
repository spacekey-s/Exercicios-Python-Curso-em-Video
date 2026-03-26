"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""
import time
import random

while True:
  numberUser = int(input("Escolha um número inteiro [0/10]: "))
  choiceUser = str(input("Par ou Ímpar? [P/I] = ")).strip().replace(" ", "").upper()
  numberComp = random.randint(0, 10)

  calc = numberUser + numberComp
  rest = calc % 2

  print(f"Computador escolheu {numberComp}.")

  if rest == 0:#par
    print("Par")
    if choiceUser == "P":
      print("Você ganhou!")

  elif rest != 0:#ímpar
    print("Ímpar")
    if choiceUser == "I":
      print("Você ganhou!")

  elif rest != 0:
    print("Par")
    if choiceUser == "P":
      print("Você perdeu!")

  elif rest == 0:
    print("Ímpar")
    if choiceUser == "I":
      print("Você perdeu!")
