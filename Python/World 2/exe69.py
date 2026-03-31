"""Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos."""
import time

listUsers = []
listMaior = []

print("-="*25)
print("Cadastro de Pessoas")
print("-="*25)

while True:
  ageUser = int(input("Digite sua idade: "));listUsers.append(ageUser)
  sexUser = str(input("Digite seu sexo [M/F]: ")).replace(" ", "").upper();listUsers.append(sexUser)

  #condição para a lista maior
  if ageUser > 18:
    listMaior.append(sexUser)

  print("-"*25)
  print("Cadastro concluído!")
  print("-"*25)

  condStop = str(input("Você deseja continuar? [S/N] => ")).strip().upper()

  #condição de parada
  if "N" in condStop:
    print("Finalizando...")
    time.sleep(3)
    break
