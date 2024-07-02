'''
    Ejercicio 6: Lista de Compras

Requisito 1: Añadir Producto

    Crea una función que permita añadir productos a una lista de compras.

Requisito 2: Mostrar Lista de Compras

    Crea una función que muestre todos los productos en la lista.

    Esto debe ser manejado desde un menú :

'''

def menu(): #Hago el menu en una funcion
    print ('''
           1.- Añadir productos
           2.- Mostrar lista de compras
           3.- SALIR''')

def añadir_productos(lista_de_compras): # Hago una funcion para añadir productos
    añadir = str (input("Nombre del producto: ")) # Pongo el nombre del producto
    lista_de_compras.append(añadir) # lo añado a la lista

def mostrar_compras(lista_de_compras): # Esta funcion es para mostrar los que añadi en la lista
    for Mostrar in lista_de_compras: # se debe hacer un or para poder visualizar las listas
        print (Mostrar) # Muestro la lista en pantalla
    

lista_de_compras = [] # Inicio la lista



while True: # hago un bucle para manejar el menu con sus opciones
    menu()
    opcion = int (input("\n Opcion: "))

    if opcion == 1:
        añadir_productos(lista_de_compras)

    elif opcion == 2:
        mostrar_compras(lista_de_compras)

    elif opcion == 3:
        print ("Haz seleccionado -- SALIR --")
        break
    else:
        print ("Opcion incorrecta, vuelva a intertarlo")