def suma(*args:float) -> float:
    return sum(args)

def resta(*args:float) -> float:
    resultado = args[0]
    for valor in args[1:]:
        resultado -= valor
    return resultado

def multiplicacion(*args:float) -> float:
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado

def division(*args:float) -> float:
    resultado = args[0]
    for valor in args[1:]:
        resultado /= valor
    return resultado

def calculadora(operacion, *args):
    if operacion == "+":
        return suma(*args)
    elif operacion == "-":
        return resta(*args)
    elif operacion == "*":
        return multiplicacion(*args)
    elif operacion == "/":
        return division(*args)
    else:
        print("Operación no reconocida")



operacion = input("¿Qué operación deseas hacer? (+,-,*,/): ")
valores = input("Introduce los valores con los que quieres operar separados por espacios: ")

valores = [float(valor) for valor in valores.split()]

print(f"El resultado es {calculadora(operacion, *valores)}")