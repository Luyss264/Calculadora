def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b == 0 or a == 0:
        print("ERROR: NO SE PUEDE DIVIDIR ENTRE 0")
    else:
        return a / b

def potencia(a,b):
    return a ** b

def raizCuadrada(a):
    if a < 0:
        print("ERROR: NO SE PUEDE CALCULAR LA RAIZ DE UN NUMERO NEGATIVO")
    else:
        return a ** 0.5

def modulo(a,b):
    if b == 0:
        print("ERROR: NO SE PUEDE CALCULAR EL MODULO CON DIVISION POR CERO")
    else:
        return a % b

def promedio(args):
    if not args:
        print("ERROR: NO HAY NUMEROS PARA CALCULAR EL PROMEDIO")
        return None
    return sum(args) / len(args)

def calculadora():
    print("BIENVENIDO A LA CALCULADORA")
    print("SELECCIONA UNA OPCIÓN POR NÚMERO:")
    print("1-SUMA")
    print("2-RESTA")
    print("3-MULTIPLICACION")
    print("4-DIVISION")
    print("5-POTENCIA")
    print("6-RAIZ CUADRADA")
    print("7-MODULO")
    print("8-PROMEDIO")


    while True:
        try:
            opcion = int(input("ESCRIBA EL NÚMERO DE LA OPERACIÓN QUE DESEA REALIZAR: "))
            break
        except ValueError:
            print("OPCIÓN NO VALIDA")
            continue

    if opcion == 1:

        while True:
            try:
                num1 = int(input("INGRESA EL PRIMER NÚMERO: "))
                num2 = int(input("INGRESA EL SEGUNDO NÚMERO: "))
            except ValueError:
                print("VALOR NO VALIDO")
                continue

            resultado = suma(num1, num2)
            print(f"EL RESULTADO DE LA SUMA ES: {resultado}")
            break
    
    elif opcion == 2:
        
        while True:

            try:
                num1 = int(input("INGRESA EL PRIMER NÚMERO: "))
                num2 = int(input("INGRESA EL SEGUNDO NÚMERO: "))
            except ValueError:
                print("VALOR NO VALIDO")
                continue

            resultado = resta(num1, num2)
            print(f"EL RESULTADO DE LA RESTA ES: {resultado}")
            break

    elif opcion == 3:
        
        while True:

            try:
                num1 = int(input("INGRESA EL PRIMER NÚMERO: "))
                num2 = int(input("INGRESA EL SEGUNDO NÚMERO: "))
            except ValueError:
                print("VALOR NO VALIDO")
                continue

            resultado = multiplicacion(num1, num2)
            print(f"EL RESULTADO DE LA MULTIPLICACION ES: {resultado}")
            break
    
    elif opcion == 4:
        while True:

            try:
                num1 = int(input("INGRESA EL PRIMER NÚMERO: "))
                num2 = int(input("INGRESA EL SEGUNDO NÚMERO: "))
            except ValueError:
                print("VALOR NO VALIDO")
                continue

            resultado = division(num1, num2)
            print(f"EL RESULTADO DE LA DIVISION ES: {resultado}")
            break

    elif opcion == 5:
        
        while True:

            try:
                num1 = int(input("INGRESA EL PRIMER NÚMERO: "))
                num2 = int(input("INGRESA EL SEGUNDO NÚMERO: "))
            except ValueError:
                print("VALOR NO VALIDO")
                continue

            resultado = potencia(num1, num2)
            print(f"EL RESULTADO DE LA POTENCIA ES: {resultado}")
            break
    
    elif opcion == 6:

        while True:

            try:
                num1 = int(input("INGRESA EL PRIMER NÚMERO: "))
            except ValueError:
                print("VALOR NO VALIDO")
                continue

            resultado = raizCuadrada(num1)
            print(f"EL RESULTADO DE LA RAIZ CUADRADA ES: {resultado}")
            break

    elif opcion == 7:

        while True:   

            try:
                num1 = int(input("INGRESA EL PRIMER NÚMERO: "))
                num2 = int(input("INGRESA EL SEGUNDO NÚMERO: "))
            except ValueError:
                print("VALOR NO VALIDO")
                continue

            resultado = modulo(num1, num2)
            print(f"EL RESULTADO DEL MODULO ES: {resultado}")
            break

    elif opcion == 8:
            
        while True:    

            try:
                numeros = input("INGRESA LOS NÚMEROS SEPARADOS POR COMAS: ")
                listaNumeros = [int(num) for num in numeros.split(",")]

            except ValueError:
                print("VALOR NO VALIDO")
                continue
            
            resultado = promedio(listaNumeros)
            print(f"EL RESULTADO DEL PROMEDIO ES : {resultado}")
            break

        
calculadora()