"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

import random
numberUser = int(input("Escolha um número inteiro: "))
computador = random.randint(0, 100)
print(computador)
