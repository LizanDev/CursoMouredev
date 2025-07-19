# 1. Genera una lista utilizando comprensiÃ³n con los nÃºmeros del 0 al 10.
mi_lista = [x for x in range(11)]
print(mi_lista)

# 2. Crea una lista utilizando comprensiÃ³n con los cuadrados de los nÃºmeros del 1 al 10.
mi_lista_cuadrados = [x**2 for x in range(1,11)]
print(mi_lista_cuadrados)

# 3. Genera una lista utilizando comprensiÃ³n con los nÃºmeros pares del 0 al 20.
mi_lista_pares = [x for x in range(21) if x % 2 == 0]
print(mi_lista_pares)

# 4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensiÃ³n.4
temperatura_celsius = [10,20,30,40,50]
temperatura_fahrenheit = [(c* 9/5)+32 for c in temperatura_celsius]
print(temperatura_fahrenheit)

# 5. Crea una lista utilizando comprensiÃ³n con los caracteres de una cadena.
cadena = "Hola mundo"
mi_lista_caracteres = [c for c in cadena]
print(mi_lista_caracteres)

# 6. Filtra una lista de palabras y deja solo las que tienen mÃ¡s de 4 letras utilizando comprensiÃ³n.
palabras = ["Hola","Python","es","no","programacion","si"]
palabras_largas = [p for p in palabras if len(p) > 4]
print(palabras_largas)

# 7. Aumenta en 5 cada nÃºmero de una lista con comprensiÃ³n usando una funciÃ³n externa.
def aumentar_cinco(x):
    return x+5
numeros = [1,2,3,4,5]
numeros_sumados = [aumentar_cinco(n) for n in numeros]
print(numeros_sumados)

# 8. Crea una lista de booleanos que indique si cada nÃºmero es mayor que 10 utilizando comprensiÃ³n.
numeros = [5,10,15,20]
mayores_diez = [n for n in numeros if n > 10]
print(mayores_diez)

# 9. Multiplica solo los nÃºmeros impares por 3 en una lista utilizando comprensiÃ³n.
numeros = [1,2,3,4,5,6,7,8,9]
numeros_impares_multi = [n * 3 for n in numeros if n % 2 != 0]
print(numeros_impares_multi)

# 10. Usa comprensiÃ³n de listas anidada para generar una matriz 3x3 con nÃºmeros del 1 al 9.
matriz = [[x + y * 3 for x in range(1,4)] for y in range(3)]
print(matriz)