#variables
firstTerm = int(input("Primeiro termo: "))
reason = int(input("Digite a razão: "))
contador = 0
n = 1
#loop
while contador < 10:
  term = firstTerm + (n - 1) * reason# formule
  contador += 1
  n += 1
  print(term,end=" > ")
print("Fim")
