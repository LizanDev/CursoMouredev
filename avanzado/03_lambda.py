# 1. Crea una lambda que sume dos nÃºmeros.
suma = lambda x, y: x + y
print(suma(5,3))
# 2. Crea una lambda que calcule el cuadrado de un nÃºmero.
cuadrado = lambda x: x**2
print(cuadrado(4))

# 3. Crea una lambda que devuelva el mayor de dos nÃºmeros.
mayor = lambda x, y: x if x > y else y
print(mayor(10,20))

# 4. Crea una lambda que sume 10 a un nÃºmero dado.
suma_diez = lambda x: x + 10
print(suma_diez(5))

# 5. Crea una lambda que devuelva el Ãºltimo carÃ¡cter de una cadena.
ultimo_caracter = lambda cadena: cadena[-1] if cadena else None
print(ultimo_caracter("Hola"))

# 6. Crea una lambda que indique si una palabra tiene mÃ¡s de 6 letras.
palabra_larga = lambda palabra: len(palabra) > 6
print(palabra_larga("prigramacion"))

# 7. Crea una lambda que convierta una cadena a minÃºsculas.
minusculas = lambda cadena: cadena.lower()
print(minusculas("HOLA MUNDO"))

# 8. Crea una lambda que devuelva True si un nÃºmero es positivo.
positivo = lambda x: x > 0
print(positivo(-3))

# 9. Crea una lambda que devuelva "Cadena vacÃ­a" si el string estÃ¡ vacÃ­o.
cadena_vacia = lambda cadena: "Cadena vacia" if not cadena else cadena
print(cadena_vacia(""))

# 10. Crea una lambda que calcule el precio final con un impuesto aÃ±adido del 21%.
precio_final = lambda precio: precio *1.21
print(precio_final(200))

