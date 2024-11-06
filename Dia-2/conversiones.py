num_1 = 20
num_2 = 30.5

print(type(num_1))
print(type(num_2))

# Conversión Implícita
num_1 = num_1 + num_2 # Reescribimos num_1 y cambia su tipo implícitamente
print(type(num_1))

# Conversión Explícita
num_3 = 5.8
print(num_3)
print(type(num_3))

num_4 = int(num_3)
print(num_4)
print(type(num_4))

edad = input('Dime tu edad: ')
print(type(edad))

edad = int(edad)
print(type(edad))

nueva_edad = 1 + edad
print(f'Tu nueva edad va a ser: {nueva_edad}')
