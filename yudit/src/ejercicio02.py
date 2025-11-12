'''
Funciones
'''

# def saludar() -> None:
#     ''' Función para saludar'''
#     print("Hola Mundo")

def saludar(nombre: str = "Yudit") -> None:
    ''' Función para saludar a una persona por su nombre'''
    print(f"Hola, {nombre}")    

# Toma el valor por defecto    
saludar()

# Pasa un valor diferente
saludar("Miriam")


'''
  Lambdas
'''

sumar = lambda num_1, num_2: num_1 + num_2

resultado: int = sumar(5, 3)

print(f"El resultado de la suma es: {resultado}")

'''
  Maps
'''
print("Map")
print(list(map(lambda num_1: num_1 ** 2, range(5))))


'''
    Filters
'''
print("Filter")
print(list(filter(lambda x: x % 2 == 0, range(10))))