'''Ejercicio nombre y apellido'''

# Requisito 1

def Recibir_nombre_apellido():
    lista_Nombre = []
    lista_Apellido = []

    nombre = (input("\nPon tu nombre: "))
    Apellido = (input("Pon tu Apellido: "))
    
    lista_Nombre.append(nombre)
    lista_Apellido.append(Apellido)
    
    return lista_Nombre, lista_Apellido


nombre, Apellido = Recibir_nombre_apellido()

#requisito 2

for elemento in nombre:
    print (f"\nTu nombre es: {elemento}")
    for elemento2 in Apellido:
        print (f"Tu apellido es: {elemento2}\n")

# Solicito el año de nacimiento al usuario
fecha_de_nacimiento = int(input("¿Cuál es tu año de nacimiento?: "))

def calcular_edad(fecha_de_nacimiento):
    
    fecha_actual = 2024
    edad = fecha_actual - fecha_de_nacimiento
    return edad

# Llamar a la función pasando el año de nacimiento como argumento
edad = calcular_edad(fecha_de_nacimiento)
print(f"Tu edad es de: {edad} años.\n")

