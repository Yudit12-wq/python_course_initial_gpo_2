
from dataclasses import dataclass


@dataclass
class Motor:
    tipo: str

@dataclass       
class Rueda:
    tamano: str
        
@dataclass    
class Coche:
    marca: str
    motor: Motor
    ruedas: list[Rueda]
        
        
    def __str__(self):
        return (
            f"Coche marca: {self.marca}\n"
            f"Tipo de motor: {self.motor.tipo}\n"
            f"Numeró de ruedas: {len(self.ruedas)}")
        
auto_uno = Coche(
    marca="VW",
    motor=Motor(tipo="Diesel"),
    ruedas=[Rueda(tamano="16 pulgadas") for _ in range(4)]
)

print(auto_uno)