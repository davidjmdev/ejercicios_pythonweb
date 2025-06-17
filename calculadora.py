while True:
    try:
        entrada = input("Introduce la operación y pulsa Enter (q para salir): ")
        if entrada.lower() in ("q",):
            break
        print(eval(entrada))
    except Exception:
        print("La entrada no es correcta, utiliza los operadores predeterminados de Python")