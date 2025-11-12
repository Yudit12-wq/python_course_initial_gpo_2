'''
Clase
'''

class Producto:
    
    
    ''' Constructor de la clase'''
    def __init__(self, nombre: str):
        self._nombre: str = nombre
        
    
    @property
    def nombre(self) -> str:
        '''Permitir acceder a la propiedad nombre de maera segura'''
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if(len(nuevo_nombre) < 1):
            raise ValueError("El nombre debe tener al menos un caracter")
        self._nombre = nuevo_nombre


producto = Producto("Lap")

print(f"El nombre del producto es: {producto.nombre}")