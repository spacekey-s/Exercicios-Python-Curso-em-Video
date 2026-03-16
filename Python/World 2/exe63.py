#F(n)=F(n−1)+F(n−2)

numberInt = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print(f"{t1} -> {t2}", end=" ")
contador = 3#porque já existe o valor de 1 e 2
#laço
while contador <= numberInt:
  t3 = t1 + t2
  print(f"-> {t3}",end="")
  contador += 1

print("Fim")
