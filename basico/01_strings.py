# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().
text = "aprendiendo python"
print(len(text))
# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.
cadena1 = "Hola"
cadena2 = "Python"
resultado = cadena1 + " " + cadena2
print(resultado)
# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.
cadena_con_salto = "Hola\nPython"
print(cadena_con_salto)
# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
nombre = "Toni"
apellido = "Lizan"
edad = 40
print(f"Hola, mi nombre es {nombre} {apellido} y tengo {edad} años.")
# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno.
variable = "python"
a, b, c, d, e, f = variable
print(a, b, c, d, e, f)
# 6. Extrae un â€œsliceâ€ de la palabra â€œProgramaciÃ³nâ€ para obtener los caracteres desde la posiciÃ³n 3 hasta la 7.
print(variable[3:8])
# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.
print(variable[::-1])
# 8. Convierte la cadena â€œaprendiendo pythonâ€ en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.
print(variable.upper())
# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€ en la cadena â€œProgramaciÃ³n en Pythonâ€.
print(variable.count("n"))
# 10. Verifica si la cadena â€œ12345â€ es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.
print("12345".isnumeric())


print("ñ á é í ó ú ü ¿ ¡")
