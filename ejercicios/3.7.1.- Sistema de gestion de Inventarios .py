'''
    Ejercicio: Sistema de Gestión de Inventarios
Descripción:
    Vas a crear un sistema básico de gestión de inventarios para una tienda. Este sistema permitirá añadir nuevos productos, eliminar productos existentes, actualizar la cantidad de productos y mostrar el inventario completo. Debes implementar las siguientes funcionalidades:
    1.	Añadir Producto: Permite al usuario añadir un nuevo producto al inventario. Cada producto debe tener un nombre, una cantidad y un precio.
    2.	Eliminar Producto: Permite al usuario eliminar un producto del inventario por su nombre.
    3.	Actualizar Cantidad: Permite al usuario actualizar la cantidad de un producto existente en el inventario.
    4.	Mostrar Inventario: Muestra una lista de todos los productos en el inventario con su nombre, cantidad y precio.
    5.	Buscar Producto: Permite al usuario buscar un producto por su nombre y mostrar sus detalles si está en el inventario.	 
Requisitos:
    1.	Funciones: Debes crear funciones para cada una de las funcionalidades mencionadas anteriormente.
    2.	Listas: Utiliza listas para almacenar los productos del inventario. Cada producto puede ser representado como un diccionario con las claves "nombre", "cantidad" y "precio".
    3.	Variables: Utiliza variables adecuadamente para manejar los datos del inventario y las entradas del usuario.
    4.	Bucles: Utiliza bucles para permitir al usuario realizar múltiples operaciones hasta que decida salir del programa.
'''

def menu():
    print ('''
        1.- Añadir producto
        2.- Eliminar producto
        3.- Actualizar cantidad
        4.- Mostrar productos
        5.- Buscar producto
        
        6.- Salir
           
''')

#Funcion para añadir un producto
def Añadir_producto(Lista_diccionario):

    while True:
        #Aquí añado las variables
        #Borro los espacios en blanco con un .strip() para minimizar errores en el futuro
        nombre = input ("Nombre del Producto: ").strip()
        cantidad = int (input("Cantidad: ").strip())
        precio = float (input("Precio: ").strip())
        
        #las guardo en un diccionario
        producto = {
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio
        }

        Lista_diccionario.append(producto) #añado al inventario
        print(f"-- Pruducto {nombre} añadido con exito! --")# le digo al usuario el producto añadido
        
        # Preguntar al usuario si desea añadir otro producto
        opc = input("\n¿Quieres añadir otro producto? si/no: ").strip().lower() # El .strip()es para eliminar los espacios en blanco y el .lower() para guardarlo en minusculas
        if opc == "no":
            break  # Salir del bucle si la respuesta es 'no'

#Funcion para eliminar un producto
def Eliminar_producto(Lista_diccionario):
    nombre = input("¿Qué producto quieres eliminar?: ").strip().lower()

    for producto in Lista_diccionario: #recorro la lsita
        if producto['nombre'] == nombre: # verifico si el producto que quiero eliminar esta en el inventario y es el mismo que pudo el usuario
            Lista_diccionario.remove(producto) # elimino el producto
            print(f"Producto '{nombre}' eliminado con éxito.") # Le informo al usuario que el producto ha sido eliminado
            break # cierro el bucle
    else:
        # Si no esta el producto le informo que no ha sido encontrado
        print(f"Producto '{nombre}' no encontrado.")

#Funcion para actualizar una cantidad
def Actualizar_cantidad(Lista_diccionario):

    nombre = input("Nombre del producto a actualizar: ").strip().lower()

    for producto in Lista_diccionario: #recorro el inventario

        if producto['nombre'].lower() == nombre: #verifico si el nombre es igual a uno del inventario

            cantidad = int (input(f"Cantidad nueva para '{nombre}': ").strip()) # Se pone la cantidad que desea actualizar

            producto['cantidad'] = cantidad  # Actualizo la cantidad del producto
            print(f"Cantidad de '{nombre}' actualizada a {cantidad}.") # Le informo al usuario que se actualizo con los valores que puso
            break
    else:
        print(f"Producto '{nombre}' no encontrado.")# le digo al usuario que el producto que quiere actualizar no esta en el inventario

#Funcion para mostar el inventario
def Mostrar_producto(Lista_diccionario):

    if not Lista_diccionario:  # Verifico si el inventario está vacío
        print("El inventario está vacío.")

    else: #Si no esta vacio se ejecuta este codigo

        print("\nInventario:") # Le digo que se está mostrando en pantalla

        for i, producto in enumerate(Lista_diccionario, 1): # 
            # muestro en pantalla el inventario
            print(f"{i}. Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']:.2f}")

#Funcion para buscar un producto
def Buscar_producto(Lista_diccionario):

    nombre = input("Nombre del producto a buscar: ").strip().lower()
    for producto in Lista_diccionario:
        if producto['nombre'].lower() == nombre.lower():
            print(f"Producto encontrado: Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']:.2f}")
            break
    else:
        print(f"Producto '{nombre}' no encontrado.")    


Lista_diccionario = []


#Bucle en cual va interacionar el usuario
while True:
    menu()# muestro el menu de opciones
    try:
        opcion = int (input("   Opcion: ").strip()) # el .strip elimina los espacios en blanco
    except ValueError: #Si el usuario pone algun otro valor que no sea int le digo que esta mal
        print ("    procura poner un NUMERO!\n")

    if opcion == 1:
        Añadir_producto(Lista_diccionario)
    
    elif opcion == 2:
        Eliminar_producto(Lista_diccionario)
    
    elif opcion == 3:
        Actualizar_cantidad(Lista_diccionario)
    
    elif opcion == 4:
        Mostrar_producto(Lista_diccionario)
    
    elif opcion == 5:
        Buscar_producto(Lista_diccionario)


    elif opcion == 6:
        print ("Saliendo...")
        break
    else:
        print("Error, procura haber seleccionado bien")
