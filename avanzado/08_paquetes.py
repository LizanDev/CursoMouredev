import math

import numpy as np
import pandas as pd
import requests

# 1. Importa el mÃ³dulo math y muestra el valor de pi.

print(math.pi)

# 2. Crea un array de nÃºmeros usando numpy y multiplÃ­calo por 3.
array = np.array([1, 2, 3, 4, 5])
array = array * 3
print(array)

# 3. Muestra la versiÃ³n instalada de numpy.
print(np.__version__)

# 4. Realiza una peticiÃ³n HTTP con requests a una API pÃºblica y muestra el cÃ³digo de estado.
response = requests.get("https://pokeapi.co/api/v2/pokemon")
print(response.status_code)


# 5. Importa una funciÃ³n llamada sum_two_values desde un paquete personalizado mypackage.arithmetics y utilÃ­zala.


# 6. Usa pandas para crear un DataFrame con nombres en espaÃ±ol.
data = {"Nombre": ["Pikachu", "Charmander", "Bulbasur"]}
pf = pd.DataFrame(data)
print(pf)

# 7. Ejecuta el comando para instalar el paquete requests desde la terminal.
"""pip install requests"""

# 8. Usa requests para obtener datos de una API y extrae solo los nombres de los primeros PokÃ©mon.
pokemones = response.json()
nombres = [pokemon["name"] for pokemon in pokemones["results"]]
print(nombres)


# 9. Muestra todos los paquetes instalados con pip desde la terminal.
"""pip list"""

# 10. Escribe una lÃ­nea de cÃ³digo que muestre la ayuda sobre el paquete numpy desde Python.
print(np.info())
