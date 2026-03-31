"""Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos."""
import time
from colorama import Fore, Style

listUsers = []
listMaior = []
listMulher = []

print("-="*25)
print("Cadastro de Pessoas")
print("-="*25)

while True:
  ageUser = int(input("Digite sua idade: "));listUsers.append(ageUser)
  sexUser = str(input("Digite seu sexo [M/F]: ")).replace(" ", "").upper();listUsers.append(sexUser)

  #condição para a listMaior
  if ageUser > 18:
    listMaior.append(sexUser)
  #condição para listMulher
  if ageUser < 20 and sexUser == "F":
    listMulher.append(sexUser)

  print("-"*19)
  print(Fore.GREEN + "Cadastro concluído!" + Style.RESET_ALL)
  print("-"*19)

  condStop = str(input("Você deseja continuar? [S/N] => ")).strip().upper()
  print("-="*25)

  #condição de parada
  if "N" in condStop:
    print("Finalizando...")
    time.sleep(3)
    print(f"{len(listMaior)} pessoa(s) com idade superior a 18 anos.")
    print(f"Quantidade de {listUsers.count("M")} pessoa(s), do sexo masculino. ")
    print(f"{len(listMulher)} mulhere(s), com idade inferior a 20 anos.")
    break
