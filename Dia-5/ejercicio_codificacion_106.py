'''Práctica sobre Argumentos Indefinidos (**kwargs) 1
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.'''
def cantidad_atributos(**kwargs):
    print(len(kwargs))
    return len(kwargs)

cantidad_atributos(nombre='Juan', apellido='Perez', edad=50)
