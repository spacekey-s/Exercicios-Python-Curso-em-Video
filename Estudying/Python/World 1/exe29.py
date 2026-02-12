"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

#i need km
velocityCar = float(input("Enter the car's speed: "))
#conditions
if velocityCar == 80:
  #show result
  print("You are average.")
  print(f"Average {velocityCar}KM.")
else:
  #calculate
  kmExceeded = velocityCar - 80
  calcFine = kmExceeded * 7
  #show result
  print(f"You exceeded the average by {kmExceeded}KM above (80KM standard).")
  print(f"Thefore, your fine will be R${calcFine}.")


