'''
        Ejercicio 7: Sistema de Biblioteca

Requisito 1: Añadir Libro

    Crea una función que permita añadir libros a un diccionario, donde la clave sea el título y el valor sea el autor.	

Requisito 2: Buscar Libro
    
    Crea una función que permita buscar un libro por su título.

'''


# Función para mostrar el menú de opciones
def menu():
    print('''
         1.- Añadir libro
         2.- Buscar libro
         3.- Salir
         ''')


# Función para añadir un libro al diccionario
def añadir_libro(diccionario_libros):
    titulo = input("Nombre del LIBRO: ")  # Solicita el título del libro al usuario
    autor = input("Nombre del AUTOR: ")   # Solicita el nombre del autor al usuario
    
    diccionario_libros[titulo] = autor    # Añade el libro (título) con su autor al diccionario
    print(f"Libro '{titulo}' de {autor} añadido con éxito.")  # Confirma que el libro ha sido añadido


# Función para buscar un libro en el diccionario
def buscar_libro(diccionario_libros):
    titulo = input("Ingrese el título del libro a buscar: ")  # Solicita el título del libro a buscar
    
    if titulo in diccionario_libros:  # Verifica si el título está en el diccionario
        print(f"El libro '{titulo}' es de {diccionario_libros[titulo]}.")  # Muestra el autor si se encuentra el libro
    else:
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")  # Muestra un mensaje si el libro no está en el diccionario


diccionario_libros = {}  # Inicializa el diccionario de libros vacío




while True:  # Bucle principal que muestra el menú y ejecuta las opciones
    menu()  # Muestra el menú
    try:
        opcion = int(input("Opción: "))  # Solicita la opción al usuario y la convierte a entero
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")  # Si la entrada no es un número, muestra un mensaje de error
        continue  # Continúa con la siguiente iteración del bucle

    if opcion == 1:  # Verifica si la opción es 1 (añadir libro)
        añadir_libro(diccionario_libros)  # Llama a la función para añadir un libro

    elif opcion == 2:  # Verifica si la opción es 2 (buscar libro)
        buscar_libro(diccionario_libros)  # Llama a la función para buscar un libro

    elif opcion == 3:  # Verifica si la opción es 3 (salir)
        print("Haz seleccionado -- SALIR --")  # Imprime un mensaje de salida
        break  # Sale del bucle y termina el programa

    else:
        print("Opción incorrecta, vuelva a intentarlo")  # Muestra un mensaje si la opción es incorrecta
