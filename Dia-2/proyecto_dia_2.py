# Proyecto Día 2
nombre = input('Vendedor ingrese su nombre: \n')
ventas = float(input('Ahora ingrese las ventas del mes: \n'))
comisiones = round(ventas * 0.13, 2)

print(f'Hola {nombre} tus comisiones ganadas de este mes son:\n\t$ {comisiones}')
