
def reverse_string(string_to_reverse):
    string__reversed = ''
    current_index = len(string_to_reverse) - 1
    while current_index >= 0:
        string__reversed += string_to_reverse[current_index]
        current_index -= 1
    return string__reversed



print(reverse_string('aguacate'))




'''
Escribe una función que encuentre el numero más grande entre 3 numeros.

'''
def numero_mas_grande(numero_uno, numero_dos, numeor_tres):
    numero_max=max(numero_uno, numero_dos, numeor_tres)
    return numero_max

print('El numeor mas grande es {}'.format(numero_mas_grande(15, -45, 35)))


'''Comprobar si el numero esta dentro del rango'''

def numero_dentro_rango(numero, minimo, maximo):
    if numero >= minimo and numero <= maximo:
        return print('El numero esta en el rango')
    else:
        return print('El numeor no esta dentro del rango')


numero_dentro_rango(15, 1, 100)



'''
Escribe una función que reciba una lista de números y devuelva otra pero conteniendo solo los números pares.
'''

def numeros_pares(lista):
    nueva_lista = []

    for numero in lista:
        if numero % 2 == 0:
            nueva_lista.append(numero)
    return nueva_lista

print(numeros_pares([2, 15, 25, 12, 24, 36]))




