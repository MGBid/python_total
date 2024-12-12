'''Práctica sobre Argumentos Indefinidos (**kwargs) 3
Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
'''

def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')

    for nombre_argumento, valor_argumento in kwargs.items():
        print(f'{nombre_argumento}: {valor_argumento}')

describir_persona("María", color_ojos="azules", color_pelo="rubio")
