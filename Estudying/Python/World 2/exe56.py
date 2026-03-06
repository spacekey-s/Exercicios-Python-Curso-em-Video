"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

listName = []
calcAgeUsers = 0
listSex = []

#loop
for data in range(1, 5):
  nameUser = str(input("Your name: ")).replace(" ", "");listName.append(nameUser)
  ageUser = int(input("Your age: "));calcAgeUsers += ageUser
  sexUser = str(input("Your sex(M/F): ")).replace(" ", "").upper();listSex.append(listSex)

print(listName)
print(calcAgeUsers)
print(listSex)
