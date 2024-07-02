

def menu():

    print ("\n1.- Agregar jugadores")
    print ("2.- Actualizar cantidad de goles")
    print ("3.- Eliminar jugadores")
    print ("4.- Mostrar top de jugadores")
    print ("\n5.- Salir")

lista_jugadores = []

def agregar_jugadores(lista_jugadores):
    # El usuario debe ingresar el nombre del jugador, el equipo al que 
    # pertenece y la cantidad de goles que ha marcado.
    while True:
        jugador = input("Nombre del jugador: ").strip().lower()
        equipo = input(f"Nombre del equipo de {jugador}: ").strip().lower()
        Goles_jugador = int (input(f"Cantidad de goles de {jugador}: ").strip())

        if Goles_jugador >= -1:
            print (f""" los datos ingresados son:
                   
            Nombre del jugador: {jugador}
            Equipo: {equipo}
            Goles: {Goles_jugador}
            """)
            validacion = input ("Es correcto? Si / No : ").strip().lower()

            if validacion == "si":

                Goles = {
                    'nombre': jugador,
                    'equipo': equipo,
                    'goles': Goles_jugador
                }

                lista_jugadores.append(Goles)
                print ("\n      Agregada con exito!!\n")
                break
            else: 
                print ("Valores no agregados, volveras al menu")
                break
        else:
            print ("\nValor incorrecto, vuelve a intentarlo\n")

def actualizar_goles(lista_jugadores):

    actualizar_gol = input("Que jugador quieres actualizar los goles? : ").strip().lower()

    for buscar_jugador in lista_jugadores:

        if buscar_jugador['nombre'] == actualizar_gol:
            print ("jugador encontrado\n")

            Cantidad_goles = int (input(f"      A cuantos goles quieres actualizar de {actualizar_gol}? : ").strip())

            buscar_jugador['goles'] = Cantidad_goles # a la llave 'goles' le añado la nueva variable
            print (f"\n El jugador {actualizar_gol} se le actualizaron los goles a {Cantidad_goles}\n")
            break

    else:
        print (f"** El jugador '{actualizar_gol}' no encontrado **")

def eliminar_jugadores(lista_jugadores):

    nombre_eliminar = input("Nombre del jugador que quieres eliminar: ").strip().lower()

    for lista_eliminar in lista_jugadores:
        
        if lista_eliminar['nombre'] == nombre_eliminar:

            print ("jugador encontrado")
            
            lista_jugadores.remove(lista_eliminar)
            
            print (f"Jugador eliminado {nombre_eliminar} con EXITO!!")
            break

    else:
        print (f"** El jugador '{nombre_eliminar}' no encontrado **")



def mostrar_top_jugadores(lista_jugadores):

    jugadores_ordenados = sorted(lista_jugadores, key=lambda x: x['goles'], reverse=True)
    
    print("Top de Jugadores:")
    
    for jugador in jugadores_ordenados:
        print(f"{jugador['nombre']} - {jugador['equipo']} - {jugador['goles']} goles")


while True:
    print ("\n -- MENU PRINCIPAL -- ")
    menu()

    try:
        opcion = int (input("\nOpcion: ").strip())
    except ValueError:
        print ("Error, vuelve a intentarlo")
        continue

    if opcion == 1:
        agregar_jugadores(lista_jugadores)
    elif opcion == 2:
        actualizar_goles(lista_jugadores)
    elif opcion == 3:
        eliminar_jugadores(lista_jugadores)
    elif opcion == 4:
        mostrar_top_jugadores(lista_jugadores)
    elif opcion == 5:
        print ("\n    Saliendo...\n")
        break
    else:
        print ("Error, vulve a intentarlo")