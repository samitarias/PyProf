my_list = [0,1,4,7,9,10]

my_second_list = [x*2 for x in my_list] #List comprehension
my_second_gen = (x*2 for x in my_list) #Generator expression

import time

impares = [2*i+1 for i in range(100)] # Crea la lista en memoria de numeros impares
impares_gen = (2*i+1 for i in range(100)) #Itera sobre los numeros impares 


print(impares)
print(type(impares))


print(impares_gen)
print(type(impares_gen))

for i in impares_gen:
    print(i)
    time.sleep(1)