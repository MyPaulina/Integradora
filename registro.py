'''cree un directorio telefonico que conserve los siguientes datos 
(ID, nombre, apellido paterno, apellido materno, teléfono, correo)
1) Carga de datos e imprimirlos
2) Coloque como índice o clave el ID del contacto para identificarlo
3) Modificar cualquiera de los datos de un contacto solo si se requiere
4) Muestre los cambios realizados'''

directorio=[]

def registrarContacto(id):
    contacto=dict(
        id=f'{id}',
        nombre=input("Ingrese el nombre:"),
        apellido_paterno=input("Ingrese el apellido paterno:"),
        apellido_materno=input("Ingrese el apellido materno:"),
        telefono=input("Ingrese el teléfono:"),
        email=input("Ingrese el email:")
    )
    return contacto

def imprimirDirectorio():
    tpl=":key: :value\t"
    msj=""
    print("\nDIRECTORIO TELEFONICO")
    for contacto in directorio:
        for key in contacto.keys():
            msj += tpl.replace(":key",key).replace(":value", contacto[key])
    print(msj+"\n")
  
def llenarDirectorio():
    if directorio:
        continua=input("¿Desea agregar otro contacto al directotio?[s/n]:\n")
        if continua=="s":
            agregaralDirectorio()
            llenarDirectorio()
    else:
        agregaralDirectorio()
        llenarDirectorio()


def agregaralDirectorio():
    id=len(directorio)+1
    contacto=registrarContacto(id)
    directorio.append(contacto)
 

def modificarContacto ():
    imprimirDirectorio()
    id=int(input("Ingrese el Id del usuario que desea editar:\n"))
    contacto=registrarContacto(id)
    directorio[id-1]=contacto


def nyz():
    contacto=directroio[0]
    for key in contacto.keys():
        





for key in lista: 
    print(key +" "+ diccionario [key])

diccionario ["Edad"]=str(input("\nModifica la edad: "))
for key in lista: 
    print(key +" "+ diccionario [key])
    
diccionario ["Altura"]=str(input("Modifica la altura: "))
print()
for key in lista: 
    print(key +" "+ diccionario [key])
    

mytuple = tuple(lista)
print(mytuple)




#pruebas

llenarDirectorio()
modificarContacto()
imprimirDirectorio()

nyz()









