def factorial(a):
    resultado=1
    if a>1:
      #resultado=a*factorial(a-1)
      for i in range(1, a+1):
         resultado=resultado*i
    print('el resultado es: ', resultado)
    return resultado

a=int(input('Ingrese el numero: '))
print('El numero es: ', a)
valor=factorial(a)
print(valor)