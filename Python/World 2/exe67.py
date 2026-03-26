#laço
while True:
  number = input("Qual tabuada você quer ver? ").strip().replace(" ", "")
  #condições
  if "-" in number[0]:
    print("Saindo...")
    break
  else:
    for tabu in range(1, 11):
      calcResultado = int(number[0]) * tabu
      print(f"{number[0]} x {tabu:>2} = {calcResultado}")
