import os, time, pyfiglet, random

palabras={"comida":["manzana","pera","platano","sandia","naranja","uva","frutilla","kiwi","mango","cereza"],
          "animales":["perro","gato","elefante","jirafa","leon","tigre","delfin","ballena","cocodrilo","tortuga"],
          "paises":["argentina","brasil","chile","colombia","mexico","peru","venezuela","ecuador","bolivia","uruguay","estados unidos"],
          "colores":["rojo","azul","verde","amarillo","naranja","purpura","rosa","celeste" ] ,
          "plantas":["rosa","lirio","tulipan","girasol","clavel","margarita","orquidea","jazmin","azalea","hibisco"],
          "personajes de anime": ["satorugojo", "naruto","sasuke","luffy","tanjiro","inosuke","itadori","sukuna","lightyagami","ryuk","misaamane","eren","mikasa","armin"],
          "marcas":["nike","adidas","ferrari","lenovo","hp","apple","samsung","kendall","xiaomi","dc","lg","hym","forever21","paris"],
          "ciudades":["paris","santiago","buenos aires","mendoza","temuco","frutillar","punta arenas","valparaiso","viña del mar","londres","nueva york","asuncion","lima","medellin","arica","puerto montt","puerto varas","llanquihue"]}

palabra_magica_dic={}

intentos=[]
palabra_completa=False

def comprobar_victoria(dic):
    for value in dic.values():
        if value["encontrado"]==False:
            return False
    return True

def elegir_dificultad():
    global palabra_a_adivinar, categoria
    os.system('cls')
    while True:
        print(""" 
                1.-Facil
                2.-Medio
                3.-Dificil
        
                """)
        dificultad=input('Ingrese dificultad: ')
        match dificultad:
            case '1':
                while True:
                    os.system('cls')
                    op=input('Desea elegir topico? \n1.-Si\n2.-No\n')
                    match op:
                        case '1':
                            palabra_a_adivinar=random.choice(palabras[elegir_topico(palabras)])
                            return 10
                
                        case '2':
                            categoria=random.choice(list(palabras.keys()))
                            palabra_a_adivinar=random.choice(palabras[categoria])
                            return 10
                        case _:
                            print('opcion invalida')
                            time.sleep(1)
                            continue
            case '2':
                categoria=random.choice(list(palabras.keys()))
                palabra_a_adivinar=random.choice(palabras[categoria])
                return 5
            case '3':
                categoria=random.choice(list(palabras.keys()))
                palabra_a_adivinar=random.choice(palabras[categoria])
                return 3
            case _:
                ('opcion invalida')
                continue

def elegir_topico(dic):
    topicos=list(dic.keys())
    while True:
        for index, topic in enumerate(topicos):
            print(f"{index+1}.- {topic}")
        numero_seleccion=input("Ingrese eleccion: ")
        if numero_seleccion.isdigit():
            numero_seleccion=int(numero_seleccion)-1
            if numero_seleccion<len(topicos) and numero_seleccion>-1:
                topico_elegido=topicos[numero_seleccion]
                print(f"Topico elegido {topico_elegido}")
                time.sleep(1.5)
                return (topico_elegido)
            else:
                print("Seleccion invalida")
                continue
        else:
            print("Ingrese numero valido")
            continue

def mostrar_avance_juego(dic):
        for value in dic.values():
            if value["encontrado"]==True:
                print(f' {value["letra"]} ' , end=" ")
            else:
                print("_" , end=" ")

def juego(palabra_magica):
    global vidas_iniciales, palabra_completa
    while True:
        os.system("cls")

        if vidas_iniciales<=0:
            print("Perdiste!")
            print(f"La palabra era {palabra_magica}")
            break

        if comprobar_victoria(palabra_magica_dic):
            os.system("cls")
            print(pyfiglet.figlet_format("VICTORIA"))
            time.sleep(2)
            break
        else:
            print(f'intentos={intentos}')
            print(f'vidas={vidas_iniciales}')
            mostrar_avance_juego(palabra_magica_dic)
            letra=pedir_letra()
            if not palabra_completa:
                actualizar_dic(palabra_magica_dic, letra)
                os.system("cls")
            elif palabra_completa:
                if palabra_a_adivinar.strip().lower()==letra:
                    os.system("cls")
                    print(pyfiglet.figlet_format("VICTORIA"))
                    time.sleep(2)
                    break
                elif letra=="hint":
                    continue
                else:
                    vidas_iniciales-=1
    
def pedir_letra():
    global palabra_completa
    palabra_completa=False
    pista_usada=False
    while True:
        if vidas_iniciales==2 and pista_usada==False:
            print("")
            print("""puedes escribir "hint" para una pista """)
            print("")
        letra_usuario=input("Ingrese letra o palabra completa: ")
        
        if letra_usuario in intentos:
            print(f'Ya ingresaste {letra_usuario}!')
            time.sleep(1)
            continue
        if letra_usuario=="hint":
            pista_usada=True
            print(f"La categoria de tu palabra es:")
            time.sleep(1)
            print("." , end="" , flush=True)
            time.sleep(1)
            print("." , end="", flush=True)
            time.sleep(1)
            print("." , end=" ", flush=True)
            time.sleep(1)
            print(categoria)
            time.sleep(3)
            
            
                
            
        if len(letra_usuario)==0:
            continue
        

        if letra_usuario.isalpha():
            if len(letra_usuario)>1:
                letra_usuario=letra_usuario.lower().strip()
                intentos.append(letra_usuario)
                palabra_completa=True
                return letra_usuario
            
            elif len(letra_usuario)==1:
                letra_usuario=letra_usuario.lower().strip()
                intentos.append(letra_usuario)
                return letra_usuario
        else:
            os.system('cls')
            print("Solo letras permitidas")
            continue
    
def crear_diccionario(palabra_magica):
    global palabra_magica_dic
    palabra_magica_dic={}
    palabra_magica=palabra_magica.strip().lower()
    for index , letter in enumerate(palabra_magica):
        palabra_magica_dic[index]={"letra":letter, "encontrado":False}
    
def actualizar_dic(dic, letra):
    global vidas_iniciales
    acierto=False

    for value in dic.values():
        if letra==value["letra"]:
            acierto=True
            value["encontrado"]=True
    
    if acierto==False:
        vidas_iniciales-=1

while True:
    os.system("cls")

    print(pyfiglet.figlet_format('El ahorcado'))
    print("""
    1.- Jugar
    2.- Salir
          
    By:notzeiro
    """)
    
    op=input("Elija una opcion: ")
    
    match op:
        case "1":
            print("Opcion 1 seleccionada")
            intentos.clear()
            palabra_magica_dic.clear()
            palabra_a_adivinar=None
            time.sleep(1)
            os.system("cls")
            vidas_iniciales=elegir_dificultad()
            
            crear_diccionario(palabra_a_adivinar)
            juego(palabra_a_adivinar)
            input("Presione cualquier tecla para continuar...  ")
        
        case "2":
            print("Adios")
            break
        case _:
            print(f"""Por favor ingrese una opcion valida "{op}" no es una opcion""")
            input("Presione cualquier tecla para continuar..  ")