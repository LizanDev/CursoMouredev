class car:
    def __init__(self, marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def mostrar_info(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nAño: {self.año}")