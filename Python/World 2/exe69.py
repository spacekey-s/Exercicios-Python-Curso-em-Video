"""Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos."""
import time

print("-="*25)
print("Cadastro de Pessoas")
print("-="*25)

while True:
  ageUser = int(input("Digite sua idade: "))
  sexUser = str(input("Digite seu sexo: "))
  condStop = str(input("Você deseja continuar? [S/N] => ")).strip().upper()
  #condição
  if "S" in condStop:
    print("Finalizando...")
    time.sleep(3)
    break
