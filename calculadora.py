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

    try:
        opcion = int(input("ESCRIBA EL NÚMERO DE LA OPERACIÓN QUE DESEA REALIZAR: "))
    except ValueError:
        print("OPCIÓN NO VALIDA")


    if opcion == 1:

        try:
            num1 = float(input("INGRESA EL PRIMER NÚMERO: "))
            num2 = float(input("INGRESA EL SEGUNDO NÚMERO: "))
        except ValueError:
            print("VALOR NO VALIDO")

        resultado = suma(num1, num2)
        print(f"EL RESULTADO DE LA SUMA ES: {resultado}")
    
    elif opcion == 2:
        try:
            num1 = float(input("INGRESA EL PRIMER NÚMERO: "))
            num2 = float(input("INGRESA EL SEGUNDO NÚMERO: "))
        except ValueError:
            print("VALOR NO VALIDO")

        resultado = resta(num1, num2)
        print(f"EL RESULTADO DE LA RESTA ES: {resultado}")

    elif opcion == 3:
        try:
            num1 = float(input("INGRESA EL PRIMER NÚMERO: "))
            num2 = float(input("INGRESA EL SEGUNDO NÚMERO: "))
        except ValueError:
            print("VALOR NO VALIDO")
        resultado = multiplicacion(num1, num2)
        print(f"EL RESULTADO DE LA MULTIPLICACION ES: {resultado}")
    
    elif opcion == 4:
        try:
            num1 = float(input("INGRESA EL PRIMER NÚMERO: "))
            num2 = float(input("INGRESA EL SEGUNDO NÚMERO: "))
        except ValueError:
            print("VALOR NO VALIDO")
        resultado = division(num1, num2)
        print(f"EL RESULTADO DE LA DIVISION ES: {resultado}")

    elif opcion == 5:
        try:
            num1 = float(input("INGRESA EL PRIMER NÚMERO: "))
            num2 = float(input("INGRESA EL SEGUNDO NÚMERO: "))
        except ValueError:
            print("VALOR NO VALIDO")
        resultado = potencia(num1, num2)
        print(f"EL RESULTADO DE LA POTENCIA ES: {resultado}")
    
    elif opcion == 6:
        try:
            num1 = float(input("INGRESA EL PRIMER NÚMERO: "))
        except ValueError:
            print("VALOR NO VALIDO")
        resultado = raizCuadrada(num1)
        print(f"EL RESULTADO DE LA RAIZ CUADRADA ES: {resultado}")

    elif opcion == 7:
        try:
            num1 = float(input("INGRESA EL PRIMER NÚMERO: "))
            num2 = float(input("INGRESA EL SEGUNDO NÚMERO: "))
        except ValueError:
            print("VALOR NO VALIDO")
        resultado = modulo(num1, num2)
        print(f"EL RESULTADO DEL MODULO ES: {resultado}")

    elif opcion == 8:
        try:
            numeros = input("INGRESA LOS NÚMEROS SEPARADOS POR COMAS: ")
            listaNumeros = [float(num) for num in numeros.split(",")]
        except ValueError:
            print("VALOR NO VALIDO")
        
        resultado = promedio(listaNumeros)
        print(f"EL RESULTADO DEL PROMEDIO ES : {resultado}")

        
calculadora()