




lista_random = [15, 'hola', 25, 59, 'cafe']
lista_enteros = []
lista_string = []
for elemento in lista_random:
    elemento=str(elemento)
    if elemento.isdigit():
        lista_enteros.append(elemento)
    else:
        lista_string.append(elemento)
print('La lista de entereos es {} y la de string {}'.format(lista_enteros, lista_string))