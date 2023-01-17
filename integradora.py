'''cree una directorio telefonico que conserve los siguientes datos 
(ID, nombre, apellido paterno, apellido materno, teléfono, correo)
1) Carga de datos e imprimirlos
2) Coloque como índice o clave el ID del contacto para identificarlo
3) Modificar cualquiera de los datos de un contacto solo si se requiere
4) Muestre los cambios realizados'''

#1) Carga de datos e imprimirlos
def cargar():
    directorio={}
    continua="s"
    while continua=="s":
        ID=int(input("Ingrese el numero de ID:"))
        nombre=input("Ingrese el nombre:")
        apellido_paterno=input("Ingrese el apellido paterno:")
        apellido_materno=input("Ingrese el apellido materno:")
        telefono=input("Ingrese el teléfono:")
        email=input("Ingrese el email:")
#2- Coloque como índice o clave el ID del contacto para identificarlo
        directorio[ID]=[nombre, apellido_paterno, apellido_materno, telefono, email]
        continua=input("¿Desea agregar otro contacto al directotio?[s/n]:\n")
    return directorio

#1) imprimirlos
def imprimir(directorio):
    print("\nDIRECTORIO TELEFONICO")
    for ID in directorio:
        print(ID,"...",directorio[ID][0],directorio[ID][1],directorio[ID][2],directorio[ID][3],directorio[ID][4])

#3) Modificar cualquier dato de un contacto si se requiere
'''def modificar(directorio):
    ID=int(input("\nIngrese el ID a consultar:"))
    if ID in directorio:
        print(ID,"...",directorio[ID][0],"...",directorio[ID][1],"...",directorio[ID][2])
        "...",directorio[ID][3],"...",directorio[ID][4],
        nombre=input("Ingrese nuevo dato:")
        directorio[ID][0]=nombre
    else:
        print("ID no registrado")'''

def modificar(directorio):
    continua="s"
    while continua=="s":
        ID=int(input("\nIngrese el numero de ID a corregir:"))
        if ID in directorio:
            continua1=input("¿Desea corregir el nombre? [s/n]:\n")
            nombre=input("Ingrese nuevo nombre:")
            directorio[ID][0]=nombre
            continua=input("Desea corregir los datos de otro ID [s/n]:\n")
        else:
            print("No existe el ID ingresado")
    return directorio



# bloque principal
directorio=cargar()
imprimir(directorio)
modificar(directorio)
imprimir(directorio)

