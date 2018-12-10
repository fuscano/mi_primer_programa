
salida = False
agenda = dict()

while not salida:
    accion = input('¿Que quieres hacer?[Añadir numero [A]]/[Consultar numero [C]]/[Salir de la agenda [S]]: ')

    #Acccion de guardar
    if accion == 'A':
        print('Vamos a añadir un numero de telefono:')
        print('-------------------------------------------')
        nombre = input('Nombre: ')
        numero = input('Numero: ')
        agenda[nombre] = numero

    #Acccion de consultar
    elif accion == 'C':
        print('Consultar numero: ')
        print('-------------------------------------------')
        nombre = input('De quien quiere saber el numero: ')
        print(agenda[nombre])
    #Accion de salir
    elif accion == 'S':
        salida = True


'''
Crea un programa que cuente el número de veces que aparece una palabra en una string
'''

frase = input('Introduce una frase: ')

cuenta_palabras = dict()

for palabra in frase.split():
    if palabra in cuenta_palabras:
        cuenta_palabras[palabra] += 1
    else:
        cuenta_palabras[palabra] = 1

print(cuenta_palabras)

'''
Crea una función que muestre por pantalla un texto y tantas barritas de subrayado como larga sea la string
'''

def barritas(titulo):
    numero_barritas=len(titulo)
    barritas='-'*numero_barritas
    return print('{}\n{}'.format(titulo, barritas))

barritas('Don Quijote de la Mancha')