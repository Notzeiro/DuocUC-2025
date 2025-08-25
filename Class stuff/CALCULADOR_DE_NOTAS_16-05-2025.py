import pyfiglet
import os
import time
welcome=pyfiglet.figlet_format("Calculadora de notas")
alumnos=[]


def limpiar_terminal():
    os.system("cls")

def busqueda_alumno():
    global alumnos
    try:
        
        menuBusqueda=pyfiglet.figlet_format("Menu de busqueda" , font="small")
        while True:
            limpiar_terminal()
            op=int(input(f"{menuBusqueda}\n1.-Buscar por nombre\n2.-Buscar por rut\n3.-Volver al menu principal\n"))
            match op:
                case 1:
                    busqueda=(input("Ingrese nombre del alumno:\n"))
                    encontrado=False
                    for alumno in alumnos:
                        if busqueda.lower() == alumno["nombre"].lower() :
                            encontrado=True
                            limpiar_terminal()
                            print("Alumno encontrado\n")
                            print(f"Nombre={alumno["nombre"]}\n-----------------------------")
                            print(f"Notas={alumno["notas"]}")
                            print(f"Promedio={alumno["promedio"]}")
                            gogogogo=input("\n\nPresione cualquier tecla para volver atras\n")
                            break
                    if encontrado==False:
                        limpiar_terminal()
                        print("Alumno no encontrado :[")
                        gogogogo=input("\n\nPresione cualquier tecla para volver atras\n")

                case 2:
                    encontrado=False
                    bus=str(input("Ingrese el rut del alumno a buscar\n"))
                    for alumno in alumnos:
                        if bus == alumno["rut"]:
                            encontrado=True
                            limpiar_terminal()
                            print("Alumno encontrado\n")
                            print(f"Nombre={alumno["nombre"]}\n-----------------------------")
                            print(f"Notas={alumno["notas"]}")
                            print(f"Promedio={alumno["promedio"]}")
                            gogogogo=input("\n\nPresione cualquier tecla para volver atras\n")
                            break
                    if encontrado==False:
                        limpiar_terminal()
                        print("Alumno no encontrado :[")
                        gogogogo=input("\n\nPresione cualquier tecla para volver atras\n")
                case 3:
                    break
                case _:

                    print("Seleccion invalida, por favor intente nuevamente")

        
    except Exception as e:
            limpiar_terminal()
            print(f"Error inesperado {e}")
            fff=input("presione cualquier tecla para continuar...")

def ingreso_nombre():
    global nombre
    try:
            ingreso=False
            while True:
                nombre=str(input(f"Nombre completo del alumno:\n")).strip()
                if all(c.isalpha() or c.isspace() or c in "áéíóúÁÉÍÓÚñÑ" for c in nombre):
                    nombre=nombre.title()
                    while True:
                        limpiar_terminal()
                        g=int(input(f"nombre ingresado:{nombre}\nEl nombre es correcto?\n1.-Si\n2.-No\n"))
                        if g==1:
                            limpiar_terminal()
                            print("Ingresado correctamente")
                            ingreso = True
                            return nombre
                        elif g==2:
                            break
                        else:
                            print("seleccion invalida")
                else:
                    print("Error: El nombre solo debe contener letras y espacios")
   
    except Exception as e:
            limpiar_terminal()
            print(f"Error inesperado {e}")
            fff=input("presione cualquier tecla para continuar...")

def ingreso_alumnos():
    global alumnos
    try:
        
            while True:
                limpiar_terminal()

                ingresoAlumnosMenu=pyfiglet.figlet_format("Ingreso de alumnos" , font="small")
                seleccion=int(input(f"{ingresoAlumnosMenu}\n1.-Ingresar alumno\n2.-Volver al menu principal\n"))
                match seleccion:
                    case 1:
                        nombre=ingreso_nombre()

                        rut=input("Ingrese el rut para el estudiante (con puntos y guion):\n")
                    
                        notasb=int(input(f"Ingrese la cantidad de notas del alumno {nombre}:\n"))
                            
                        notaslista=[]

                        for d in range(notasb):
                            #aca se ingresan las notas

                            notas=(float(input(f"Ingrese la nota n°{d+1} de {nombre}:\n")))

                            notaslista.append(notas)
                        alumno={"nombre":nombre ,            
                                "notas" : notaslista ,
                                "rut" : rut ,
                                "promedio": sum( notaslista ) / len( notaslista )
                                }

                        alumnos.append(alumno)

                    case 2:
                        break

                    case _:
                        f=input("Por favor ingrese una opcion valida... presione cualquier tecla para continuar")   
    
    except Exception as e:
        limpiar_terminal()
        print(f"Error inesperado {e}")
        fff=input("presione cualquier tecla para continuar...")
def menu():
    menuu=pyfiglet.figlet_format("MENU PRINCIPAL" , font="small" )
    while True:
        try:
            limpiar_terminal()
            op=(int(input(f"{menuu}\n1.-Busqueda de alumno\n2.-Ingreso alumnos\n3.-Salir\n"))) 
            match op:
                case 1:
                    limpiar_terminal()
                    busqueda_alumno() 
                case 2:
                    limpiar_terminal()
                    ingreso_alumnos()
                case 3:
                    limpiar_terminal()
                    adios=pyfiglet.figlet_format("Adios" , font="small")
                    print(f"{adios}\n:]")
                    break
        except Exception as e:
            limpiar_terminal()
            print(f"Error inesperado {e}")
            fff=input("presione cualquier tecla para continuar...")



print(welcome)
print("By:NotZeiro")
time.sleep(2)
limpiar_terminal()
menu()


