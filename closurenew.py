def listar(n)-> int: 
    lista=[]
    for _ in range(n):
        x=int(input("Ingrese el numero: "))
        lista.append(x)
    print('Esta es la lista de elementos: ',lista)    
    print(sum(lista))
    
def suma_cuenta(lista):
    def agregatexto():
        #suma=sum(lista)
        #print('La suma de los elementos es: ',lista)
        print(sum(lista))
    return agregatexto

if __name__=='__main__':
    y=int(input("¿Cuantos elementos desea sumar?  "))
    listar(y)
    f=suma_cuenta(y)
    print(suma_cuenta)