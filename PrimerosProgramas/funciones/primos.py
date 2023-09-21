def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos(valor):
    primos = []
    for i in range(1, valor + 1):
        if es_primo(i):
            primos.append(i)
    return primos

def main():
    a = 1
    while a == 1:
        value = input('Ingrese un valor: ')
        value = int(value)
        primos = encontrar_primos(value)
        
        for i in range(1, value + 1):
            if i in primos:
                print(f'{i} es un primo')
            else:
                print(f'{i} no es un primo')
        
        print('\n¿Quieres continuar? Presiona 1 para hacerlo')
        a = input()
        a = int(a)

if __name__ == "__main__":
    main()
