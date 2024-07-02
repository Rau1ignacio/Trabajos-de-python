'''
Problema: Gestión de Reservas de Citas en una Clínica

Contexto:
    En una clínica, la gestión eficiente de las reservas de citas es crucial para asegurar que los pacientes reciban atención oportuna y que los médicos puedan organizar su tiempo adecuadamente. Un sistema de gestión de reservas debe permitir a los administradores agregar nuevas citas, eliminar citas existentes, buscar citas por el nombre del paciente y guardar el inventario de citas en un archivo CSV para su posterior análisis o reporte.
Requisitos:

1.	Agregar Nuevas Citas:
    o	Permitir al usuario ingresar los detalles de la cita, incluyendo el nombre del paciente, nombre del médico, fecha y hora de la cita, y el motivo de la consulta.
    o	Guardar estos detalles en un diccionario que actúe como el inventario de citas.
2.	Eliminar Citas Existentes:
    o	Permitir al usuario eliminar una cita existente basándose en el nombre del paciente y la fecha de la cita.
3.	Buscar Citas por Nombre del Paciente:
    o	Permitir al usuario buscar todas las citas de un paciente específico basándose en el nombre del paciente.
4.	Guardar el Inventario de Citas en un Archivo CSV:
    o	Permitir al usuario guardar la lista completa de citas en un archivo CSV para su posterior uso.

Ejemplo de estructura de diccionario:

cita = { "nombre_paciente": "Juan Pérez", 
        "nombre_medico": "Dra. María López",
        "fecha": "2024-06-15", 
        "hora": "10:30",
        "motivo": "Consulta general" }
'''
import csv
#Archivo csv = inventario.csv

def menu():
    print ("\n- MENU PRINCIPAL -")
    print('''
        1- Agregar Nuevas Citas
        2- Eliminar Citas Existentes
        3- Buscar Citas por Nombre del Paciente
        4- Guardar el Inventario de Citas en un Archivo CSV
            
        5- Salir
        ''')
    
def Agregar_nuevas_citas(inventario):

    while True:

        nombre_paciente = input("Paciente: ").lower().strip()
        nombre_medico = input("Medico: ").lower().strip()
        fecha = input("Fecha (YYYY-MM-DD): ").lower().strip()
        hora = input("Hora (HH:HH): ").lower().strip()
        motivo = input("Motivo: ").lower().strip()

        print (f""" \n los datos ingresados son:
               
                nombre paciente: {nombre_paciente}
                nombre medico: {nombre_medico}
                fecha: {fecha} 
                hora:{hora} 
                motivo:{motivo}
            """)
        Validar = input ("Es correcta esta informacion? Si / No : ").strip().lower()

        if Validar == "si":

            Citas = {
                "nombre_paciente": nombre_paciente,
                "nombre_medico": nombre_medico,
                "fecha": fecha,
                "hora": hora,
                "motivo": motivo
            }
            
            inventario.append(Citas)
            print ("\n-- Cita agregada con EXITO! --")
            break
        else:
            print ("Volviendo al menu...")
            break

def eliminar_cita(inventario):

        nombre_delete  = input("Nombre del paciente para cancelar cita: ").strip().lower()
        fecha_delete = input("Fecha del cliente a cancelar cita (YYYY-MM-DD): ").strip().lower()

        for eliminar in inventario:
            while True:

                if eliminar['nombre_paciente'] == nombre_delete and eliminar['fecha'] == fecha_delete:

                    inventario.remove(eliminar)
                    print (f"-- El/la cliente '{nombre_delete}' con fecha '{fecha_delete}' ha sido eliminada con EXITO!! --n")
                    break

                else:
                    print (f"\n**   Cliente '{nombre_delete}' con fecha '{fecha_delete}' NO SE HA ENCONTRADO **")
                    print ("Intente de nuevo")
                    break

def buscar_citas_existentes(inventario):

    Nombre_A_Buscar = input("Ingrese nombre del cliente a buscar: ").strip().lower()

    for buscar_user in inventario:

        if buscar_user['nombre_paciente'] == Nombre_A_Buscar:
            
            print(f"""\nCita encontrada:
                    Nombre: {buscar_user['nombre_paciente']}
                    Médico: {buscar_user['nombre_medico']}
                    Fecha: {buscar_user['fecha']}
                    Hora: {buscar_user['hora']}
                    Motivo: {buscar_user['motivo']}
                    """)            
            break

        else:
            print ("** Error, Usuario no encontrado, intente de nuevo **")
            break

def guardar_inventario_en_csv(inventario):
    if not inventario:
        print ("No hay datos que guardar")

    else:

        with open ('inventario_citas.csv', 'w') as in_citas:

            escribir = csv.writer(in_citas)

            escribir.writerow(inventario)

        print ("\n  Archivo guardado con EXITO!!")

        while True:

            opcion_csv = input("\nQuieres ver el archivo guardado? Si / No: ").strip().lower()

            if opcion_csv == "si":

                with open ('inventario_citas.csv', 'r') as in_citas:
                    leer_csv = csv.reader(in_citas)
                    for leer in leer_csv:
                        #for indentado, mostrar in enumerate(inventario, start=1)
                        print ()
                        print (leer)
                        break
            else:
                print ("\n Volviendo al menu principal...")
                break

inventario = []

while True:
    menu()
    try:

        opcion = int (input("Opcion: ").strip())

    except ValueError:
        print ("** Error, recuerda colocar una opcion **")
        continue


    if opcion == 1:
        Agregar_nuevas_citas(inventario)
    elif opcion == 2:
        eliminar_cita(inventario)
    elif opcion == 3:
        buscar_citas_existentes(inventario)
    elif opcion == 4:
        guardar_inventario_en_csv(inventario)

    elif opcion == 5:
        print ("\n      Saliendo del sistema...\n")
        break
    else:
        print("Opcion incorrecta")