while True:

  try:                                                                           #inserir numero 1
    numero1 = float(input("Adicione um numero (1°): "))                              # se usuario inserir float = ok, int = conversão, str = pedir input novamente.
  except:
    print("Inserir apenas algarismos")
    continue

  operações = ["+", "-", "*", "/"]
  print("\nAs operações são:  +  |  -  |  *  |  /  ")

  operador = input("Escolha uma operação ")                                      #inserir operação basica
  if operador not in operações:
    print("Escolha uma operação! ")
    operador = input("Escolha uma operação ")

  try:                                                                          #inserir numero 2
    numero2 = float(input("\nAdicione um numero (2°): "))                                 # se usuario inserir float = ok, int = conversão, str = pedir input novamente.
  except:
    print("Inserir apenas algarismos")
    numero2 = float(input("Adicione um numero (2°): "))

#operações
  if operador == "+":                                                             # soma
    resultado = float(numero1 + numero2)
    print("\no resultado da SOMA é", resultado)

  if operador == "-":                                                             # subtração
    resultado = float(numero1 - numero2)
    print("\no resultado da SUBTRAÇÃO é", resultado)

  if operador == "*":                                                             # multiplicação
    resultado = float(numero1 * numero2)
    print("\no resultado da MULTIPLICAÇÃO é", resultado)

  if operador == "/":                                                             # divisão
    resultado = float(numero1 / numero2)
    print("\no resultado da DIVISÃO é", resultado)

  break
