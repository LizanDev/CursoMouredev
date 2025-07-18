def contar_palabras(texto, palabra):
    palabra = palabra.lower()
    palabras = texto.lower().split()
    contador = palabras.count(palabra)
    return contador