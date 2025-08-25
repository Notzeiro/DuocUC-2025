import time, os

def cambio_hora(variable, texto):
    while True:
        variable=input(f"Ingrese {texto}: ")
        if not variable.isdigit():
            print("Solo numeros, por favor intente de nuevo.")
            continue
        variable=int(variable)
        return variable

def ult_vehiculo_y_total(dictionary):
    print(f"Ultimo vehiculo ingresado: {dictionary["ultimo_ingreso"]}")
    print(f"Total de vehiculos en el garage:{dictionary["total_vehiculos"]}")
    
def ingreso_vehiculos(dictionary):
    
    os.system("cls")
    while True:# INGRESO MARCA
        marca=input("Ingrese la marca del vehiculo: ")
        if marca.isalpha():
            print(f"Es la marca {marca} correcta? \n1.-Si, continuar\n2.-No, modificar\n") 
            q=input("Seleccione una opcion: ")
            match q:
                case "1":
                    while True:# INGRESO MODELO ----------------------------------------------------------------------------------------------------------
                        modelo=input("Ingrese el modelo del vehiculo: ") 
                        if modelo.isalpha():
                            print(f"Es la el modelo {modelo} correcta? \n1.-Si, continuar\n2.-No, modificar\n")
                            q=input("Seleccione una opcion: ")
                            match q:
                                case "1":
                                    while True:# INGRESO AÑO ----------------------------------------------------------------------------------------------------------
                                        año=(input("Ingrese el año del vehiculo: ")) 
                                        if año.isdigit():
                                            año=int(año)
                                        else:
                                            print("El año debe ser un numero, por favor intente de nuevo.")
                                            continue
                                        print(f"Es el año {año} correcto? \n1.-Si, continuar\n2.-No, modificar\n")
                                        q=input("Seleccione una opcion: ")
                                        match q:
                                            case "1":
                                                while True: # INGRESO PATENTE ----------------------------------------------------------------------------------------------------------
                                                    patente=input("Ingrese la patente del vehiculo: ").lower()
                                                    letras=0
                                                    numeros=0
                                                    for char in patente:
                                                        if char.isalpha():
                                                            letras+=1
                                                        elif char.isdigit():
                                                            numeros+=1
                                                    if letras==4 and numeros==2:
                                                        print (f"""Es la patente {patente} correcta? \n1.-Si, continuar\n2.-No, modificar\n""")
                                                        q=input("Seleccione una opcion: ")
                                                        match q:
                                                            case "1":
                                                                while True: # INGRESO TIPO DE VEHICULO ----------------------------------------------------------------------------------------------------------
                                                                    tipo=(input("Ingrese el tipo de vehiculo (C para camioneta, S para sedan, M para Moto): ")).upper()
                                                                    if tipo in ["C", "S", "M"]:
                                                                        print(f"""Es el tipo {tipo} correcto? \n1.-Si, continuar\n2.-No, modificar\n""")
                                                                        q=input("Seleccione una opcion: ")
                                                                        match q:
                                                                            case "1":
                                                                                new_vehicle = {"marca":marca , 
                                                                                               "modelo": modelo ,
                                                                                                 "año": año ,
                                                                                                "patente": patente ,
                                                                                                 "tipo": tipo,
                                                                                                 "hora_ingreso": time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime()),
                                                                                                 "hora_salida": None}
                                                                                vehicles_id = list(dictionary["vehiculos"].keys())
                                                                                dictionary["vehiculos"][vehicles_id[-1]+1] = new_vehicle
                                                                                dictionary["ultimo_ingreso"] =new_vehicle
                                                                                dictionary["total_vehiculos"] += 1
                                                                                print(f"Vehiculo ingresado correctamente: {new_vehicle}")
                                                                                input("Presione cualquier tecla para continuar...  ")
                                                                                return
                                                                            case "2":
                                                                                continue

                                                                            case _:
                                                                                print(f"""Por favor ingrese una opcion valida "{q}" no es una opcion""")
                                                                                continue
                                                                            
                                                            case "2":
                                                                continue
                                                            case _:
                                                                print(f"""Por favor ingrese una opcion valida "{q}" no es una opcion""")
                                                                continue
                                                    else:
                                                        print("La patente debe tener 4 letras y 2 numeros, por favor intente de nuevo.")
                                                        continue        

                                            case "2":
                                                continue
                                            case _:
                                                print(f"""Por favor ingrese una opcion valida "{q}" no es una opcion""")
                                                continue
        
                                case "2":
                                    continue
                                case _:
                                    print(f"""Por favor ingrese una opcion valida "{q}" no es una opcion""")
                                    continue
                        else:
                            print("El modelo debe contener solo letras, por favor intente de nuevo.")
                            continue
                    

                case "2":
                    continue
                case _:
                    print(f"""Por favor ingrese una opcion valida "{q}" no es una opcion""")
                    continue

        else:
            print("La marca debe contener solo letras, por favor intente de nuevo.")
            continue

