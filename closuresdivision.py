def makedivisionby(n):
    def divisor(x):
        assert n>0, "El valor debe ser mayor a 0"
        return x/n
    return divisor

divisionby3=makedivisionby(3)
print(divisionby3(18))

divisionby3=makedivisionby(5)
print(divisionby3(100))

divisionby3=makedivisionby(18)
print(divisionby3(54))