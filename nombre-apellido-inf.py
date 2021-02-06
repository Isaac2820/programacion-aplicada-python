nombre= input("¿Cual es su primer nombre?");
apellido=input("¿Cual es su apellido?");

ciudad= input("¿DONDE VIVE?");
space=""

edad= int(input("¿Que edad tiene?"));
print("Bienvenido ",nombre,space,apellido,space,"esta en ",ciudad,"tienes",space,edad,"años",space,"por lo tanto UD ")
if edad >=1 and edad <=10:
    print("SE ENCUENTRA EN UNA EDAD PREADOLESCENTE ")
elif edad >=11 and edad <=18:
    print("SE ENCUENTRA EN UNA EDAD ADOLESCENTE")
elif edad>=19 and edad <=90:
    print("SE ENCUENTRA EN UNA EDAD MADURA ")
else:
    print("ERROR")

