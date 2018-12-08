

lista_datos = [1, 2, 3, 'ard', False, [], True, 22, 2.1]
lista_tipos = []

for dato in lista_datos:
    lista_tipos.append(type(dato))

print(lista_tipos)

string = input('introduzca una palabra:')
largo = 0
for letra in string:
    largo +=1
largo = [largo]
print('El largo de la palabra {} es {}'.format(string, largo))

lista_numeros = []

while len(lista_numeros) < 1:
    numero = int(input('Introduce un numero: '))
    lista_numeros.append(numero)


multiplo=1
for variable in lista_numeros:
    multiplo *= variable


print('La lista de numeros introducidos es {}'.format(lista_numeros))
print('El resultado de la multiplicacion es {}'.format(multiplo))





