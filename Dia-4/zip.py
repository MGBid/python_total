print('# ZIP')
print('Combina dos o más listas entrelazando sus elementos en tuples')
print('Si hay elementos extra en alguna de las listas, los ignora')
nombres = ['Juan', 'Pablo', 'Ana']
edades = [25, 42, 33, 55, 19]
zipeados = list(zip(nombres, edades))
print(zipeados)

nombres_2 = ['Ana', 'Hugo', 'Valeria']
edades_2 = [65, 29, 42]
ciudades = ['Lima', 'Madrid', 'México']

# Para verlo debemos Castearlo dentro de una Lista:
combinados = list(zip(nombres_2, edades_2, ciudades))
print(combinados)

# Se vuelve útil al momento de tener que imprimir frases con dichos datos
for nombre, edad, ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')