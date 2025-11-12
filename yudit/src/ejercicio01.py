# Comentario en linea

'''
Comentario de bloque
Que puede ser multilinea
Comilla simple
Comilla doble
'''

# Tipos de datos, no hay problema si tiene el mismo nombre

mi_variable: int = 10
print(type(mi_variable))
mi_variable: float = 10.5
print(type(mi_variable))
mi_variable: str = "Hola, Mundo"
print(type(mi_variable))
mi_variable: bool = True # es con mayuscula al inicio
print(type(mi_variable))

# Imprimir en cconsola
print("Hola mundo")

#Estructiura de datos
#Listas
mi_lista: list = [1, 2, 3]
print(type(mi_lista))
mi_lista[2] = 4 # Modificar un elemento de la lista
print(type(mi_lista))

#Tuplas, no son modificables
mi_tupla: tuple = (1, 2, 3)

print(type(mi_tupla))

#Diccionarios, son clave vlor
mi_diccionario: dict = {"clave1": "valor1", "clave2": "valor2"}
print(type(mi_diccionario))

#Sets
mi_set: set = {1, 2, 3}

#f strings
nombre: str = "Yudit"
print("Hola, " + nombre) # Concatenar tradicional
print(f"Hola, {nombre}") # Uso de f strings


'''
Compresiones
'''

cuadrados: list = [x**2 for x in range(10)]
print(cuadrados)

# Breack, continue, else en bucles