def mostrar_vehiculos(dictionary):
    for key, vehicle in dictionary["vehiculos"].items():
                print (key , ":" ,vehicle)

def actualizar_vehiculos(dictionary):
    mostrar_vehiculos(dictionary)
    print("Seleccione el ID del vehiculo que desea actualizar: ")
    id_actualizar= input("ID del vehiculo: ")
    print(dictionary["vehiculos"][int(id_actualizar)])
    print("""
          1.- Actualizar marca
          2.- Actualizar modelo
          3.- Actualizar año
          4.- Actualizar patente
          5.- Actualizar tipo
          6.- Actualizar hora de ingreso
          7.- Volver al menu principal
          """)
    q= input("Seleccione una opcion: ")
    match q:
        case "1":
            while True: # INGRESO MARCA NUEVA
                marca=input("Ingrese la marca del vehiculo: ")
                if marca.isalpha():
                    print(f"Es la marca {marca} correcta? \n1.-Si, continuar\n2.-No, modificar\n") 
                    q=input("Seleccione una opcion: ")
                    match q:
                        case "1":
                            dictionary["vehiculos"][int(id_actualizar)]["marca"] = marca
                            print(f"Marca actualizada a {marca}")
                            input("Presione cualquier tecla para continuar...  ")
                            return
                        case "2":
                            continue
                        case _:
                            print(f"""Por favor ingrese una opcion valida "{q}" no es una opcion""")
                            continue
                else:
                    print("La marca debe contener solo letras, por favor intente de nuevo.")
                    continue

        case "2":
            while True: # INGRESO modelo NUEVo
                modelo=input("Ingrese el modelo del vehiculo: ")
                if modelo.isalpha():
                    print(f"Es el modelo {modelo} correcto? \n1.-Si, continuar\n2.-No, modificar\n") 
                    q=input("Seleccione una opcion: ")
                    match q:
                        case "1":
                            dictionary["vehiculos"][int(id_actualizar)]["modelo"] = modelo
                            print(f"Modelo actualizado a {modelo}")
                            input("Presione cualquier tecla para continuar...  ")
                            return
                        case "2":
                            continue
                        case _:
                            print(f"""Por favor ingrese una opcion valida "{q}" no es una opcion""")
                            continue
                else:
                    print("El modelo debe contener solo letras, por favor intente de nuevo.")
                    continue
        case "3":
            while True:# INGRESO AÑO ----------------------------------------------------------------------------------------------------------
                    año=(input("Ingrese el año del vehiculo: ")) 
                    if año.isdigit():
                        año=int(año)
                    else:
                        print("El año debe ser un numero, por favor intente de nuevo.")
                        continue
                    print(f"Es el año {año} correcto? \n1.-Si, continuar\n2.-No, modificar\n")
                    q=input("Seleccione una opcion: ")
                    match q:
                        case "1":
                            dictionary["vehiculos"][int(id_actualizar)]["año"] = año
                            print(f"año actualizado a {año}")
                            input("Presione cualquier tecla para continuar...  ")
                            return
                        case "2":
                            continue
                        case _:
                            print(f"""Por favor ingrese una opcion valida "{q}" no es una opcion""")
                            continue
        case "4":
            while True: # INGRESO PATENTE ----------------------------------------------------------------------------------------------------------
                patente=input("Ingrese la patente del vehiculo: ").lower()
                letras=0
                numeros=0
                for char in patente:
                    if char.isalpha():
                        letras+=1
                    elif char.isdigit():
                        numeros+=1
                if letras==4 and numeros==2:
                    print (f"""Es la patente {patente} correcta? \n1.-Si, continuar\n2.-No, modificar\n""")
                    q=input("Seleccione una opcion: ")
                    match q:
                        case "1":
                            dictionary["vehiculos"][int(id_actualizar)]["patente"] = patente
                            print(f"patente actualizada a {patente}")
                            input("Presione cualquier tecla para continuar...  ")
                            return
                        case "2":
                            continue
                        case _:
                            print(f"""Por favor ingrese una opcion valida "{q}" no es una opcion""")
                            continue

        case "5":
            while True: # INGRESO TIPO DE VEHICULO ----------------------------------------------------------------------------------------------------------
                tipo=(input("Ingrese el tipo de vehiculo (C para camioneta, S para sedan, M para Moto): ")).upper()
                if tipo in ["C", "S", "M"]:
                    print(f"""Es el tipo {tipo} correcto? \n1.-Si, continuar\n2.-No, modificar\n""")
                    q=input("Seleccione una opcion: ")
                    match q:
                        case "1":
                            dictionary["vehiculos"][int(id_actualizar)]["tipo"] = tipo
                            print(f"Tipo de vehiculo actualizado a {tipo}")
                            input("Presione cualquier tecla para continuar...  ")
                            return
                        case "2":
                            continue
                        case _:
                            print(f"""Por favor ingrese una opcion valida "{q}" no es una opcion""")
                            continue
        case "6":
            año=0
            mes=0
            dia=0
            hora=0
            minuto=0

            año=cambio_hora(año, "año")
            mes=cambio_hora(mes , "mes")
            dia=cambio_hora(dia, "dia")
            hora=cambio_hora(hora, "hora")
            minuto=cambio_hora(minuto, "minuto")

            
            hora_ingreso=f"{año}-{mes}-{dia} {hora}:{minuto}:00"
            dictionary["vehiculos"][int(id_actualizar)]["hora_ingreso"] = hora_ingreso
            print(f"Hora de ingreso actualizada a {hora_ingreso}")


        case "7":
            print("Adios")
            return
        case _:
            print(f"""Por favor ingrese una opcion valida "{q}" no es una opcion""")
            input("Presione cualquier tecla para continuar..  ")

