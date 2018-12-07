
'''
Introduce un numero y suelta la tabla de multiplicar
'''

n_tabla = int(input('Introduce el numeor de la tabla que quieras:'))

print('del 1 al 10')
for multiplo in range(1, 11):
    print('{} X {} = {}'.format(multiplo, n_tabla, multiplo*n_tabla))

print('del 5 al 15')
for multiplo in range(5, 16):
    print('{} X {} = {}'.format(multiplo, n_tabla, multiplo*n_tabla))

print('solo los pares')
for multiplo in range(1, 16):
    if ((n_tabla*multiplo)%2) == 0:
        print('{} X {} = {}'.format(multiplo, n_tabla, multiplo*n_tabla))

print('Tabla invertida')
for multiplo in range(1, 11):
    print('{} X {} = {}'.format(11-multiplo, n_tabla, multiplo*n_tabla))
