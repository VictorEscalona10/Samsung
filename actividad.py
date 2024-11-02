# actividad 1

def cambio(cantidad, monedas):
    cambios = []
    mayor = 0  # -> Proceso de selección

    monedas.sort(reverse=True)
    
    while cantidad > 0 and mayor < len(monedas):
        print(f"Iteración: mayor = {mayor}, cambios = {cambios}, cantidad = {cantidad}")
        if cantidad < monedas[mayor]:  # -> Comprobación de viabilidad
            mayor += 1
        else:
            cambios.append(monedas[mayor])  # -> Comprobación de solución
            cantidad -= monedas[mayor]
            
    print(f"Estado final: mayor = {mayor}, cambios = {cambios}, cantidad = {cantidad}")
    return cambios 

monedas = [500, 400, 100, 50, 10]
cantidad = int(input("Dame la cantidad: "))
cambios = cambio(cantidad, monedas)
print("Cambio: ", cambios)

'''
Iteración: mayor = 0, cambios = [], cantidad = 800
Iteración: mayor = 0, cambios = [500], cantidad = 300
Iteración: mayor = 1, cambios = [500], cantidad = 300
Iteración: mayor = 2, cambios = [500], cantidad = 300
Iteración: mayor = 2, cambios = [500, 100], cantidad = 200
Iteración: mayor = 2, cambios = [500, 100, 100], cantidad = 100      
Estado final: mayor = 2, cambios = [500, 100, 100, 100], cantidad = 0
Cambio:  [500, 100, 100, 100]
'''

# actividad 2
# 1, 500, 1, 100, 3, 50, 2, 10

def cambio_moneda2(cantidad, monedas):
    cambio = []
    monedas.sort(key=lambda x: x[1], reverse=True)
    
    for cantidad_monedas, valor_moneda in monedas:
        if cantidad <= 0:
            break  # Salir si ya no queda monto por cambiar
        
        max_monedas_a_usar = cantidad // valor_moneda 
        num_monedas = min(max_monedas_a_usar, cantidad_monedas) 
        
        if num_monedas > 0:
            cambio.append([num_monedas, valor_moneda])  
            cantidad -= num_monedas * valor_moneda

    if cantidad > 0:
        return "No se puede hacer el cambio con las monedas disponibles."
    
    return cambio

def crear_lista_monedas():
    monedas_str = input("Ingrese las monedas almacenadas (cantidad, valor): ").split()
    monedas = []
    for moneda in monedas_str:
        cantidad, valor = map(int, moneda.split(','))
        monedas.append([cantidad, valor])
    return monedas

monedas = crear_lista_monedas()
print("Las monedas son: ", monedas)
cant = int(input("Ingrese el monto: "))
cambios = cambio_moneda2(cant, monedas)
print("Cambio: ", cambios, len(cambios))











