'''
     Modelado de objetos mediate composición y herecia
'''

class Motor:
    def __init__(self, tipo: str):
        self.tipo = tipo
        
class Rueda:
    def __init__(self, tamano: str):
        self.tamano = tamano
        
        
class Coche:
    def __init__(self, marca: str, motor: Motor, ruedas: list[Rueda]):
        self.marca = marca
        self.motor = motor
        self.ruedas = ruedas
        
        
    def descripcion(self):
        print(f"Coche marca: {self.marca}")
        print(f"Tipo de motor: {self.motor.tipo}")
        print(f"Numeró de ruedas: {len(self.ruedas)}")
        
auto_uno = Coche(
    marca="VW",
    motor=Motor(tipo="Disel"),
    ruedas=[Rueda(tamano="16 pulgadas") for _ in range(4)]
)

auto_uno.descripcion()