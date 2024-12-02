def chequear_3_cifras(numero):
    return numero in range(100, 1000)

resultado = chequear_3_cifras(658)
print(resultado)

suma = 586 + 402
print(chequear_3_cifras(suma))

# Lo mismo probando listas
def chequear_3_cifras_lista(lista):
    for numero in lista:
        if numero in range(100, 1000):
            return True
        else:
            pass
    return False

resultado_lista = chequear_3_cifras_lista([55, 99, 6000])
print(f'---\n{resultado_lista}')

resultado_lista = chequear_3_cifras_lista([555, 99, 6000])
print(f'---\n{resultado_lista}')

def chequear_3_cifras_retorna_lista(lista):
    lista_creada = []
    for numero in lista:
        if numero in range(100, 1000):
            lista_creada.append(numero)
        else:
            pass
    return lista_creada

lista_nueva = chequear_3_cifras_retorna_lista([555, 99, 600])
print('---------------')
print(lista_nueva)
