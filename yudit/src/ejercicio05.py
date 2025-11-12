class CustomError(Exception):
    ''' Clase de error personalizada'''
    pass

def funcion_con_error(n1: int):
    if(n1 < 0):
        raise CustomError("Error: numero menor a 0")
    print("El numero es correcto")

'''
Manejo de excepciones
'''
try:
    funcion_con_error(-5)
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"Ejecución correcta")
finally:
    print("Ejecución finalizada")