string = "103 123 4444 99 2000"

def ordenar(digitos: str) -> tuple[int, str]:
    # Se convierte cada número en entero y se suman los dígitos
    empaquetado = (int(numero) for numero in digitos)
    return sum(empaquetado), digitos

def order_weight(strng: str) -> str:
    # Se divide la cadena en números individuales
    secuencia = strng.split()  # ["103", "123", "4444", "99", "2000"]

    # Se ordena la lista por la suma de los dígitos y luego alfabéticamente
    secuencia_final = sorted(secuencia, key=ordenar)

    # Se retorna la lista ordenada como una cadena con espacios
    return ' '.join(secuencia_final)

# Ejemplo de uso
print(order_weight(string))
