file=open("devices.txt","a")

while True:
    newItem=input("Ingrese nuevo dispositivo: ")
    if newItem=="exit":
      print("LISTPO" +"\n")
      break
    else:
       file.write(newItem+"\n")
file.close()
       



