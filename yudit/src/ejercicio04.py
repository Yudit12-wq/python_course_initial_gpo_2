'''
    Decoradores -> Aumetar funcionalidad si modificar la función original
'''
   
import time


def decorador(func):
    def envoltura():
        print("Inicio")
        func()
        print("Final")
    return envoltura

@decorador
def saludar():
    print("Hola Mundo")
    
# saludo_decorado = decorador(saludar)
# saludo_decorado()
saludar()


# Decorador co args y kwargs

def decoradorr(func):
    def envoltura(*args, **kwargs):
        print(f"Inicio con args: {args} y kwargs: {kwargs}")
        func(*args, **kwargs)
        print("fial de mi decorador")
    return envoltura

@decoradorr
def suma(n1: int, n2: int):
    print(f"La suma es: {n1 + n2}")
    

# decorador par medir el tiempo de ejecución de una fución
def decorador3(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        print(f"Tiempo de inicio: {inicio}")
        ejecucion = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de finalización: {fin}")
        print(f"Tiempo de ejeución: {fin - inicio}")
        return ejecucion
    return envoltura

@decorador3
def tiempo():
    time.sleep(1)
    print("Función que tarda 1 segundos en ejecutarse")
    
tiempo()
        