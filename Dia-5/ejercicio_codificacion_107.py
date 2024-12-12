'''Práctica sobre Argumentos Indefinidos (**kwargs) 2
Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.'''
def lista_atributos(**kwargs):
    return list(kwargs.values())

milista = lista_atributos(nombre='Juan', apellido='Perez', edad=50)
print(milista)
print(type(milista))
