'''
Ejercicio 5: Gestión de Contactos

    Requisito 1: Añadir Contacto

        Crea una función que permita añadir un contacto a un diccionario, 
        donde la clave sea el nombre y el valor sea el número de teléfono.

    Requisito 2: Buscar Contacto

        Crea una función que permita buscar un contacto por nombre.

        Esto debe ser manejado desde un menú:
'''
'''
Para darle mas dificultad le puedo agregar que los contactos se guarden en
minusculo o mayuscula
- Verificar la cantidad de numeros ingresados con un len
'''


# Aqui hago el menu con una funcion
def menu(): 
    
    print ("1.- Añadir contacto\n2.- Buscar contacto\n3.- SALIR\n")

# Aqui me pongo añadir os contactos y numeros al diccionario
def Añadir_contactos(diccionario_de_contactos):

    clave = str (input("Nombre del contacto: "))
    valor = int (input("Nombre del numero: "))
    diccionario_de_contactos[clave] = valor
    print ("Añadido con exito")

# Aqui se buscan el numeor con el nombre ingresado
def buscar_contacto(diccionario_de_contactos):

    clave = input("Nombre del contacto a buscar: ")
    if clave in diccionario_de_contactos:
        print(f"telefono de {clave}: {diccionario_de_contactos[clave]}")
    else:
        print(f"No se encontró el contacto {clave}.")

diccionario_de_contactos = {} #Los diccionarios van con llaves

while True:
    menu()
    opcion = int(input("Opcion: "))

    if opcion == 1:
        Añadir_contactos(diccionario_de_contactos)

    elif opcion == 2:
        buscar_contacto(diccionario_de_contactos)
    
    elif opcion == 3:
        break
    else:
        print("Opcion ingresada incorrecto")
