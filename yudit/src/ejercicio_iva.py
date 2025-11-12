''' 
 Calcula el precio final con IVA incluido
 Recibe el prrecio del producto y el IVA a aplicar
 Retorna el precio final
'''
def precio_final(precio: float, iva: float) -> float:
    return precio + (precio * iva / 100)

donas: float = 20
iva: float = 16

print(f"El precio final de las donas es: {precio_final(donas, iva)}")

'''
Calcular el precio de los productos aplicandole el IVA
Este metodo recibe la lista de precios y el IVA a aplicar
Regresando una lista ya con los precios finales
'''
def precio_final_productos(productos: list, iva: float) -> list:
    return [precio_final(precio, iva) for precio in productos]

precios_productos: list = [20, 33.5, 16, 40.10]
print(f"Los precios finales de los productos son: {precio_final_productos(precios_productos, iva)}")