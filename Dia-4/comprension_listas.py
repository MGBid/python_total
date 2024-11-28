palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

# Forma nueva de hacer algo más eficiente con comprensión de listas
lista_comprension = [letra for letra in palabra]

print(lista_comprension)

lista_range = [num for num in range(0, 21)]

lista_range_pares = [num_par for num_par in range(0, 21, 2)]

print(lista_range)

print(lista_range_pares)

# También puedo modificar esos números, por ejemplo dividirlo por 2. Puedo alterar el número antes de incorporarlo a la lista
lista_modificando_numeros = [numero/2 for numero in range(0, 21, 2)]

print(lista_modificando_numeros)

# Podemos condicionar
condicionando = [n for n in range(0, 21, 2) if n * 2 > 10]
print(condicionando)

# Cambia la sintaxis si agregamos el else. El costo es la legibilidad
lista_condicionada = [numero if numero * 2 > 10 else 'NO' for numero in range(0, 21, 2)]
print(lista_condicionada)

# Uso de la vida real
pies = [10, 20, 30, 40, 50]
metros = [valor / 3.281 for valor in pies]
print(metros)
