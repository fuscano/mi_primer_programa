
"""
crea un programa que te cuente el numero de vocales y consonantes dentro de una frase introducida por el usuario
"""
frase_usuario = input('una frase: ')

vocales = ['a', 'e', 'i', 'o', 'u']

n_vocales = 0
n_consonantes =0
n_espacio = 0
n_espacio = 0
n_punto = 0
n_coma = 0
lista_vocales=[]
for letra in frase_usuario:
    if letra in vocales:
        n_vocales += 1
        lista_vocales.append(letra)
    elif letra == ' ':
        n_espacio += 1
    elif letra == '.':
        n_punto += 1
    elif letra == ',':
        n_coma += 1
    else:
        n_consonantes += 1

print('las vocales son {}'.format(n_vocales))
print('las consonantes son {}'.format(n_consonantes))
print('las comas son {}'.format(n_coma))
print('los punto son {}'.format(n_punto))
print('los espacios son {}'.format(n_espacio))
print(lista_vocales)
