from xmlrpc.client import Boolean


def esprimo (numero: int) -> Boolean:
    if numero < 1 :
        return False
    elif numero == 2:
        return True
    else:
        for i in range (2, numero):
            if numero % i == 0:
                return False
        return True 
        
if __name__ == '__main__':
    x=int(input('Ingrese un numero:'))
    print(esprimo(x))
