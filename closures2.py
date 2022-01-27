def makerepeater(n):
    def repeater(string):
        assert type(string)==str, "Solo puedes usar Strings"
        return string*n
    return repeater


def run():
    repeat5=makerepeater(5)
    print(repeat5("Hola"))
    repeat10=makerepeater(10)
    print(repeat10("Platzi"))

if __name__== '__main__':
    run()