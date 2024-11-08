variable_true = True
variable_false = False

print(type(variable_true))
print(variable_true)
print('---------------')

# Ahora la asignamos de manera INDIRECTA
numero = 5 > 2+3
print(type(numero))
print(numero)
print('---------------')

numero = 5 == 2+3
print(type(numero))
print(numero)
print('---------------')

print('OTRA FORMA DE GENERAR LA VARIABLE BOOLEANA EXPLÍCITAMENTE ES ENCERRAR EN UN CASTEO LA EXPRESIÓN bool(expresion)')
numero = bool(5 >= 2+3)
print(type(numero))
print(numero)
print('---------------')

lista = [1, 2, 3, 4]
control = 5 in lista
print(type(control))
print(control)
print('---------------')

control = 5 not in lista
print(type(control))
print(control)
print('---------------')

