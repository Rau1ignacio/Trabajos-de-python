'''
Ejercicio 4: Gestión de Tareas

    Requisito 1: Añadir Tarea
    
    Crea una función que permita al usuario añadir tareas a una lista.
    
    Requisito 2: Mostrar Tareas
    
    Crea una función que muestre todas las tareas de la lista.
    
    Esto debe ser manejado desde un menú:

'''

'''
while True:
    #Muestro el Menu:
    menulista = ["1.- Añadir tareas \n2.- Mostrar Tareas\n3.- Salir\n"]
    for menu in menulista:
        print (menu)
        opcion = int (input("Opcion: "))

    if opcion == 1:

        # Requisito 1 Añadir tareas

        def Añadir_tareas():

            lista_tareas = []

            Añadir_tareas_1 = (input("Nombre la tarea qu equiera agregar: "))

            lista_tareas.append(Añadir_tareas_1)

            return lista_tareas
        
        Añadir_tareas_1 = Añadir_tareas()
        

    elif opcion == 2:

        # Requisito 2 Mostrar tareas

        def mostrar():

            for Mostrar_tareas in Añadir_tareas_1:
                print (Mostrar_tareas)

    elif opcion == 3:
        break
    
    else:
        print("Opción no válida. Inténtelo de nuevo.")
'''


'''

def Añadir_tareas():

    lista_tareas = []

    Añadir_tareas_1 = (input("Nombre la tarea qu equiera agregar: "))

    lista_tareas.append(Añadir_tareas_1)

    return lista_tareas


Añadir_tareas_1 = Añadir_tareas()


# Requisito 2 Mostrar tareas
def mostrar():

    for Mostrar_tareas in Añadir_tareas_1:
        print (Mostrar_tareas)

'''


# codigo hecho con chatGPT

# Las funciones debemos ponerlas fuera del ciclo porque son mas eficientes}
# Lo que esta dentro del argumento es la lista
#

def añadir_tareas(lista_tareas):
    tarea = input("Nombre la tarea que quiera agregar: ")
    lista_tareas.append(tarea)

# El for es para mostrar la lista de tareas
def mostrar_tareas(lista_tareas):
    if lista_tareas:
        for tarea in lista_tareas:
            print(tarea)
    else:
        print("No hay tareas en la lista.")

def menu():
    print("1.- Añadir tareas")
    print("2.- Mostrar tareas")
    print("3.- Salir")

# Lista de tareas inicial vacía
lista_tareas = []


# iniciamos el bucle 
while True:
    menu() # se desplega el menu hecho en la funcion
    opcion = int(input("Opción: ")) # almacenamos el valor

    #segun lo puesto en opcion nos va a dirigir a las distintas opciones
    if opcion == 1:
        añadir_tareas(lista_tareas)
    elif opcion == 2:
        mostrar_tareas(lista_tareas)
    elif opcion == 3:
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
