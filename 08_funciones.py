# 1. Crea una funciÃ³n llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>".
#  Si no se proporciona ningÃºn nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(name="desconocido"):
    print(f"Hola, {name}")
personalized_greeting("Toño")
personalized_greeting()
# 2. Escribe una funciÃ³n llamada "multiply" que reciba dos nÃºmeros como argumentos y retorne el resultado de 
# multiplicarlos.
def multiply(num1,num2):
    return num1 * num2
print(multiply(5,3))

# 3. Crea una funciÃ³n llamada "is_even" que reciba un nÃºmero entero como argumento y retorne True si es par y 
# False si es impar.
number = int(input("Ingrese un numero entero: "))
def is_even(number):
    return number %2 == 0
if is_even(number):
    print(f"{number} ess par")
else:
    print(f"{number} es impar")

# 4. Escribe una funciÃ³n llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayÃºsculas.
def convert_to_uppercase(text):
    return text.upper()
print(convert_to_uppercase("hola mundo"))
# 5. Crea una funciÃ³n llamada "arbitrary_sum" que reciba un nÃºmero arbitrario de nÃºmeros como argumentos y 
# retorne la suma de todos ellos.
def arbitrary_sum(*args):
    total = 0
    for num in args:
        total += num
    return total
print(arbitrary_sum(1,2,3,4,5))
# 6. Escribe una funciÃ³n llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y 
# retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
def generate_full_greeting(name, surname):
    return f"Hola, {name}{surname}"
print(generate_full_greeting(name="Toño ", surname="Lizan"))
# 7. Crea una funciÃ³n llamada "power" que reciba dos nÃºmeros: base y exponente, y retorne el resultado de 
# elevar la base al exponente.
def power(base, exponente):
    return base ** exponente
print(power(2,3))
# 8. Escribe una funciÃ³n llamada "calculate_average" que reciba tres nÃºmeros y retorne su promedio.
def calulate_average(num1,num2,num3):
    return (num1+num2+num3)/3
print(calulate_average(10,20,30))
# 9. Crea una funciÃ³n llamada "count_characters" que reciba una cadena de texto y retorne el nÃºmero de caracteres 
# que contiene.
def count_characters(text):
    return len(text)
print(count_characters("Hola mundo"))
# 10. Escribe una funciÃ³n llamada "display_messages" que reciba un nÃºmero indefinido de cadenas y las imprima 
# en mayÃºsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*messages):
    for message in messages:
        print(message.upper())
display_messages("Hola", "Toño", "lizan", "python")