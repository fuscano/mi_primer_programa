


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30, 60, 100]


for indices in range(len(numeros)):
    numero = numeros[indices]

    if numero % 3 == 0 or numero % 5 == 0:
        numeros[indices] = ''

        if numero % 3 == 0 :
            numeros[indices] += 'Fizz'

        if numero % 5 == 0 :
            numeros[indices] += 'Buzz'
print(numeros)

'''
Realizar el FizzBuzz con las mismas reglas pero en el caso que el numero sea divisible entre 3 y 5, cambiar el texto por “Bazinga”.
'''
numeros_bazinga = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30, 60, 100]

for indices in range(len(numeros_bazinga)):
    numero = numeros_bazinga[indices]

    if numero % 3 == 0 or numero % 5 == 0:
        numeros_bazinga[indices] = ''
        numeros_bazinga[indices] += 'Bazinga'

print(numeros_bazinga)

'''
Crear un programa que encuentre el numero más grande de una lista (sin usar la función max).
'''
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 160, 151, 12, 13, 14, 15, 20, 30, 60, 120]
max_valor = 0

for indice in range(len(lista_numeros)):
    valor = lista_numeros[indice]
    if valor > max_valor:
        max_valor = valor

print('El maximo valor es {}'.format(max_valor))

'''
Crear un programa que guarde e imprima varias listas con todos los números que estén dentro de una lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.

Ejemplo:

input = [1, 10, 70, 30, 50, 55]

multiplos_dos = [10, 70, 30, 50]
multiplos_tres = [30]
multiplos_cinco = [10, 70, 30, 60, 55]
multiplos_siete = [70]
'''


entrada = [1, 10, 70, 30, 50, 55]
multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []



for indice_nuevo in range(len(entrada)):
    nuevo_valor = entrada[indice_nuevo]
    if nuevo_valor % 2 == 0 :
        multiplos_dos.append(nuevo_valor)
    if nuevo_valor % 3 == 0 :
        multiplos_tres.append(nuevo_valor)
    if nuevo_valor % 5 == 0:
        multiplos_cinco.append(nuevo_valor)
    if nuevo_valor % 7 == 0 :
        multiplos_siete.append(nuevo_valor)
print('Los multipos de 2 son {}'.format(multiplos_dos))
print('Los multipos de 3 son {}'.format(multiplos_tres))
print('Los multipos de 5 son {}'.format(multiplos_cinco))
print('Los multipos de 7 son {}'.format(multiplos_siete))