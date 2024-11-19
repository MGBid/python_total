# Es importante que el nombre de nuestro archivo o .py no tenga el mismo nombre del módulo o librería que vamos a importar, porque esto generaría una importación circular. 
# from random import randint
from random import *

print('Ver cómo se importan los métodos de una librería')
aleatorio = randint(1, 50)
print(f'Aleatorio con randint: {aleatorio}')

aleatorio_uniform = round(uniform(1, 5), 1) # Nos da un valor float dentro del rango especificado
print(f'Aleatorio con uniform y round: {aleatorio_uniform}')

# Elije un número float entre 0 y 1
aleatorio_random = random()
print(f'Aleatorio con random: {aleatorio_random}')

# Choice permite trabajar con una selección aleatoria dentro de los elementos de una lista.
aleatorio_choice = choice([21, 3, 19, 68, 10, 12, 64, 13, 7, 92, 9, 94, 5, 0])
colores = ['Azul', 'Verde', 'Rojo', 'Amarillo', 'Lila', 'Celeste', 'Violeta']
print(f'Aleatorio con Choice: {aleatorio_choice}')
print(f'Aleatorio con Choice Colores: {choice(colores)}')

print('* Método Shuffle (mezclar) que también trabaja con aleatorio')
# Es útil en los juegos de cartas, NO se puede usar con STRINGS
numeros = list(range(5, 51, 5))
print(f' Números: {numeros}')

shuffle(numeros)
print(f'Números después de shuffle: {numeros}')