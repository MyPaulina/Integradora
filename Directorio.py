'''cree un directorio telefonico que conserve los siguientes datos (ID, nombre, apellido paterno,
apellido materno, teléfono, correo)
1) Carga de datos e imprimirlos
2) Coloque como índice o clave el ID del contacto para identificarlo
3) Modificar cualquiera de los datos de un contacto solo si se requiere
4) Muestre los cambios realizados'''

#1) Carga de datos
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
def modificar(directorio):
     ID=int(input("\nIngrese el ID de contacto a modificar:"))
     if ID in directorio:
        print(ID,"...",directorio[ID][0],directorio[ID][1],directorio[ID][2],directorio[ID][3],directorio[ID][4])
        while True:
            menu="""Seleccione el campo que desea editar [0 al 5]:
1-Nombre
2-Apellido paterno
3-Apellido materno
4-Teléfono
5-E-mail
0-Salir """    
            print(menu)
            opcion=int(input("\nCampo a  editar:"))
            if opcion==1:
                nombre=input("Edita el nombre:")
                directorio[ID][0]=nombre
                c=input("Desea editar otro campo si/no:")
                if c=="no":
                    return directorio
            elif opcion==2:
                apellido_paterno=input("Edita el apellido paterno:")
                directorio[ID][1]=apellido_paterno
                c=input("Desea editar otro campo si/no:")
                if c=="no":
                    return directorio
            elif opcion==3:
                apellido_materno=input("Edita el apellido materno:")
                directorio[ID][2]=apellido_materno
                c=input("Desea editar otro campo si/no:")
                if c=="no":
                    return directorio
            elif opcion==4:
                telefono=input("Edita el telefono:")
                directorio[ID][3]=telefono
                c=input("Desea editar otro campo si/no:")
                if c=="no":
                    return directorio
            elif opcion==5:
                email=input("Edita el email:")
                directorio[ID][4]=email
                c=input("Desea editar otro campo si/no:")
                if c=="no":
                    return directorio
            elif opcion==0:
             return directorio

            else:
             print("Opción incorrecta")
             return(modificar(directorio))
     else:
         print("Ingrese un ID válido")
         return(modificar(directorio))
    
    
    

# bloque principal
directorio=cargar()
imprimir(directorio)
modificar(directorio)
imprimir(directorio)

