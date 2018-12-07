
numeros_usuario = []
numero_del_usuario = ''

while len(numeros_usuario) < 5:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input('Dimer un numero: ')
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario=''
    print('!numeor añadido¡')

numero_grnade=numeros_usuario[0]
n_numeros_introducidos=0

for numero in numeros_usuario:
    if numero > numero_grnade:
        numero_grnade=numero
    n_numeros_introducidos +=1

media = sum(numeros_usuario)/n_numeros_introducidos

print('El número más grande es {}'.format(numero_grnade))
print('El numero mas pequeño es {}'.format(min(numeros_usuario)))
print('El numero de numeros introducidos es {}'.format(n_numeros_introducidos))
print('La meida es {}'.format(media))