# 1. Crea una función que sume dos números.
def suma(x, y):
    return x + y


print(suma(5, 3))


# 2. Crea una función que calcule el cuadrado de un número.
def cuadrado(x):
    return x**2


print(cuadrado(4))


# 3. Crea una función que devuelva el mayor de dos números.
def mayor(x, y):
    return x if x > y else y


print(mayor(10, 20))


# 4. Crea una función que sume 10 a un número dado.
def suma_diez(x):
    return x + 10


print(suma_diez(5))


# 5. Crea una función que devuelva el último carácter de una cadena.
def ultimo_caracter(cadena):
    return cadena[-1] if cadena else None


print(ultimo_caracter("Hola"))


# 6. Crea una función que indique si una palabra tiene más de 6 letras.
def palabra_larga(palabra):
    return len(palabra) > 6


print(palabra_larga("prigramacion"))


# 7. Crea una función que convierta una cadena a minúsculas.
def minusculas(cadena):
    return cadena.lower()


print(minusculas("HOLA MUNDO"))


# 8. Crea una función que devuelva True si un número es positivo.
def positivo(x):
    return x > 0


print(positivo(-3))


# 9. Crea una función que devuelva "Cadena vacía" si el string está vacío.
def cadena_vacia(cadena):
    return "Cadena vacia" if not cadena else cadena


print(cadena_vacia(""))


# 10. Crea una función que calcule el precio final con un impuesto añadido del 21%.
def precio_final(precio):
    return precio * 1.21


print(precio_final(200))
