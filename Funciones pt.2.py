# Funciones con retorno de valor

def multiplicar(num1,num2):
    mult = num1*num2
    return mult

print(multiplicar(3,4))

def prueba():
    return "Hola",4,[2,1,3]
c,n,l = prueba()

print(c)
print(n)
print(l)