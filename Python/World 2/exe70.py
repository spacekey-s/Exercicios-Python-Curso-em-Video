'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

import time

listPriceProducts = []
listProductsExpensive = []
nameAndValue = []

while True:
  print("-="*25)
  nameProduct = str(input("Digite o nome do produto: "))
  priceProduct = float(input("Informe o valor: R$"));listPriceProducts.append(priceProduct)#adicionando valor na lista

  #condiçao para saber quem é o menor
  productCheap = min(listPriceProducts)

  if priceProduct == productCheap:
    nameAndValue.clear()
    nameAndValue.append(nameProduct)
    nameAndValue.append(productCheap)

  #condição para a lista de produtos caros // listProductsExpensive
  if priceProduct > 1000:
    listProductsExpensive.append(priceProduct)

  #condição de parada
  condStop = str(input("Deseja parar? [S/N] ")).replace(" ", "").upper()
  if condStop == "S":
    print("-="*25)
    print("Finalizando...")
    time.sleep(3)
    print(f"Total da compra: R${sum(listPriceProducts)}.")
    print(f"{len(listProductsExpensive)} produtos com o valor acima de R$1000.")
    print(f"O nome do produto mas barato é o {nameAndValue[0]}.")
    break
