# 1. Crea un archivo de texto y escribe en Ã©l la frase "Hola desde Python".
my_file = open("mi_archivo.txt","r+")
my_file.write("Hola desde python")
#my_file.close()

# 2. Abre un archivo y lee todo su contenido.
my_file.seek(0)
print(my_file.read())

# 3. AÃ±ade una nueva lÃ­nea al final del archivo con el texto "LÃ­nea aÃ±adida".
my_file.write("\nLinea añadida")
# 4. Lee solo los primeros 10 caracteres del archivo.
my_file.seek(0)
print(my_file.read(10))

# 5. Usa seek para volver al inicio del archivo y leer desde ahÃ­.
my_file.seek(0)
print(my_file.read())
# 6. Lee e imprime el contenido lÃ­nea por lÃ­nea usando readline.
my_file.seek(0)
print(my_file.readline())

# 7. Lee todas las lÃ­neas del archivo en una lista y recÃ³rrelas con un bucle.
my_file.seek(0)
for line in my_file:
    print(line.strip())

# 8. Crea un archivo nuevo que sobrescriba si ya existe, y escribe varias lÃ­neas.
with open("nuevo_archivo.txt","w") as new_file:
    new_file.write("Linea 1")
    new_file.write("\nLinea 2")
    new_file.write("\nLinea 3")

# 9. Usa una funciÃ³n para abrir un archivo, escribir texto y cerrarlo automÃ¡ticamente con with.
def write_to_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)

# 10. Lee un archivo lÃ­nea por lÃ­nea y muestra solo las que contienen la palabra "Python".
with open("mi_archivo.txt","r") as file:
    for line in file:
        if "Python" in line:
            print(line.strip())