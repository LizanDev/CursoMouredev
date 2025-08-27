import re

# 1. Busca si una cadena empieza por "Hola".
mi_variable = "Hola, como estas?"

if re.match(r"Hola", mi_variable):
    print("La cadena empieza por 'Hola'")


# 2. Busca la palabra "Python" en una cadena aunque estÃ© en minÃºsculas.
mi_otra_variable = "esto es python"
if re.search(r"python", mi_otra_variable, re.IGNORECASE):
    print("La cadena contiene la palabra 'Python'")

# 3. Encuentra todas las apariciones de la palabra "curso" en una cadena.
mi_tercer_variable = "Curso de python, curso de Java, curso de c++"
if contador := re.findall(r"curso", mi_tercer_variable, re.IGNORECASE):
    print(f"La cadena contiene la palabra 'curso'{len(contador)} veces")

# 4. Reemplaza todas las apariciones de "lecciÃ³n" por "LECCIÃ“N".
mi_cuarta_variable = "leccion de python"
if nueva_variable := re.sub(r"leccion", "LECCION", mi_cuarta_variable):
    print(nueva_variable)

# 5. Divide un texto en partes separadas por comas.
mi_quinta_variable = "manzana,pera,platano,fresa"
if partes := re.split(r",", mi_quinta_variable):
    print(partes)

# 6. Busca la primera palabra que comience con "A" o "a".
mi_sexta_variable = "esto es una aventura"
if palabra := re.search(r"\b[aA]\w*", mi_sexta_variable):
    print(f"La primera palabra que empieza por 'A' o 'a' es: {palabra.group()}")

# 7. Encuentra todas las palabras en una cadena que terminen en "ciÃ³n".
mi_septima_variable = "educacion, formacion, programacion, python, java"
if palabras := re.findall(r"\b\w*ci[oó]n\b", mi_septima_variable, re.IGNORECASE):
    print(f"Palabras que terminan en 'ción': {palabras}")

# 8. Verifica si una cadena contiene solo nÃºmeros.
mi_octava_variable = "12345a"
if re.fullmatch(r"\d+", str(mi_octava_variable)):
    print("La cadena contiene solo numeros")

# 9. Reemplaza todos los nÃºmeros de una cadena por el texto "[nÃºmero]".
mi_novena_variable = "Tengo 2 manzanas y 3 peras"
if nueva_variable := re.sub(r"\d+", "[numero]", mi_novena_variable):
    print(nueva_variable)

# 10. Encuentra todas las palabras de 4 letras exactas en una cadena.
mi_decima_variable = "Este es un test para ver las palabras que contienen cuatro letras"
if palabras := re.findall(r"\b\w{4}\b", mi_decima_variable):
    print(f"Palabras de 4 letras: {palabras}")
