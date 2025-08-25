import matplotlib.pyplot as plt
from random import randint

x_values=[]
y_values=[]

for month in range (1,13):
    x_values.append(month)
print(x_values)

for month in range (1,13):
    random_number=randint(1,5)*randint(1,5)
    y_values.append(random_number)
print(y_values)


plt.title("Muscle gain in time")
plt.xlabel("Months")
plt.ylabel("Times the user went to the gym")
plt.plot(x_values , y_values )

plt.show()