def marcar_salida(dictionary):
    print("Seleccione el ID del vehiculo que desea marcar como salido: ")
    id_salida= input("ID del vehiculo: ")
    hora_salida = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
    garage["vehiculos"][int(id_salida)]["hora_salida"] = hora_salida
    print(f"Vehiculo con ID {id_salida} marcado como salido a las {hora_salida}")
    garage["total_vehiculos"] -= 1

garage={
    "vehiculos": 
    {
    1:{"marca": "Ford" , "modelo":"Mustang GT" , "año": 2023 , "patente": "beat69" , "tipo": "S", 
       "hora_ingreso": ("2025-6-23 03:08:34" ), "hora_salida": None} ,
    2:{"marca": "Porshe" , "modelo":"Cayman" , "año": 2025 , "patente": "dadd77" , "tipo": "S", 
       "hora_ingreso": ("2025-6-23 04:07:32" ), "hora_salida": None} ,
    3:{"marca": "Toyota" , "modelo":"Hilux" , "año": 2021 , "patente": "elp3p3" , "tipo": "C", 
       "hora_ingreso": ("1999-6-23 01:06:23" ), "hora_salida": None}
                  },
    "ultimo_ingreso": None,
    "total_vehiculos": 0
}



while True:
    os.system("cls")
    print("""
    1.- Ingresar vehiculo
    2.- Mostrar vehiculos
    3.- Actualizar vehiculos
    4.- Marcar salida de vehiculo con hora
    5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
    6.- Salir
    """)
    
    op=input("Elija una opcion: ")
    
    match op:
        case "1":
            print("Opcion 1 seleccionada")
            ingreso_vehiculos(garage)
            input("Presione cualquier tecla para continuar...  ")
        case "2":
            print("Opcion 2 seleccionada")
            mostrar_vehiculos(garage)
            input("Presione cualquier tecla para continuar...  ")
        case "3":
            print("Opcion 3 seleccionada")
            actualizar_vehiculos(garage)
            input("Presione cualquier tecla para continuar...  ")
        case "4":
            print("Opcion 4 seleccionada")
            mostrar_vehiculos(garage)
            marcar_salida(garage)   
            input("Presione cualquier tecla para continuar...  ")
        case "5":
            print("Opcion 5 seleccionada")
            ult_vehiculo_y_total(garage)
            input("Presione cualquier tecla para continuar...  ")
        case "6":
            print("Adios")
            break
        case _:
            print(f"""Por favor ingrese una opcion valida "{op}" no es una opcion""")
            input("Presione cualquier tecla para continuar..  ")