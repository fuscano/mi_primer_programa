
apetece_helado = input("¿Te apetece un helado?(si/no):").upper()
tiene_dinero = input("¿Tienes dinero para un helado?(si/no):").upper()
esta_tu_tia=input("estas con tu tia?(si/no)").upper()

if apetece_helado == "SI" and(tiene_dinero == "SI" or esta_tu_tia == "SI"):
    print("Pues comete un helado")
else:
    print("Pues nada")

