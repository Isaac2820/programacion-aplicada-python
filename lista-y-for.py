lista1=["R1","R2","R3","S1","S2","S3"]
for i in lista1:
    if "R" in i:#evalua si hay valores con R
        print(i)
     
#crear 2 listas en blanco y llenarlas 
switches=[]
routers=[]
for i in lista1:
    if "S"in i:
        switches.append(i)
