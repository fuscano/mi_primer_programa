
valores_a_sustituir = [1, 2, 'hola', 'adios']
string_a_cambiar = 'Hola, numero {}, numero {}, {} y {}'

for valor in valores_a_sustituir:
    string_a_cambiar = string_a_cambiar.replace('{}', str(valor), 1)

print(string_a_cambiar)

# EJERCICIO 1: Crear un programa que cambie todas las ‘A’ o ‘a’ por la string ‘VACA’ de una string introducida por el usuario.

frase_usuario = input('introduzca una frase: ')

frase_cambiada_A = frase_usuario.replace('A', 'VACA')
frase_cambiada_final = frase_cambiada_A.replace('a', 'VACA')
print(frase_cambiada_final)

# EJERCICIO 2: Crear un programa que le repita al usuario odo lo que dice pero con todas las vocales cambiadas por i

frase_usuario_i = input('Introduzca una frase: ')
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    frase_usuario_i = frase_usuario_i.replace(vocal, 'i')

print(frase_usuario_i)

# EJERCICIO 3: Crear un programa que cambia las vocales por su numero de aparición. Por ejemplo la string “aurora boreal” se convertiría en “12r3r4 b5r67l”

frase = 'aurora boreal'
numero_sustitucion = 0

for letra in frase:
    if letra in vocales:
        numero_sustitucion += 1
        frase=frase.replace(letra, str(numero_sustitucion), 1)

print(frase)

