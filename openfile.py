lista=[]
file=open("devices.txt")
for a in file:
    a=a.strip()
    lista.append(a)
    print(a)
file.close()
print(lista)
    


