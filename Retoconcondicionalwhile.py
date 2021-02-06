while True:
    num=input("INGRESE UN NUMERO PARA EL CONTEO:")
    if num=='q' or num=='quit':
        break
    num=int(num)
    y=1
    while True:
      print(y)
      y=y+1
      if y>num:
        break

