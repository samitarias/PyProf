#Nested functions -> Son funciones dentro de otras funciones.
#Clousures -> Se da cuando una variable que está en un scope superior es recordada por una función que está en un scope inferior, aunque el scope superior sea eliminado.
#Ejemplo:
#Nested functions -> Son funciones dentro de otras funciones.
#Clousures -> Se da cuando una variable que está en un scope superior es recordada por una función que está en un scope inferior, aunque el scope superior sea eliminado.
#Ejemplo:
def main():
  a = 1

  def nested():
    print(a)

  nested() # 1

main()

def make_multiplier(x):

    def multiplier(n):
        return x * n

    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))