'''
    Args y kwargs
'''

# args: argumentos posicionales - reciben por posición

def procesar_datos(*args) -> None:
    print(f"Argumentos posicionales recibidos: {args}")
    
mitupla = (1, 2, 3, 4)

procesar_datos(2, 3, 4)

# kwargs: argumentos nombrados
def saludos_dinamicos(**kwargs) -> None:
    print(f"Argumentos nombrados recibidos: {kwargs}")
    
saludos_dinamicos(nombre="Yudit", edad=25)

# Generadores -> para manejar grandes volumenes de datos, utilizan yield en lugar de return

def generar_datos(limite: int):
    ''' Generador que produce números hasta un limite dado'''
    for num in range(limite):
        print(f"Bucle en posición {num}")
        yield num
        print(f"Fin del generador")
        
def generar_datos_tradicional(limite: int) -> list:
    ''' Función tradicional que devuelve una lista de números hasta un limite dado'''
    resultado: list = []
    for num in range(limite):
        print(f"Bucle en posición {num}")
        resultado.append(num)
        print(f"Fin de la función tradicional")
    return resultado

print("Uso del generador")
print(type(generar_datos))
generador = generar_datos(5)

for item in generador:
    print(f"Valor generado: {item}")
    
listaa = generar_datos_tradicional(5)

for item in listaa:
    print(f"Valor generado: {item}")

# Ejercicio de fibonacci co generadores
def generador_fibonacci(n: int):
    """
    Generador que produce los primeros n números de la serie Fibonacci
    Ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21...
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Pruebas del generadores
print("SERIE FIBONACCI")

print("Primeros 10 números de Fibonacci:")
for num in generador_fibonacci(10):
    print(num, end=" ")

print("Primeros 8 números de Fibonacci:")
fib_gen = generador_fibonacci(8)
for num in fib_gen:
    print(num, end=" ")
