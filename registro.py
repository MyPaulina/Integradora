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








#pruebas

llenarDirectorio()
modificarContacto()
imprimirDirectorio()








