
pokemon_elegido = input('¿Contra que poquemon quieres combatir?(Squirtle/Charmander/Bulbasur):')

vida_enemigo=0
vida_picachu = 100
ataque_enemigo = 0
nombre_pokemon = ''


if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    ataque_enemigo = 8
    nombre_pokemon = "Squirtle"

elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    ataque_enemigo = 7
    nombre_pokemon = "Charmander"

elif pokemon_elegido == "Bulbasur":
    vida_enemigo = 100
    ataque_enemigo = 10
    nombre_pokemon = "Bulbasur"



while vida_picachu > 0 and vida_enemigo > 0:
    #Elegimos el ataque
    ataque_elegido = input('que ataque usamos?(chispaso/bola voltio):')
    if ataque_elegido == 'chispaso':
       vida_enemigo -= 10
    elif ataque_elegido == 'bola voltio':
        vida_enemigo -= 12
    #Mostramos el resultado del ataque
    print('la vida de {} ahora es de {}'.format(nombre_pokemon, vida_enemigo))

    print('{} te hace un ataque de {} de daño'.format(nombre_pokemon, ataque_enemigo))
    vida_picachu -= ataque_enemigo
    print('La vida de picachu es de {}'.format(vida_picachu))




if vida_enemigo<=0:
    print('Has ganado')
else:
    print('Has perdido')
print('el cambate ha terminado')
