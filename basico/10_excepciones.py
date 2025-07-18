# 1. Crea una funciÃ³n que intente dividir dos nÃºmeros proporcionados por el usuario. Usa try-except para capturar 
# cualquier error de divisiÃ³n (por ejemplo, divisiÃ³n por cero).
def dividir_numeros():
    try:
        num1 = float(input("Introduce un numero: "))
        num2 = float(input("Introduce otro numero: "))
        resultado = num1 / num2
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")
dividir_numeros()
# 2. Crea una funciÃ³n que tome una cadena e intente convertirla en un nÃºmero entero. Usa try-except para capturar 
# cualquier error en la conversiÃ³n.
def convertir_a_entero(cadena):
    try:
        numero = int(cadena)
        return numero
    except ValueError:
        print("Error: la cadena no se puede convertir a un entero")
convertir_a_entero("123abc")
# 3. Crea una funciÃ³n que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no 
# encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"Error: el archivo {nombre_archivo} no se encuentra")

# 4. Crea una funciÃ³n que realice mÃºltiples operaciones (suma, resta, divisiÃ³n, multiplicaciÃ³n) con dos nÃºmeros.
# Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de 
# los errores.
def operaciones_numericas(num1, num2):
    try:
        suma = num1 + num2
        resta = num1 - num2
        division = num1 / num2
        multiplicacion = num1 * num2
        print(f"Suma: {suma}, Resta: {resta}, Division: {division}, Multiplicacion: {multiplicacion}")
    except ZeroDivisionError:
        print("Error, no se puede dividir por cero")
    except TypeError:
        print("Error, los valores deben ser numeros")
    else:
        print("Operaiones realizadas con exito")
    finally:
        print("Fin de las operaciones")
operaciones_numericas(10,5)

# 5. Crea una funciÃ³n que le pida al usuario su edad y lance un ValueError si la entrada no es un nÃºmero entero 
# positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea 
# necesario.
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0:
            raise ValueError("La edad no puede ser negativo")
    except ValueError as e:
        print(e)
pedir_edad()

# 6. Crea una funciÃ³n que intente acceder a un elemento de una lista por Ã­ndice. Usa try-except para manejar el 
# caso donde el Ã­ndice estÃ© fuera de rango.
def acceder_elemento_lista(lista, indice):
    try:
        elemento = lista[indice]
        print(f"Elemento en el indice {indice}: {elemento}")
    except IndexError:
        print(f"Error en el indice {indice}")
acceder_elemento_lista([1,2,3],5)
# 7. Crea una funciÃ³n que use try-except para manejar mÃºltiples excepciones: ZeroDivisionError, ValueError y 
# TypeError.
def manejar_excepciones(num1, num2):
    try:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Error al dividir por cero")
    except ValueError:
        print("Error: valor no valido")
    except TypeError:
        print("Error tipo de dato no valido")
manejar_excepciones(10, 0)
# 8. Crea una funciÃ³n que simule una transacciÃ³n. Lanza una excepciÃ³n personalizada llamada InsufficientFundsError 
# si el saldo es menor que la cantidad a retirar.
def realizar_transaccion(saldo, cantidad):
    class InsufficientFundsError(Exception):
        def __init__(self,message):
            self.message = message
            try:
                if cantidad > saldo:
                    raise InsufficientFundsError("Fondos insuficientes")
            except InsufficientFundsError as e:
                print(e.message)
realizar_transaccion(100,150)

# 9. Crea una funciÃ³n que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja 
# cuando una cadena no pueda convertirse.
def convert_list_to_integers(string_list):
    integers = []
    for string in string_list:
        try:
            integers.append(int(string))
        except ValueError:
            print(f"Error: '{string}' no se puede transformar en un entero.")
    return integers

# 10. Crea una funciÃ³n que calcule la raÃ­z cuadrada de un nÃºmero. Lanza un ValueError si el nÃºmero es negativo.
def calculate_square_root(number):
    try:
        if number < 0:
            raise ValueError(
                "No se puede calcular la raÃ­z cuadrada de un nÃºmero negativo.")
        return number ** 0.5
    except ValueError as e:
        print(f"Error: {e}")