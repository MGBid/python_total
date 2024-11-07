print('Los Strings son Inmutables, no se puede cambiar a través de sus índices')
nombre = 'Carina'
# nombre[0] = 'K' => FALLA el print()
# Sí podemos reasignarle un valor
nombre = 'Karina'
print(nombre)

n_1 = 'Kari'
n_2 = 'na'
print('---\n' + n_1 + n_2)
print(n_1 * 10)

poema = '''Mil pequeños peces blancos
como si hirviera
el color del agua'''
print(poema)

print('Podemos preguntar si existe una palabra dentro del poema/string')
print('agua' in poema)
print('sol' in poema)
print('sol' not in poema)