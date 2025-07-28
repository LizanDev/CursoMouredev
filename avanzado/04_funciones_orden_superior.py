# 1. Crea una funciÃ³n que reciba una funciÃ³n y un nÃºmero, y devuelva el resultado de aplicar la funciÃ³n al nÃºmero.
def aplicar_funcion(funcion, numero):
    return funcion(numero)
print(aplicar_funcion(lambda x: x**2, 3))

# 2. Crea una funciÃ³n que reciba dos nÃºmeros y una funciÃ³n, y devuelva el resultado de sumar los dos nÃºmeros y aplicar 
# la funciÃ³n.
def sumar_y_aplicar(numero1, numero2, funcion):
    return funcion(numero1 + numero2)
print(sumar_y_aplicar(1,2,lambda x: x**2))

# 3. Crea una funciÃ³n que devuelva otra funciÃ³n que sume un nÃºmero fijo.
def sumar_fijo(numero):
    return lambda x: x+numero
print(sumar_fijo(5)(10))

# 4. Usa map() con lambda para multiplicar cada nÃºmero de una lista por 10.
print(list(map(lambda x: x*10, [1,2,3,4,5])))

# 5. Usa filter() con lambda para quedarte solo con los nÃºmeros pares.
print(list(filter(lambda x: x%2==0, [1,2,3,4,5])))

# 6. Usa reduce() con lambda para obtener la suma total de una lista.
from functools import reduce
print(reduce(lambda x,y: x+y, [1,2,3,4,5]))

# 7. Escribe una funciÃ³n que devuelva una funciÃ³n que reciba un nombre y devuelva â€œHola, â€.
def hola_nombre(nombre):
    return lambda : f"Hola, {nombre}"
print(hola_nombre("Lizan")())

# 8. Crea una funciÃ³n que reciba una lista y una funciÃ³n, y cuente cuÃ¡ntos elementos cumplen con la funciÃ³n.
def contador(lista, funcion):
    return len(list(filter(funcion, lista)))
print(contador([1,2,3,4,5],lambda x: x%2==0))

# 9. Crea una funciÃ³n que reciba dos funciones y un nÃºmero, y las aplique en orden.
def aplicar_funciones(funcion1,funcion2,numero):
    return funcion2(funcion1(numero))
print(aplicar_funciones(lambda x: x**2, lambda x: x+1, 2))

# 10. Crea una funciÃ³n que reciba una lista y una funciÃ³n, y aplique esa funciÃ³n a cada elemento usando un bucle (sin map).
def aplicar_funcion_bucle(lista, funcion):
    for i in range(len(lista)):
        lista[i] = funcion(lista[i])
    return lista
print(aplicar_funcion_bucle([1,2,3,4,5],lambda x: x**2))
