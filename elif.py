acl=int(input('Ingrese el numero de acl: '))
if acl>=1 and acl<=99:
    print('la acl es estandar')
elif acl>=100 and acl<=199:
    print('el acl es Extendida')
else: 
    print('el numero ingresado no es de una acl')