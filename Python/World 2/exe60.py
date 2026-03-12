#Maneira com módulos atuais
"""import math


numberFact = int(input("Digite um número: "))

factorial = math.factorial(numberFact)

print(f"O factorial do número {numberFact} é {factorial}.")"""

numberFact = int(input("Digite um número: "))
counter = numberFact

while counter > 0:
  counter -= 1
  print(counter)
