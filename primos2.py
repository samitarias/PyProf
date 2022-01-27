def esprimo (numero: int):
    if numero < 1 :
        print(f'El numero {numero} no es un numero primo')
    elif numero == 2:
        print(f'El numero {numero} es un numero primo')
    else:
        for i in range (2, numero):
            if numero % i == 0:
                print(f'El numero {numero} no es un numero primo')
        print(f'El numero {numero} es un numero primo')
        
if __name__ == '__main__':
    x=int(input('Ingrese un numero:'))
    esprimo(x)
