import csv

def menu():
    print ('''
           1.- Comprar boleto
           2.- Confirmar boleto
           3.- Eliminar boleto
           4.- Exportar registro

           5.- Salir           
''')

def comprar_boleto(tickets_lista):
    # - o	Permitir registrar un nuevo boleto solicitando la información mencionada (nombre del comprador, 
    # - hora de compra, correo electrónico, estado del boleto por defecto "pendiente" y destino válido).

    while True: # inicio un bucle para las variables

        try:

            nombre_del_comprador = input("\nNombre del comprador: ").strip().lower() #se introduce el nombre
            hora_compra = input("Hora de compra: ").strip().lower() ### podria hacer una validacion que ponga hora / pero perderia mucho tiempo en el examen
            Correo = input("Correo electronico: ").strip().lower()### podria hacer una validacion que ponga fechas
            estado_boleto = "pendiente".strip().lower() #El valor inicial siempre sera pendiente    

            while True:# con este bucle hago mediante una validacion que usuario ponga una de las 4 opciones de ciudades

                destino_boleto = input("Destino del boleto (Viña del Mar, Valparaíso, Concón, Santiago) : ").strip().lower()

                if destino_boleto in [ "viña del mar", "valparaiso", "concon", "santiago"]:
                    print (f"   Excelente tu destino '{destino_boleto}' ha sido guardado")
                    break
                else:
                    print ("\n** Error, opcion incorrecta, eliga una de estas opciones: \nviña del mar \nvalparaiso \nconcon \nsantiago \n")

            print ("Estos son los datos ingresado:")

            print (f"""
                    Nombre del comprador: {nombre_del_comprador}
                    Hora de compra: {hora_compra}
                    Correo electronico: {Correo}
                    Estado de boleto: {estado_boleto}
                    Destino del boleto: {destino_boleto}
                    """) # Le muestro al cliente los datos que puso

            respuesta = input ("Estas seguro que son los datos correctos? SI / NO : ").strip().lower() # Le pregunto al cliente si los datos mostrados anteriormente estan correctos
            if respuesta == "si":

                compradores = {
                    'Nombre del comprador': nombre_del_comprador,
                    'Hora de compra': hora_compra,
                    'Correo electronico': Correo,
                    'Estado del boleto': estado_boleto,
                    'Destino del boleto': destino_boleto
                }
                tickets_lista.append(compradores) #Lo agrego a la lista de tickets

                print ("Excelente, Datos almacenados con EXITO!") # Con esto compuebo que todos los valores de almacenaron en el diccionario
                break

            elif respuesta == "no":
                print ("\n ** Reiniciando el sistema para que puedas volver a ingresar los datos. ** \n")
                break

        except ValueError:
            print ("Coloque el valor correcto")

def confirmar_boleto(tickets_lista):
# - Permitir buscar un boleto por el correo electrónico registrado y cambiar su estado de "pendiente" a "confirmado".
    try:
        correo_confirmado = input("Coloque su correo electronico: ").lower().strip()
        for confirmar in tickets_lista: # Recorro los tickets registrados
            if confirmar['Correo electronico'] == correo_confirmado:

                print ("\nBoleto encontrado\n")
                print (f"Nombre del comprador : {confirmar['Nombre del comprador']}")
                print (f"Destino : {confirmar['Destino del boleto']}")
                print (f"Hora de compra : {confirmar['Hora de compra']}")
                print (f"Estado del boleto: {confirmar['Estado del boleto']}")

                while True: # Hago un bucle para verificar si quiere o no confirmar los boletos.

                    respuesta = input("\n¿Desea confirmar este boleto? si / no: ").lower().strip()
                    
                    if respuesta == 'si':
                        confirmar['Estado del boleto'] = 'confirmado'
                        print("\nBoleto confirmado:")
                        print(f'''
                            Nombre del comprador: {confirmar['Nombre del comprador']}
                            Destino: {confirmar['Destino del boleto']}
                            Hora de compra: {confirmar['Hora de compra']}
                            Estado: {confirmar['Estado del boleto']}''')
                        break

                    elif respuesta == 'no':
                        print("El boleto no ha sido confirmado.")
                        break

                    else:
                        print("Respuesta inválida. Por favor, responda 'si' o 'no'.")
            else:
                print (f"Boleto {correo_confirmado} no encontrado!!")

    except ValueError:
        print (f"Boleto {correo_confirmado} no encontrado!!, vuelve a intentarlo")


def eliminar_boleto(tickets_lista):

    try:
        correo_eliminar = input("Coloque su correo electronico: ")

        for delete in tickets_lista: # recorro los tickets registrados
            if delete ['Correo electronico'] == correo_eliminar:

                print ("Boleto encontrado\n")
                print (f"Nombre del comprador : {delete['Nombre del comprador']}")
                print (f"Destino : {delete['Destino del boleto']}")
                print (f"Hora de compra : {delete['Hora de compra']}")
                print (f"Estado del boleto: {delete['Estado del boleto']}")
                respuesta = input ("Desea eliminar este boleto: si / no : ").lower().strip() # se puede hacer un bucle para corroborar las respuestas
                if respuesta == 'si':
                    tickets_lista.remove(delete) ### ver si este codigo esta bien o si se puede hacer mejor
                    print ("Boleto elminado")
            else:
                print (f"Boleto con correo '{correo_eliminar}' no encontrado, vea si lo ha digitado mal")
    except Exception as e:
        print ("Error")


def exportar_registro(tickets_lista): #se debe exportar solo los confirmados!!

    print("Se exportara la siguiente data: ")

    for datos in tickets_lista:
        if tickets_lista['Estado del boleto'] == 'confirmado':

            print (f'''
                Nombre del comprador : {tickets_lista['Nombre del comprador']}
                Destino : {tickets_lista['Destino del boleto']}
                Hora de compra : {tickets_lista['Hora de compra']}
                Estado : {tickets_lista['Estado del boleto']}
                ''')
            respuesta =  input("Desea exportar? si / no : ").strip().lower()
            if respuesta == 'si':
                with open('datos_boletos.csv', 'w') as boletos:
                    escritor = csv.writer(boletos)
                    escritor.writerow('Nombre del comprador','Hora de compra','Correo electronico','Estado del boleto','Destino del boleto')
                    
                    for data in boletos:
                        escritor.writerow([data])

tickets_lista = []

while True:
    menu()
    try:

        opcion = int (input("Opcion: ").strip())

        if opcion == 1:
            comprar_boleto(tickets_lista)
        elif opcion == 2:
            confirmar_boleto(tickets_lista)
        elif opcion == 3:
            eliminar_boleto(tickets_lista)
        elif opcion == 4:
            exportar_registro(tickets_lista)
        elif opcion == 5:
            print ("Saliendo del sistema...")
            break
        else:
            print ("Opcion incorrecta.")

    except ValueError:
        print ("** Error, Opcion incorrecta **")

