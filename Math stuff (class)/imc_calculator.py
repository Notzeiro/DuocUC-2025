def calcular_imc(peso , altura):#peso en kg y altura en metros
    global imc
    imc = (peso/(altura*altura))
    imc = round (imc , 2)
    return imc

def nivel_de_peso(imc):
    global imc_rango
    if imc<18.5:
        imc_rango="Bajo peso"
        return imc_rango
    elif imc>18.5 and imc<25:
        imc_rango="Peso normal"
        return imc_rango
    elif imc>25 and imc<30:
        imc_rango="Sobrepeso"
        return imc_rango
    elif imc>30:
        imc_rango="Obesidad"
        return imc_rango
    

peso=float(input("ingrese su peso en kg: "))
altura=float(input("ingrese su altura en metros: "))
calcular_imc(peso, altura)
nivel_de_peso(imc)
print (f"Segun el valor de su imc que es {imc} usted tiene: {imc_rango}")
