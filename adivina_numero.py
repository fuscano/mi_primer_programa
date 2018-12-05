
number_to_guess=2


intentos=0
while intentos < 4:
    user_number = int(input("Adivina un numero:"))
    if number_to_guess == user_number:
        print("has ganado")
    else:
        intentos +=1
        print("has perdido")


print("No tienes mas intentos")
