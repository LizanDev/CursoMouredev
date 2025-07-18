# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un mÃ©todo "make_sound" que imprima un 
# sonido genÃ©rico.
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Sonido animal generico")


# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacÃ©nala en una propiedad pÃºblica.
#  AÃ±ade el mÃ©todo "make_sound" que imprima un sonido dependiendo de la especie.
class Animal:
    def __init__ (self, species):
        self.species = species
    def make_sound(self):
        if self.species == "dog":
            print("Guau!")
        elif self.species == "cat":
            print("Miau!")
        else:
            print("Sonido generico de animal")
Animal1 = Animal("dog")
Animal1.make_sound()
# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model". AdemÃ¡s, debe tener una 
#  privada "_speed" que inicialmente serÃ¡ 0.
class Car:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0

# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate" que aumente la velocidad en 10 unidades. AÃ±ade tambiÃ©n
#  un mÃ©todo "brake" que reduzca la velocidad en 10 unidades. AsegÃºrate de que la velocidad no sea negativa.
    def accelerate(self):
        self._speed += 10
    
    def brake(self):
        if self._speed >= 10:
            self._speed -= 10
        else:
            self._speed = 0
    
# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author" (privado). AÃ±ade un mÃ©todo 
# para obtener el autor y otro para cambiar el tÃ­tulo del libro.
class Book:
    def __init__ (self, title, author):
        self.title = title
        self._author = author
    def get_author(self):
        return self._author
    def set_title(self, new_title):
        self.title = new_title
    
# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. 
# AÃ±ade un mÃ©todo para calcular y devolver la nota media del estudiante.
class Estudiante:
    def __init__ (self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = []
    def agregar_notas(self, nota):
        self.notas.append(nota)
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas)/len(self.notas)
    
# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". AÃ±ade mÃ©todos para depositar y 
# retirar dinero, asegurÃ¡ndote de que no se pueda retirar mÃ¡s de lo que hay en la cuenta.
class BankAccount:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance
    def depositar(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposito efectuado. Nuevo saldo: {self.balance}")
    def retirar(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Retiro de dinero efectuado. Nuevo saldo: {self.balane}")
        else:
            print("Fondos insuficientes o cantidad no valida para retirar.")

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". AÃ±ade un mÃ©todo 
# que calcule la distancia entre dos puntos.
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distania(self, other_point):
        return ((self.x - other_point.x) **2 + (self.y - other_point.y) **2) ** 0.5
    
# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked".
#  AÃ±ade un mÃ©todo que calcule el pago total basado en las horas trabajadas y el salario por hora.
class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_total_pay(self):
        return self.hourly_wage * self.hours_worked

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). AÃ±ade un mÃ©todo para
#  agregar un producto al inventario y otro para mostrar todos los productos disponibles.
class Store:
    def __init__(self):
        self.inventory = []
    def add_product(self, product):
        self.inventory.append(product)
    def show_poducts(self):
        if not self.inventory:
            print("Inventario vacio")
        else:
            print("Productos disponibles:")
            for product in self.inventory:
                print(product)