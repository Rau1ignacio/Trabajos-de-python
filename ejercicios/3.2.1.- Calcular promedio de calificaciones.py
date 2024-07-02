'''
Requisito 1: Calcular Promedio

Crea una función que reciba una lista de calificaciones y devuelva el promedio.

Requisito 2: Validar Entradas

Valida que las calificaciones estén entre 0 y 10.
'''

'''

#codigo hecho por raul
Lista_de_calificaciones = []

def calificaciones(lista_de_calificaciones):
    calificacion = int (input("Introduzca calificacion 1: "))
    if calificacion > 0 and calificacion < 10:
        Lista_de_calificaciones.append(calificacion)
    
    promedio = calificaciones 
    #Validacion de entradas
    
    

calificaciones()

'''

# se hace una funcion para el calculo del promedio
def calcular_promedio(lista_de_calificaciones):
    if not lista_de_calificaciones:
        return 0  # Evitar división por cero si la lista está vacía
    return sum(lista_de_calificaciones) / len(lista_de_calificaciones)
    #sum para sumar las calificaciones y el len para contar cuantas calificaciones son dentro de la lsita


# Segunda funcion para poder validar los alores ingresados
def validar_calificacion(calificacion):
    return 0 <= calificacion <= 10

# Una funcion para la lista
def ingresar_calificaciones():
    lista_de_calificaciones = []

    while True:

        try:
            calificacion = float(input("Introduzca una calificación entre 0 y 10 (o -1 para terminar): "))
            
            # el -1 es para poder de terminar de agregar notas a las lista y poder hacer el promedio
            if calificacion == -1:
                break
                
            #Si los valores entan dentro del rango se ejecuta este if y añade el valor a la lista
            if validar_calificacion(calificacion):
                lista_de_calificaciones.append(calificacion)

            #los valores deben estar entre 0 y 10
            else:
                print("Calificación no válida. Debe estar entre 0 y 10.")

        except ValueError:
            print("Entrada no válida. Por favor, introduzca un número.")

    return lista_de_calificaciones

# Añado los valor de ingresar_calificaciones a la lista.
lista_de_calificaciones = ingresar_calificaciones()
#calculo de promedio
promedio = calcular_promedio(lista_de_calificaciones)
#muestro los valores de la lista y el promedio en pantalla
print(f"Las calificaciones son: {lista_de_calificaciones}")
print(f"El promedio de las calificaciones es: {promedio}")
