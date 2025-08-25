import matplotlib.pyplot as plt
import numpy as np

def g(x):
    return 600000 + 45000 * x

x_values=np.linspace( 1 , 10 , 10)
y_values=g(x_values)

plt.ticklabel_format(style='plain', axis='y') #esto desactiva la notacion cientifica

plt.xlabel("Años")
plt.ylabel("Sueldo")
plt.plot( x_values , y_values )

print(f"El resultado al año 8 es: {g(8)}")
print(f"Si alguien lleva 12 años en la empresa su sueldo es de: {g(12)}")

#a eje X seria la variable de los años, el tiempo en otras palabras(variable independiente)
#b eje Y seria la variable de el sueldo, la platita (variable dependiente)
#c X seria 8 y Y seria 960000 , significa que en 8 años ganara 960.000$
#d la preimagen seria los años dentro de la funcon y la imagen seria el sueldo final 
#e Recibira 1.140.000$