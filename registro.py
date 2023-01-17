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

def imprimirContacto(contacto):
    tpl=":key: :value\t"
    msj=""
    print("\nDIRECTORIO TELEFONICO")
    for key in contacto.keys():
        msj += tpl.replace(":key",key).replace(":value", contacto[key])
    print(msj)
  
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
 




#pruebas

llenarDirectorio()

for contacto in directorio:
    imprimirContacto(contacto)







