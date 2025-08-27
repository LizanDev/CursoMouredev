# 1. Genera un SyntaxError al imprimir una cadena sin parÃ©ntesis.
# print"Hola, que tal"
# 2. Genera un NameError intentando usar una variable no definida.
# print(edad)
# 3. Genera un IndexError accediendo a un Ã­ndice inexistente de una lista.
lista_inexistente = [1, 2, 3]
# print(lista_inexistente[4])
# 4. Genera un ModuleNotFoundError al importar un mÃ³dulo inexistente.
# import maths
# 5. Genera un AttributeError accediendo a un atributo que no existe.

# print(math.PI)
# 6. Genera un KeyError al acceder a una clave inexistente de un diccionario.
my_dic = {"saludo": "hola", "nombre": "toni"}
# print(my_dic["salud"])
# 7. Genera un TypeError usando tipos incorrectos (Ã­ndice string en lista).
# print(lista_inexistente["0"])

# 8. Genera un ImportError al importar una funciÃ³n que no existe desde un mÃ³dulo.
# from math import PI

# 9. Genera un ValueError intentando convertir un string no numÃ©rico a entero.
# my_int = int("no es un numero")
# print(my_int)

# 10. Intenta detectar si un error ocurre usando try-except con un KeyError.
my_dict = {"course": "Python"}
try:
    print(my_dict["name"])
except KeyError:
    print("Error: clave no encontrada")
