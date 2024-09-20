# find_product.py

import random
liste = []
r= -1
product= 1
while len(liste)<5:
    r = random.randint(1,5)
    liste.append(r)
    product = product * r
print("this is the list of random numbers?n", liste)
print("the producct is: ", product)
