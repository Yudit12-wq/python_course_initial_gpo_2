import logging

'''
Configuración del logging
'''
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='logs.log',
)

'''
Ejemplos de logging en Python
'''
logging.debug("Log nivel debug")
logging.info("Log nivel info")
logging.warning("Log nivel warning")
logging.error("Log nivel error")


class CustomError(Exception):
    ''' Clase de error personalizada'''
    pass

def funcion_con_error(n1: int):
    if(n1 < 0):
        raise CustomError("Error: numero menor a 0")
    logging.info("El numero es correcto")

'''
Manejo de excepciones
'''
try:
    funcion_con_error(-5)
except Exception as e:
    logging.error(f"Error: {e}")
else:
    logging.info(f"Ejecución correcta")
finally:
    logging.info("Ejecución finalizada")