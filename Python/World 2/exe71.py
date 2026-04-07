"""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

valor = int(input("Valor a ser sacado(int number): R$"))

#NOTAS 50
if valor >= 50:
  notas_50 = valor // 50
  print(f"{notas_50} nota(s) de R$50.")
  valor = valor % 50

#NOTAS 20
if valor >= 20:
  notas_20 = valor // 20
  print(f"{notas_20} nota(s) de R$20.")
  valor = valor % 20

#NOTAS 10
if valor >= 10:
  notas_10 = valor // 10
  print(f"{notas_10} nota(s) de R$10.")
  valor = valor % 10

#NOTAS 1
if valor >= 1:
  notas_1 = valor // 1
  print(f"{notas_1} nota(s) de R$1.")
  valor = valor % 1
