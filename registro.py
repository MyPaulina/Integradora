

def registrarContacto(id):
    contacto=dict(
        id=str(id),
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
  
gato=registrarContacto(1)
imprimirContacto(gato)
