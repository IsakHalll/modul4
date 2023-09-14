import os
os.system('cls')
import math
"""
min_length=1.4
length = float(input("din längd i meter: "))
if length >= min_length:
    print ("du får åka")
elif length < min_length:
    print ("Kortis du får inte åka")


print ("välkommen")
name = str(input("Namn: "))
while True:
    
    try:
        age = int(input("Ålder: "))
        break
    except:
        print("skriv i heltal")

while True:
    try:
        a2=float(input("din längd i meter:")) 
        b2=float(input("din vikt:"))
        print(b2/(a2**2))
        break
    except:
        print("skriv i decimaltal")


while True:
    try:
        radius = float(input("cirkelns radie: "))
        print(radius*radius*math.pi)
        break
    except:
        print("skriv i decimaltal")
        continue
    


op = int(input("vilket räknesätt (1 = + 2 = - 3 = * 4 = /)"))
x = float(input("x: "))
y = float(input("y: "))

if op == 1:
    print(x + y)
elif op == 2:
    print(x - y)
elif op == 3:
    print(x / y)
elif op == 4:
    print(x * y)
"""

import random



x=int(input("hur många tärningar?: "))
        
for x in range(1,x+1):
    dice = random.randint(1,6)
    print(dice)
