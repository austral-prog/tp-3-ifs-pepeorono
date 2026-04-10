def grades():
    """
    Ejercicio 5 - Clasificar Notas

    Leer una nota (0-10) mediante input(). Clasificar la nota e imprimir:
    - "Excelente" si está entre 9 y 10
    - "Bueno" si está entre 7 y 8
    - "Regular" si está entre 5 y 6
    - "Insuficiente" si está entre 0 y 4

    Ejemplo:
        Para la entrada "9", la salida esperada es:
        Excelente

        Para la entrada "6", la salida esperada es:
        Regular

        Para la entrada "3", la salida esperada es:
        Insuficiente
    """
    num = int(input())
    if num > 8 and num < 11:
        print("Excelente")
    elif num > 6 and num < 9:
        print("Bueno")
    elif num > 4 and num < 6:
        print("Regular")
    elif num < 4 or num ==0:
        print("Insuficiente")
#grades()
