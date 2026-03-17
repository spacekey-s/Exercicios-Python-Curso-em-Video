"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

condicao = 0
listNumbers = []

while condicao == 0:
  numbers = int(input("Digite um número: "))
  listNumbers.append(numbers)
  question = str(input("Deseja continuar ? [S/N] -> ")).strip().upper()

  if question == "N":
    media = sum(listNumbers) / len(listNumbers)
    print(f"A média na soma dos valores é {media}.")
    print(f"Maior número: {max(listNumbers)}\nMenor número: {min(listNumbers)}")
    condicao = 1
