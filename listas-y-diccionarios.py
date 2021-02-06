  
#creacion de listas 
lista=["R1",5.5,6,True,"R2"]
print(lista[1])
print(lista[-1])
print(lista[-5])
del lista[4]
print(lista)
lista[1]="R3"
print(lista)
del lista[-2]
print(lista)

#creacion de diccionarios
dict1={"R1":"192.168.0.1",
       "R2":"192.168.0.2",
       "R3":"192.168.0.3"}
print(dict1)
print(dict1['R2'])
dict1['R4']="102.168.0.4"
dict1['S3']="192.168.1.3"
print("S3" in dict1)
#creacion de tuplas
nombre=("Caldeon","Isaac")
print(nombre)
print(nombre[0])

