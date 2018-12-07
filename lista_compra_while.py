

mi_lista = ['lechuga', 'tomate', 'helado', 'pan', 'pasta', 'olivas', 'atun', 'fanta']
mi_lista.append('pimientos')



mi_lista = []
input_usuario = ''
while input_usuario != 'fin':
    input_usuario=input('Que necesitas comprar:(escribe fin para salir)')
    if input_usuario != 'fin:':
        mi_lista.append(input_usuario)


largo_lista = len(mi_lista)
indice_actual = 0

while indice_actual < largo_lista:
    print('tengo que comprar {}'.format(mi_lista[indice_actual]))
    indice_actual +=1
print('esta es la lista de la compra')

mi_lista = [34, 15, 35, 25, 18]
for item in mi_lista:
    print('tengo que comprar {}'.format(item))
