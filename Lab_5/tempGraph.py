#Patrick Roscio
#Lab_5: tempGraph.py
#Description: using matplotlib and random, a list named "time" is created with 12 hours. The three cities are named and a random number generator creates a list of 12 random temperatures for each city
#   The cities' temperatures ar then plooted and labeled accordingly. 

import matplotlib.pyplot as plt
import random

time = []
creation = 12
for i in range(creation): 
    time.append(i+1)

city_1 = "New York"
city_2 = "Phillidelphia"
city_3 = "Boston"

city_1temp = []
city_2temp = []
city_3temp = []


for i in range(creation):
    random_temp_1 = random.randrange(10,31)
    city_1temp.append(random_temp_1)
    random_temp_2 = random.randrange(10,31)
    city_2temp.append(random_temp_2)
    random_temp_3 = random.randrange(10,31)
    city_3temp.append(random_temp_3)

plt.plot(time,city_1temp, label = city_1)
plt.plot(time,city_2temp, label = city_2)
plt.plot(time,city_3temp, label = city_3)

plt.xlabel("Time")
plt.ylabel("Temperatures")
plt.title("City temperatures over time: ")

plt.legend()

plt.show()

exit()
